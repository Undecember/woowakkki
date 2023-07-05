username = input('Enter username : ').replace('\n', '')
password = input('Enter password : ').replace('\n', '')

import os, random, time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=options)
browser.set_window_size(1920, 1080)
browser.get('https://nid.naver.com/nidlogin.login')
browser.find_element(By.NAME, 'id').send_keys(username)
browser.find_element(By.NAME, 'pw').send_keys(password)
browser.find_element(By.ID, 'log.login').click()
time.sleep(2)
while True:
    browser.save_screenshot('cim.png')
    cap = input('captcha image saved in cim.png. Enter the answer : ').replace('\n', '')
    if cap == 'done': break
    browser.find_element(By.NAME, 'pw').send_keys(password)
    browser.find_element(By.ID, 'captcha').send_keys(cap)
    browser.find_element(By.ID, 'log.login').click()
    time.sleep(2)
browser.find_element(By.ID, 'new.dontsave').click()
time.sleep(2)
browser.get('https://cafe.naver.com/steamindiegame')
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
