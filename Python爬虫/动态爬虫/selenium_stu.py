from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get("https://blog.gaozhe.top/")
    driver.find_elements_by_id("kw")
    driver.save_screenshot("1.png")
    driver.close()


if __name__ == '__main__':
    main()