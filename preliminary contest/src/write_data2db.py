# coding=utf-8

import pymysql
import urllib.request as ur
import csv


def write_train2db(train_infile):
	"""
        infile: AdMaster_train_dataset
	"""
	coon = pymysql.connect(host="localhost", user="root", password="123456",
						   db="test", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
	sql = 'insert into complete_data values('
	for i in range(0, 22):
		sql += '%s,'
	sql = sql.rstrip(',')
	sql += ')'
	cnt = 0
	with coon.cursor() as cur:
		with open(train_infile) as fr:
			line = fr.readline().rstrip("\n")
			insert_list = []
			while line != "":
				line_list =  line.split("\x01")
				line_list[0] = int(line_list[0])
				line_list[-5] = ur.unquote(line_list[-5])
				insert_list.append(line_list)
				if cnt % 1000000 == 0:
					print(cnt/1000000)
					cur.executemany(sql, insert_list)
					coon.commit()
					insert_list = []
				cnt += 1
				line = fr.readline().rstrip("\n")
			cur.executemany(sql, insert_list)
			coon.commit()


def write_test2db(test_infile):
	"""
		infile: AdMaster_train_dataset
	"""
	coon = pymysql.connect(host="localhost", user="root", password="123456",
						   db="test", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
	sql = 'insert into final_test values('
	for i in range(0, 22):
		sql += '%s,'
	sql = sql.rstrip(',')
	sql += ')'
	cnt = 0
	with coon.cursor() as cur:
		with open(test_infile) as fr:
			line = fr.readline().rstrip("\n")
			insert_list = []
			while line != "":
				line_list = line.split("\x01")
				line_list[0] = int(line_list[0])
				line_list[-5] = ur.unquote(line_list[-5])
				line_list.append("")
				insert_list.append(line_list)
				if cnt % 1000000 == 0:
					print(cnt/1000000)
					cur.executemany(sql, insert_list)
					coon.commit()
					insert_list = []
				cnt += 1
				line = fr.readline().rstrip("\n")
			cur.executemany(sql, insert_list)
			coon.commit()


def write_media2db(meida_infile):
	coon = pymysql.connect(host="localhost", user="HumanOrRobot", password="123456",
						   db="test", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
	sql = "insert into media values(%s, %s, %s, %s, %s)"
	insert_list = []
	with open(meida_infile, 'r', encoding="gbk") as fr:
		fr.readline()
		csv_reader = csv.reader(fr)
		coon = pymysql.connect(host="localhost", user="HumanOrRobot", password="123456",
							   db="test", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
		sql = "insert into media values(%s, %s, %s, %s, %s)"
		insert_list = []
		with coon.cursor() as cur:
			for line in csv_reader:
				# print(len(line[-1]))
				insert_list.append(line)
			cur.executemany(sql, insert_list)
			coon.commit()
	print("over~")
