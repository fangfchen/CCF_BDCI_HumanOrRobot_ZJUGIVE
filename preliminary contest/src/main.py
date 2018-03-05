from write_data2db import write_train2db, write_test2db, write_media2db
from get_fraud import get_fraud, f1_score


if __name__ == "__main__":
	train_infile = "../data/AdMaster_train_dataset"
	test_infile = "../data/final_ccf_test_0919"
	media_infile = "../data/ccf_media_info.csv"
	result = "../data/result.csv"

	"""write train data, test data and media data into database"""
	# write_train2db(train_infile)
	# write_test2db(test_infile)
	# write_media2db(media_infile)

	"""print f1-score of the train data"""
	print(f1_score(train_infile))

	"""get fraud ranks of the test data"""
	ranks = get_fraud(test_infile)

	"""write result ranks into outfile"""
	with open(result, "w") as fw:
		for rank in ranks:
			fw.write(str(rank) + "\n")
