import os

path = r"C:\Users\USER\Music\pyMuse"

for x in os.listdir(path):
	list = x.split(".ff.")
	new = list[-1]
	os.rename(x,new)