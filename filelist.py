import os


for item in os.listdir("."):
	if os.path.isfile(item):
		print("{} is a file".format(item))
	
	if os.path.isdir(item):
		print("{} is a folder")
