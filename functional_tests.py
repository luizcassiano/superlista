from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\Others\chromedriver_win32\chromedriver.exe")
browser.get("http://localhost:8000")

assert 'worked successfully' in browser.title