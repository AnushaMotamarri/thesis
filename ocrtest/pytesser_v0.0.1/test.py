from PIL import Image
import pytesseract
import cv2
f=open("formatted.txt",'a+',encoding='utf-8')
for i in range(160,161):
    print(i)
    page='TribhashaNighantuvuTeluguEnglishHindi-free_KinigeDotCom-'+str(i)+'.jpg'
    img=cv2.imread('/home/anu/Documents/thesis/ocrtest/Dictionary/'+page)
    tex=pytesseract.image_to_string(Image.open('/home/anu/Documents/thesis/ocrtest/Dictionary/'+page),lang='tel')
    f.write(pytesseract.image_to_string(Image.open('/home/anu/Documents/thesis/ocrtest/Dictionary/'+page),lang='tel'))
f.close()
