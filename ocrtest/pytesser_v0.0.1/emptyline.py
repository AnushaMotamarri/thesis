f=open("wordlist1.txt",'a+',encoding='utf-8')
with open('wordlist.txt','r') as file:
    for line in file:
        if not line.isspace():
            f.write(line)
