from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

import os
import requests
from PIL import Image
import shutil
import urllib
import csv

def _options():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-gpu') if os.name == 'nt' else None # Windows workaround
    options.add_argument("--verbose")
    return options

browser = webdriver.Chrome()
browser.set_window_size(1024, 600)
browser.maximize_window()

browser.implicitly_wait(1)
# browser.minimize_window()
captions = []
images = []

def append_to_csv(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

with open('links.txt', 'r') as file:
    c = 0
    lines = file.readlines()
    for line in lines:
        # if c < 50:
        browser.get(line)
        try:
            # Try to find an element with the current class name
            # img_elem = browser.find_element(By.CSS_SELECTOR, ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
            
            img_elem = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")) #This is a dummy element
            )
        
            sleep(1)
            url = img_elem.get_attribute("src")
            response = requests.get(url, stream=True)
            file_path = './images/' + str(c) + '.png'
            with open(file_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

            del response
            # caption_elem = browser.find_element(By.CSS_SELECTOR, "._aacl._aaco._aacu._aacx._aad7._aade")
            caption_elem = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._aacl._aaco._aacu._aacx._aad7._aade")) #This is a dummy element
            )
            sleep(1)
            caption = caption_elem.text
            caption = caption.replace('\n', '')
            captions.append(caption)
            # Perform the procedure you want to execute if the class exists
            # For example, you can click on the element or interact with it here
            # element.click()
            c += 1
        except NoSuchElementException:
            print("skipping")

        

append_to_csv('captions.csv', captions)



# Example usage

# Get text of div element
# div_text = elem.text
# print(div_text)


# def read_and_print_lines(filename):
#     c = 0
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if c < 10:
#                     browser.get(line)
                    
#                     try:
#                         elem = WebDriverWait(browser, 10).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, ".x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")) #This is a dummy element
#                     )
#                         print(elem)
#                     finally:
#                         print("element not found")

#                     # captions = browser.find_element(By.CSS_SELECTOR, "._aacl._aaco._aacu._aacx._aad7._aade").text
#                     # photo_elem = browser.find_element(By.CSS_SELECTOR, "._aagv [src]")
#                     # photo_link = photo_elem.get_attribute('src') 

#                     # print(captions)
#                     # print(photo_link)
                    
#                     # img_url = photo_link
#                     # img = Image.open(requests.get(img_url, stream = True).raw)

                
#                     # img.save('./images' + str(c) + '.png')
#                     c += 1

#             #print("File reading and printing completed.")
#     except Exception as e:
#         print("An error occurred:", e)

# Replace 'example.txt' with the actual filename you want to read

captions = []
images = []

# file_name = 'links.txt'
# read_and_print_lines(file_name)



# elems = browser.find_elements(By.CSS_SELECTOR, "._aabd._aa8k._al3l [href]")
# links = [elem.get_attribute('href') for elem in elems]
    