from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from pyvirtualdisplay import Display
import pyperclip
from selenium.webdriver import ActionChains
# from bs4 import BeautifulSoup
import re
import random

# pip install pyperclip
file = open("numbers.txt", "r")
msg = open("msg.txt", "r",encoding="utf8")
imgpath = open("imgpath.txt", "r",encoding="utf8")
Lines = file.readlines()
msgline = msg.readlines()
imglinepath = imgpath.readlines()
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/nihal/AppData/Local/Google/Chrome/User Data")
driver=webdriver.Chrome(options=options)
time.sleep(1)
message_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
attach_button_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
send_button_path = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'
for line in range(0,len(Lines)):
    number = (Lines[line].strip()).replace(" ","")
    number91 = 0
    if len(number)==10:
        number91 = '+91' + number
    else:
        number91 = number
    time.sleep(5)
    url="https://web.whatsapp.com/send?phone="+str(number91)+"&text="
    try:
        driver.get(url)
    except:
        continue
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "lhggkp7q")))
    except:
        continue
    for line in range(0,len(msgline)):
        message = msgline[line].strip()
        try:
            message_box=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,message_box_path)))
        except:
            print("except")
            break
        if line == 0:
            message_box.send_keys(Keys.SHIFT + Keys.ENTER)
        # print(message_box.send_keys(message[0][0]))
        pyperclip.copy(message)
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        # message_box.send_keys(message)
        message_box.send_keys(Keys.SHIFT)
        # message_box.send_keys(end='')
        message_box.send_keys(Keys.SHIFT + Keys.ENTER)

        if len(msgline)-1 == line:
            if imglinepath:
                print(number91)
                attachbutt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, attach_button_path)))
                attachbutt.click()
                time.sleep(3)
                image_box=driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(imglinepath)
                send_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, send_button_path)))
                random_time_stop = random.randint(1, 10)
                time.sleep(random_time_stop)
                send_button.click()
            else:
                print(number91)
                random_time_stop = random.randint(1, 10)
                time.sleep(random_time_stop)
                message_box.send_keys(Keys.ENTER)
time.sleep(4)
driver.close()