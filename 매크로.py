from selenium import webdriver
chrome_path = 'C:\Wujin_py\chromedriver'
url = "https://www.naver.com/"
browser = webdriver.Chrome(chrome_path)
browser.get(url)