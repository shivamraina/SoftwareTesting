import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/srain/Downloads/chromedriver.exe')

def dropdown():
    driver.get('https://www.amazon.in')
    searchbar = driver.find_element_by_id("twotabsearchtextbox")
    for char in '4K UHD TV':
        searchbar.send_keys(char)
        time.sleep(0.3)
    time.sleep(1)
    el = driver.find_elements_by_class_name("s-suggestion")
    el[2].click()

def dynamicxpath():
    productXpath = "//div[@class='s-main-slot s-result-list s-search-results sg-row']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"
    product = driver.find_element_by_xpath(productXpath)
		
    product.click()

def iterating_lists():
    chwd = driver.window_handles
    driver.switch_to.window(chwd[1])
    
    productXpath = "//div[@id='feature-bullets']//li"
    products = driver.find_elements_by_xpath(productXpath)
    
    for p in products:
        print(p.text)

def javascript():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def amazon():
    dropdown()    
    dynamicxpath()
    iterating_lists()
    javascript()

amazon()