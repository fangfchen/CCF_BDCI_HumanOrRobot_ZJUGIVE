import pymysql
import urllib.request as ur
import csv
cnt = 0


def write_train2db(train_infile, has_header):
	"""
        infile: AdMaster_train_dataset
	"""
	coon = pymysql.connect(host="localhost", user="root", password="123456",
                           db="test", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
	sql = 'insert into complete_data values('
	for i in range(0, 24):
		sql += '%s,'
	sql = sql.rstrip(',')
	sql += ')'
	cnt = 0
	with coon.cursor() as cur:
		with open(train_infile, 'r', encoding='utf-8') as fr:
			if has_header:
				fr.readline()  # 第一个文件有表头，需要去掉
			line = fr.readline().rstrip("\n")
			insert_list = []
			with coon.cursor() as cursor:
				while line != '':
					line = fr.readline()
					line = line.rstrip('\n')
					line_list = line.split(',')
					line_list[3] = int(line_list[3])
					line_list[-5] = ur.unquote(line_list[-5]).encode("unicode_escape")
					line_list[-1] = line_list[-1]
					insert_list.append([cnt] + line_list)
					if cnt % 1000000 == 0:
						print(cnt / 1000000)
						cursor.executemany(sql, insert_list)
						coon.commit()
						insert_list = []
					cnt += 1
					line = fr.readline().rstrip("\n")
				cur.executemany(sql, insert_list)
				coon.commit()



def write_test2db(test_infile, has_header):
	"""
            infile: AdMaster_train_dataset
        """
	coon = pymysql.connect(host="localhost", user="root", password="123456",
						   db="HumanOrRobot", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
	sql = 'insert into complete_data values('
	for i in range(0, 24):
		sql += '%s,'
	sql = sql.rstrip(',')
	sql += ')'
	cnt = 0
	with coon.cursor() as cur:
		with open(test_infile, 'r', encoding='utf-8') as fr:
			if has_header:
				fr.readline()  # 第一个文件有表头，需要去掉
			line = fr.readline().rstrip("\n")
			insert_list = []
			with coon.cursor() as cursor:
				while line != '':
					line = fr.readline()
					line = line.rstrip('\n')
					line_list = line.split(',')
					line_list[3] = int(line_list[3])
					line_list[-5] = ur.unquote(line_list[-5]).encode("unicode_escape")
					line_list[-1] = line_list[-1]
					insert_list.append([cnt] + line_list)
					if cnt % 1000000 == 0:
						print(cnt / 1000000)
						cursor.executemany(sql, insert_list)
						coon.commit()
						insert_list = []
					cnt += 1
					line = fr.readline().rstrip("\n")
				cur.executemany(sql, insert_list)
				coon.commit()


def write_media2db(in_file):
	"""
    将媒体信息写入数据库中
    :param in_file:媒体文件
    :return: null
    """
	with open(in_file, 'r', encoding="utf-8") as fr:
		fr.readline()
		csv_reader = csv.reader(fr)
		coon = pymysql.connect(host="localhost", user="root", password="123456",
                               db="HumanOrRobot", charset="UTF8", cursorclass=pymysql.cursors.DictCursor)
		sql = "insert into media values(%s, %s, %s, %s, %s)"
		insert_list = []
		with coon.cursor() as cur:
			for line in csv_reader:
				insert_list.append(line)
			cur.executemany(sql, insert_list)
			coon.commit()
