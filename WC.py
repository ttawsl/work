"# -*- coding: utf-8 -*-"
import sys
import re
import os

class all():

	def __init__(self, file_list, order_number, order_list):
		self.file_list = file_list
		self.order_number = order_number
		self.order_list = order_list

	def chara(self, ff):
		count1 = 0
		for i in ff:
			count1 += len(i.rstrip())
		return count1

	def word(self, ff):
		count2 = 0
		string_after = ""
		for i in ff:
			string_after+=i.rstrip()
		new_a = re.sub("[^a-zA-z0-9\s]"," ",string_after)
		words = new_a.split()
		for word in words:
			if word != "":
				count2 += 1
		return count2

	def line(self,ff):
		return len(ff)

	def file_recurse(self,pathh):
		files = os.listdir(pathh)
		p1 = self.order_list[self.order_number-1].split(".")
		p = "."+ p1[1].upper()
		for f in files:
			real_path = os.path.join(pathh,f)
			if os.path.isfile(real_path):
				spl = os.path.splitext(real_path)
				if spl[1].upper() == p:
					self.file_list.append(real_path)
			if os.path.isdir(real_path):
				self.file_recurse(real_path)

	def explain(self,k,flag):
		if re.search(r"//",k) != None:
			flag = 1
			return flag
		if re.search(r"/\*",k) != None:
			flag = 0
		if re.search(r"\*/",k) != None:
			flag=1
			return flag

	def complex_data(self,ff):
		empty_l = 0
		code_num = 0
		explanation = 0
		flag = 0
		for i in ff:
			k = i.strip()
			if len(k)<=1:
				empty_l += 1
			elif all.explain(self,i,flag)==True:
				explanation += 1
			elif len(k)>1:
				code_num += 1
		print("空行："+str(empty_l))
		print("代码行："+str(code_num))
		print("注释行："+str(explanation))

	def menu(self):
		for f in self.file_list:
			try:
				with open(f) as file_object:
					ff = file_object
					fa = ff.readlines()
					print(os.path.abspath(f))
					for i in range(1, num-1):
						if self.order_list[i] == '-c':
							print("字符数: " + str(all.chara(self,fa)))
						elif self.order_list[i] == '-w':
							print("单词数: " + str(all.word(self,fa)))
						elif self.order_list[i] == "-l":
							print("行数: " + str(all.line(self,fa)))
						elif self.order_list[i] == '-s':
							continue
						elif self.order_list[i] == '-a':
							all.complex_data(self,fa)
						else:
							print("指令错误")
			except FileNotFoundError:
				m = "file: " + os.path.basename(f) + " does not exist"
				print (m)

if __name__ == "__main__":
	num = len(sys.argv)
	file_list = []
	w = all(file_list, num, sys.argv)
	if len(file_list) == 0:
		pp = os.path.abspath(__file__)
		w.file_recurse(os.path.dirname(pp))
	if len(file_list) == 0:
		print("此文件不存在")
	else:
		w.menu()
