import os
from collections import Counter
string=''
path="/home/anusha/Documents/thesis/td/"
dirs=os.listdir(path)  #gives years
for dir in dirs: 
	innerpath=path+dir+'/' #creating path with years
	innerdirs=os.listdir(innerpath) #getting all sub directories in year directory
	for innerdir in innerdirs: #traversing sub dir
		npath=innerpath+innerdir+'/' 
		files=os.listdir(npath) #getting all files in subfolder
		for f in files:
			#print(f)
			toread=open(npath+f,'r',encoding='utf-8')
			p=toread.read()
			string=string+p
string=string.split() #comment this for letters

print(Counter(string))
	 

