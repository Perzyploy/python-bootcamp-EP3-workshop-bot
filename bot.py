# bot.py

import webbrowser
import time
import pyautogui
import pyperclip
import os


thaichar = [chr(i) for i in range(3585,3676) ] #เรียกคาแรกเตอร์ภาษาไทยจากแอสกีโค้ด

def isThai(word):
	for w in word:
		if w in thaichar:
			print('Thai')
			return True  # ถ้าเข้าเงื่อนไข โปรแกรมจะจบการรันที่บรรทัดสุดท้ายตรง return True ทันที ไม่อ่านบรรทัดล่างต่อ
	print('Other language')
	return False 


def Search(keyword = 'thailand'):

	url = 'http://www.google.com'
	webbrowser.open(url)
	time.sleep(2) # ให้หน่วงเวลา 2 วิ รอให้เปิดเวบขึ้นมาก่อน ค่อยพิมพ์

	if isThai(keyword): #ถ้า keyword ของเราเป็นภาษาไทย เช็คจากฟังก์ชัน isThai
		pyperclip.copy(keyword) # ให้ทำการ copy keyword เก็บเอาไว้ใน clipboard
		time.sleep(0.5) # ตั้งหน่วงเวลาให้มันมีเวลา copy นิดนึง
		pyautogui.hotkey('ctrl','v') # ใช้ hotkey จากคีย์บอร์ดให้มันวางข้อความจากคลิปบอร์ด แบบคำสั่ง paste
	else:
		pyautogui.write(keyword,interval = 0.25) # interval คือให้หน่วยเวลาในการพิมพ์ื
		# ถ้าไม่ใช่ภาษาไทย ให้พิมพ์ keyword ลงไปได้เลย


	pyautogui.press('enter')
	time.sleep(1)


	# กรณีจะให้ภาพที่แคปเจอร์ได้เก็บไว้ในโฟลเดอร์แยก
	#path =r'C:\Users\perzyploy\Documents\python\Bootcamp\EP3\screen capture'
	#filename =os.path.join(path,'{}.jpg'.format(keyword))



	pyautogui.screenshot('{}.jpg'.format(keyword)) # สั่งให้แคปหน้าจอ เซฟเป็นไฟล์ jpeg
	time.sleep(1)

	pyautogui.hotkey('ctrl','w') # สั่งให้ใช้คีย์บอร์ดกดปิดเว็บ



wordlist = ['thailand','กรุงเทพ']
for s in wordlist:
	Search(s)