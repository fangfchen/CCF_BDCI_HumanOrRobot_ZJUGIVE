import csv


def get_fraud(infile, ratio):
	ip_dt_map = {}
	ranks = []
	with open(infile) as fr:
		line = fr.readline().rstrip("\n")
		while line != "":
			line_list = line.split(",")
			rank = int(line_list[0])
			dt = line_list[1]
			cookie = line_list[2]
			ip = line_list[3]
			timestamp = line_list[9]
			camp = line_list[10]
			placement_id = line_list[16]
			ip_dt_key = ip + "_" + dt
			key = cookie + "_" + ip + "_" + timestamp + "_" + camp + "_" + placement_id
			if not ip_dt_map.get(ip_dt_key):
				ip_dt_map[ip_dt_key] = {key: [rank]}
			else:
				if not ip_dt_map[ip_dt_key].get(key):
					ip_dt_map[ip_dt_key][key] = [rank]
				else:
					ip_dt_map[ip_dt_key][key].append(rank)
			line = fr.readline().rstrip("\n")
	for ip_dt_key in ip_dt_map:
		key_ranks_map = ip_dt_map[ip_dt_key]
		total = 0
		repeated_records = 0
		tmp_ranks = []
		for key in key_ranks_map:
			total += len(key_ranks_map[key])
			if len(key_ranks_map[key]) >= 2:
				repeated_records += len(key_ranks_map)
				tmp_ranks += key_ranks_map[key]
		if repeated_records / total >= ratio:
			ranks += tmp_ranks
	return sorted(ranks)


def f1_score(infile, ratio):
	tp = 0  # predict to be fraud and turned out to be fraud
	fp = 0  # predict to be fraud and turned out to be unfraud
	fn = 0  # predict to be unfraud and turned out to be fraud
	ranks = get_fraud(infile, ratio)
	cnt = 0
	rank_flag_maps = {}
	with open(infile) as fr:
		line = fr.readline().rstrip("\n")
		while line != "":
			line_list = line.split("\x01")
			rank_flag_maps[line_list[0]] = line_list[-1]
			line = fr.readline().rstrip("\n")
			if cnt % 1000000 == 0:
				print(cnt / 1000000)
			cnt += 1

	m = 0
	rank = 0
	while rank < cnt:
		try:
			if rank == ranks[m]:
				if rank_flag_maps[str(rank)] == "1":
					tp += 1
				else:
					fp += 1
				m += 1
			else:
				if rank_flag_maps[str(rank)] == "1":
					fn += 1
			rank += 1
		except:
			if rank_flag_maps[str(rank)] == "1":
				fn += 1
			rank += 1
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1 = 2 * precision * recall / (precision + recall)
	return f1


def get_middle_level(infile):
	cookie_map = {}
	ranks = []
	cnt = 0
	with open(infile, "r") as fr:
		line = fr.readline().rstrip("\n")
		while line != "":
			line_list =line.split(",")
			key = line_list[2]+"_"+line_list[4]
			value = line_list[3] + "_" + line_list[5]  # f_camp
			if not cookie_map.get(key):
				cookie_map[key] = {value: [line_list[0]]}
			else:
				if not cookie_map[key].get(value):
					cookie_map[key][value] = [line_list[0]]
				else:
					cookie_map[key][value].append(line_list[0])
			line = fr.readline().rstrip("\n")
			if cnt % 1000000 == 0:
				print(cnt/1000000)
			cnt += 1
	print(len(cookie_map))
	cnt = 0
	for key in cookie_map:
		value_ranklist = cookie_map[key]  # {27953_1401: [1,2,3], 27953_1402:[4,5,6]}
		if len(value_ranklist) >= 2:
			for value_rank in value_ranklist:
				ranks += value_ranklist[value_rank]
		if cnt % 1000000 == 0:
			print(cnt/1000000)
		cnt += 1
	return ranks


def get_exceptional_uas(infile, outfile):
	"""
	wirte exceptional useragent into outfile
	:param infile:	train data
	:param outfile: exceptional useragents
	:return:
	"""
	ua_maps = {}
	with open(infile) as fr:
		csv_reader = csv.reader(fr)
		next(csv_reader)
		for line_list in csv_reader:
			ua = line_list[-5]
			flag = line_list[-1]
			if not ua_maps.get(ua):
				if flag == "0":
					ua_maps[ua] = {"total": 1, "unfraud": 1}
				else:
					ua_maps[ua] = {"total": 1, "fraud": 1}
			else:
				ua_maps[ua]["total"] += 1
				if flag == "0":
					ua_maps[ua]["unfraud"] += 1
				else:
					ua_maps[ua]["fraud"] += 1
	with open(outfile, "w") as fw:
		for ua in ua_maps:
			values = ua_maps[ua]
			total_num = values["total"]
			fraud_num = values["fraud"]
			fraud_ratio = fraud_num / total_num
			if total_num >= 1000 and fraud_ratio >= 0.95:
				fw.write(ua + "," + str(total_num) + "," + str(fraud_ratio) + "\n")


def get_exceptional_ua_ranks(ua_infile, test_infile, outfile):
	exception_ua_ranks = []
	uas = []
	with open(ua_infile) as fr:
		csv_reader = csv.reader(fr)
		for line_list in csv_reader:
			uas.append(line_list[0])
	with open(test_infile) as fr:
		csv_reader = csv.reader(fr)
		for line_list in csv_reader:
			if line_list[-5] in uas:
				exception_ua_ranks.append(int(line_list[0]))

	with open(outfile, "w") as fw:
		for rank in exception_ua_ranks:
			fw.write(str(rank) + "\n")


def write_ranks2file(ranks, outfile):
	with open(outfile, "w") as fw:
		for rank in ranks:
			fw.write(str(rank) + "\n")
