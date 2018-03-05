def get_fraud(infile):
	ip_dt_map = {}
	ranks = []
	cnt = 0
	with open(infile) as fr:
		line = fr.readline().rstrip("\n")
		while line != "":
			line_list = line.split("\x01")
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
			if cnt % 1000000 == 0:
				print(cnt / 1000000)
			cnt += 1
	for ip_dt_key in ip_dt_map:
		key_ranks_map = ip_dt_map[ip_dt_key]
		total = 0
		repeated_records = 0
		tmp_ranks = []
		for key in key_ranks_map:
			total += len(key_ranks_map[key])
			if len(key_ranks_map[key]) >= 2:
				repeated_records += len(key_ranks_map[key])
				tmp_ranks += key_ranks_map[key]
		if repeated_records / total == 1.0:
			ranks += tmp_ranks
	return sorted(ranks)


def f1_score(infile):
	tp = 0  # predict to be fraud and turned out to be fraud
	fp = 0  # predict to be fraud and turned out to be unfraud
	fn = 0  # predict to be unfraud and turned out to be fraud
	ranks = get_fraud(infile)
	cnt = 0
	rank_flag_maps = {}
	with open(infile) as fr:
		line = fr.readline().rstrip("\n")
		while line != "":
			line_list =line.split("\x01")
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
