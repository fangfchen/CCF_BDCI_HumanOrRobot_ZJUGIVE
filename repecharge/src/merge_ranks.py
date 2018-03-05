def merge_ranks(infiles):
	ranks = []
	for infile in infiles:
		with open(infile) as fr:
			line = fr.readline().rstrip("\n")
			while line != "":
				ranks.append(int(line))
				line = fr.readline().rstrip("\n")

	rank_set = list(set(ranks))
	sorted_ranks = sorted(rank_set)
	return sorted_ranks
