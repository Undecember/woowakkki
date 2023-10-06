username = input('Enter username : ').replace('\n', '')
password = input('Enter password : ').replace('\n', '')

import os, random, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

service = Service('./chromedriver')
browser = webdriver.Chrome(service = service, options = options)
browser.implicitly_wait(0)
browser.set_window_size(1920, 1080)

browser.get('https://nid.naver.com/nidlogin.login')
browser.find_element(By.ID, 'qrcode').click()
browser.save_screenshot('cim.png')
input('Press enter after done : ')
time.sleep(5)
while True:
    while True:
        post_number = random.randint(10000000, 11900000)
        post_url = f'https://cafe.naver.com/steamindiegame/{post_number}'
        print(f'opening post number {post_number}...')
        browser.get(post_url)
        time.sleep(5)
        try:
            browser.save_screenshot('cim.png')
            print(f'opened post saved in cim.png')
            break
        except:
            print(f'failed opening. retrying...')
            continue
    print(f'sleep...')
    time.sleep(30 * 60 + 5)
