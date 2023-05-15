"""
This scripts reads the file input.txt which contains some lines to be translated.
'language' is the variable of the translation language, now is set to German.

"""
import time
import clipboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# If a clickable element is intercepted
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

# language of translation
language = 'de' # This corresponds to german

# URL for translation
url = 'https://www.deepl.com/translator'
driver.get(url)

# create an ActionChains object to move the mouse to the button later
actions = ActionChains(driver)

# Closing cookies
driver.find_element(By.CSS_SELECTOR,'.dl_cookieBanner--buttonClose').click()

time.sleep(10)

WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="translator-target-lang-btn"]')) )
lang_bttn = driver.find_element(By.CSS_SELECTOR,'[data-testid="translator-target-lang-btn"]')
actions.move_to_element(lang_bttn)    
actions.click(lang_bttn).perform() 

WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-testid="translator-lang-option-{language}"]')) )
lang_bttn2 = driver.find_element(By.CSS_SELECTOR,f'[data-testid="translator-lang-option-{language}"]')
actions.move_to_element(lang_bttn2)    
actions.click(lang_bttn2).perform() 
#driver.find_element(By.CSS_SELECTOR, '[data-testid="translator-lang-option-de"]').click()

with open('translation.txt','a',encoding='utf-8') as f_translation:
    with open('input.txt','r') as f_input:    
        lines = f_input.readlines()
        for line in lines:
            # Writing text in the input field
            input_text_area = driver.find_element(By.CSS_SELECTOR, '[data-testid="translator-source-input"]')
            input_text_area.send_keys(line)

            # Copy to clipboard 
            clipboard_content =""
            while len(clipboard_content.split()) < len(line.split())/2.0:
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="translator-target-toolbar-copy"]')) )                        
                clipboard_bttn = driver.find_element(By.CSS_SELECTOR, '[data-testid="translator-target-toolbar-copy"]')
                actions.move_to_element(clipboard_bttn)    
                actions.click(clipboard_bttn).perform()                             
                clipboard_content = clipboard.paste()               
            
            # Save to a file 
            print(clipboard_content)
            f_translation.write(clipboard_content.strip()+'\n')

            # Clear the input field
            input_text_area.send_keys(Keys.CONTROL, 'a')  # Select all text
            input_text_area.send_keys(Keys.BACKSPACE)        

#driver.quit()
driver.close()