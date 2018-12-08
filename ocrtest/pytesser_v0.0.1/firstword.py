f=open("wordlist.txt",'a+',encoding='utf-8')
words=''
with open('formattedfinal.txt','r') as file:
    for line in file:
        if '.' in line:
            a=line.split('.')
            b=a[0].split(' ')
            for word in b:
                if any(char.isdigit() for char in word):
                    continue
                else:
                    words=words+' '+word
            f.write(words+'\n')
            words=''
f.close()
