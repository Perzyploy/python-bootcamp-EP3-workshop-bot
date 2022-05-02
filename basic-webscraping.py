# basic-webscraping.py

from urllib.request import urlopen as req # as req คือการตั้งคำสั้นๆ
from bs4 import BeautifulSoup as soup


def StockPrice(CODE='PTT'): 
	url = f'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={CODE}&ssoPageId=10&selectPage=2'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')

	result = data.find_all('div',{'class':'col-xs-6'})
	#print(result[3].text.replace('\n','=')) # เปลี่ยนตัวอักษร \n ให้เป็น = .replace เป็นคำสั่งสำหรับใช้แทนที่คำ
	# อาจใช้ .strip แทนก็ได้ อันนี้เอาไว้ตัดคำด้านหน้ากับด้านหลัง

	title = result[0].text
	price = float(result[2].text)
	change = result[3].text.replace('\n','')
	change = change.replace('\r','').replace(' ','').replace('\t','')
	change = float(change[11:])
	pchange = result[4].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	pchange = pchange[12:-1] # ตัดคำว่า % เปลี่ยนแปลงและ % ด้านหลังออกไป


	print('stock:{} Price:{} Change:{} %Change: {}'.format(title,price,change,pchange))
	return(title,price,change,pchange) #ต้องมีการ return ค่าด้วย เพราะเราจะเอาฟังก์ชันนี้มาใช้งานในหุ้นตัวอื่นๆต่อ คือจะเรียกใช้ฟังก์ชันนี้ซ้ำได้ ถ้าไม่ใส่จะใช้งานได้แค่ครั้งเดียว

StockPrice('KBANK')
StockPrice('SCB')
StockPrice('PTT')


#คำนวณราคาหุ้นที่มี
kbank = StockPrice('KBANK')
print(kbank[1]*1000) # มี 1000 หุ้น เอามาคูณกับค่าที่ดินเด็กที่ 1 จะคำนวณมูลค่าหุ้นที่มีออกมา
