from selenium import webdriver
import time

def main():
    web = webdriver.Chrome()
    web.get('https://zzzscore.com/1to50/en/')
    time.sleep(5)
    for i in range(99, 0, -1):
        select_element =  web.find_element('xpath', '//*[@style="z-index:'+str(i)+'"]')
        select_element.click()
        time.sleep(0.2)

main()

    
    
    
