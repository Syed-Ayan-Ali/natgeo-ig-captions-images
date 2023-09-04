from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()

browser.implicitly_wait(1)

browser.get('https://www.instagram.com/')

sleep(1)

username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("syed_ayan.ali")
password_input.send_keys("instFooBar123!")

login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

sleep(3)

browser.get('https://www.instagram.com/natgeo')

sleep(2)
links = []
all_links = []

for i in range(20):
    if len(links) < 42:
        elems = browser.find_elements(By.CSS_SELECTOR, "._aabd._aa8k._al3l [href]")
        for elem in elems:
            links = elem.get_attribute('href')
            all_links.append(links)
    else:
        links = []

    print(all_links)
    sleep(2)
    html = browser.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    sleep(2)


def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List elements written to the file successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Replace 'list_data.txt' with the actual filename and provide the list of data
file_name = 'links.txt'
data_to_write = all_links

write_list_to_file(file_name, data_to_write)

def remove_duplicates(file_path):
    lines_seen = set()  # Set to store unique lines
    output_lines = []

    # Read the input file line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line not in lines_seen:
                lines_seen.add(line)
                output_lines.append(line)

    # Write the unique lines to a new file
    with open(file_path, 'w') as file:
        file.write('\n'.join(output_lines))

# Specify the path to your text file
file_path = 'links.txt'

# Call the function to remove duplicates
remove_duplicates(file_path)

sleep(1)