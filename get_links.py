from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')

sleep(1)

username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("syed_ayan.ali")
password_input.send_keys("instFooBar123!")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

sleep(5)

driver.get("https://www.instagram.com/natgeo/")

sleep (5)

def append_list_to_file(lst, file_path):
    with open(file_path, 'a') as file:
        for element in lst:
            file.write(str(element) + '\n')

def remove_duplicate_lines(file_path):
    lines_seen = set()  # Set to store unique lines
    output_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            if line not in lines_seen:
                output_lines.append(line)
                lines_seen.add(line)

    with open(file_path, 'w') as file:
        file.writelines(output_lines)

def options():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-gpu') if os.name == 'nt' else None # Windows workaround
    options.add_argument("--verbose")
    return options

all_links = []

for i in range(5000):
    div = driver.find_elements(By.CSS_SELECTOR, '._aabd._aa8k._al3l')
    for d in div:
        links = d.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        # print(links)
        all_links.append(links)

    remove_duplicate_lines('links.txt')
    append_list_to_file(all_links, 'links.txt')   
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    
    sleep(2)
    print("""
          
          NEXT LOOP
          
          """)
    all_links = []   
    