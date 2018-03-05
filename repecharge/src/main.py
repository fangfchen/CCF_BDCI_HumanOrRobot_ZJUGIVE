from write_data2db import write_train2db, write_test2db, write_media2db
from process_train_test import get_fraud, f1_score, get_middle_level, get_exceptional_uas, get_exceptional_ua_ranks, write_ranks2file
from merge_ranks import merge_ranks

if __name__ == "__main__":
	train_infile = ["../data/ccf_data_1", "../data/ccf_data_2", "../data/ccf_data_3"]  # train data
	test_infile = ["../data/test_data_1_1118", "../data/test_data_2_1118"]  # test data
	media_infile = "../data/ccf_media_info.csv"

	complete_data = "../data/complete_data.csv"
	final_test = "../data/final_test.csv"

	exceptional_uas = "../data/exceptional_uas.csv"

	test_exceptional_ua_ranks_file = "../data/exceptional_ua_ranks.csv"

	low_level_ranks_file = "../data/low_level_ranks.csv"

	middle_level_ranks_file = "../data/middle_level_ranks.csv"

	final_result = "../data/final_result.csv"


	print("start writing train data into database...")
	for i in range(len(train_infile)):
		if i == 0:
			write_train2db(train_infile[i], True)
		else:
			write_train2db(train_infile[i], False)

	print("start writing test data into database...")
	for i in range(len(test_infile)):
		if i == 0:
			write_test2db(test_infile[i], True)
		else:
			write_test2db(test_infile[i], False)

	print("start writing media data into database...")
	write_media2db(media_infile)

	for i in range(80, 100):
		print(f1_score(complete_data, i/100))

	low_level_ranks = get_fraud(final_test, 0.9)  # get low level fraud rows
	middle_level_ranks = get_middle_level(final_test)  # get middle level fraud rows
	get_exceptional_uas(complete_data, exceptional_uas)  # write exceptional useragents into outfile
	get_exceptional_ua_ranks(exceptional_uas, final_test, test_exceptional_ua_ranks_file)  # write ranks of exceptional useragents into outfile

	write_ranks2file(low_level_ranks, low_level_ranks_file)  # write low level rows num into outfile
	write_ranks2file(middle_level_ranks, middle_level_ranks_file)  # write middle level rows num into outfile

	total_ranks = merge_ranks([low_level_ranks_file, middle_level_ranks_file, test_exceptional_ua_ranks_file])  # merge rows num

	with open(final_result, "w") as fw:
		for rank in total_ranks:
			fw.write(str(rank) + "\n")
