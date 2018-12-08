import requests
from bs4 import BeautifulSoup
import os
url='http://www.eenadu.net/special-pages/aalayaalu/aalayaalu-more.aspx'
resp=requests.get(url)
if resp.status_code==200:
    soup=BeautifulSoup(resp.text,'html.parser')
    anchors=soup.findAll("a")
    for link in anchors:
        l=link.get("href")
        if('aalayaalu-' in l):
            num=l.split('=')[1]
            #print (num)
            try:
                cont=''
                resp1=requests.get('http://www.eenadu.net/special-pages/aalayaalu/'+l.strip())
                soup1=BeautifulSoup(resp1.text,'html.parser')
                section=soup1.find("section",{"class":"two-col-left-block box-shadow telugu_uni_body offset-b fullstory"})
                paras=section.findAll("p")
                for t in paras:
                    cont+=t.text
                if (cont!=''):
                    filename='02'+'0'*(5-len(num))+num+'.txt'
                    f=open(filename,'w',encoding='utf-8')
                    f.write(cont)
                    print (filename)

            except:
                print("Network Error!")
