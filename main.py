from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time


driver = webdriver.Firefox()

insta = 'https://www.instagram.com/'
Instagram = driver.get(insta)


user_id = 'g.keshav_911'
user_password = 'keshav1234k@'
file = '/home/keshav/Downloads/black.jpeg'
driver.set_page_load_timeout(30)

def login(user_id, user_password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
    username = driver.find_element(By.NAME, 'username')
    username.clear()
    username.send_keys(user_id)

    password = driver.find_element(By.NAME, 'password')
    password.clear()
    password.send_keys(user_password)

    password.send_keys(Keys.RETURN)


def upload_photo(path):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.x1iyjqo2:nth-child(2) > div:nth-child(7)')))
   
    goto_post = driver.find_element(By.CSS_SELECTOR, 'div.x1iyjqo2:nth-child(2) > div:nth-child(7)')
    goto_post.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.x1iorvi4 > button:nth-child(1)')))

    button = driver.find_element(By.CSS_SELECTOR, '.x1iorvi4 > button:nth-child(1)')
    button.click()

    #open address bar in the file browser window
    pyautogui.hotkey('ctrl','l')
    #enter the path where the file is present
    pyautogui.write(path)
    #press enter to navigate to the folder
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.press('enter')

    for _ in range(3):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                        ((By.CSS_SELECTOR, '.xyamay9 > div:nth-child(1)')))
    
        next_button = driver.find_element(By.CSS_SELECTOR, '.xyamay9 > div:nth-child(1)')
        next_button.click()
    
    # if caption is not None:
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable
    #                                 ((By.CSS_SELECTOR, '.x1hnll1o')))
    # parent_cption = driver.find_element(By.CSS_SELECTOR, '._ac2p > div:nth-child(2) > div:nth-child(1)')

    # cption = parent_cption.find_element(By.CSS_SELECTOR, '.x6s0dn4 [aria-label="Write a caption..."]')

    # # cption = parent_cption.find_element(By.XPATH, '/div')
    # cption.click()                                   
    # time.sleep(5)

    # cption.send_keys('it is my auto generated post caption')
    # # next_button = driver.find_element(By.CSS_SELECTOR, '.xyamay9 > div:nth-child(1)')
    # # next_button.click()
    time.sleep(5)

    close = driver.find_element(By.CSS_SELECTOR, '.x160vmok > div:nth-child(1) > div:nth-child(1)')
    close.click()

login(user_id=user_id, user_password=user_password)
# for _ in range(3):
#     upload_photo(path=file)

time.sleep(100)
driver.close()
driver.quit()










