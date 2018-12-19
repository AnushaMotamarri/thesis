import os
filename = "probable_stopwords"
file = open(filename, "r")
for line in file:
   print(line)
a = line.split(":")

path="/home/anusha/Documents/thesis/td/"
dirs=os.listdir(path)  #gives years

for word in a:
	count=0

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
				if word in p:
					count=1+count
	print(str(word)+" "+str(158000/count))
