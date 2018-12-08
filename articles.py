import requests
from bs4 import BeautifulSoup
import os
for k in range(4842,30000):
    ans=''
    url='http://www.eenadu.net/magazines/sunday-magazine/sunday-magazineinner.aspx?catfullstory='+str(k)
    try:
        resp=requests.get(url)

        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("section",{"class":"two-col-left-block box-shadow telugu_uni_body fullstory1"})
            for para in l.findAll("span"):
                if(para.text not in ans):
                    ans+=para.text
            if(ans!=''):
                filename='01'+'0'*(5-len(str(k)))+str(k)+'.txt'
                f=open(filename,'w',encoding='utf-8')
                print (filename)
                f.write(ans)
    except:
        print("Network error!")
        f1=open("missed.txt",'a+',encoding='utf-8')
        f1.write(str(k))
