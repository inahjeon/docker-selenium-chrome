import os

from selenium import webdriver


def get_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    chrome_driver = webdriver.Chrome('chromedriver', options=chrome_options)

    return chrome_driver


driver = get_chrome_driver()
query = os.environ.get('QUERY', 'selenium')
url = f'https://www.google.com/search?q={query}'
driver.get(url)
driver.implicitly_wait(1)

search_result = driver.find_elements_by_class_name('srg')
if search_result:
    titles = search_result[0].find_elements_by_tag_name('h3')
    with open(f'./output/result-{query}.txt', 'w') as f:
        for title in titles:
            print(title.text)
            f.write(title.text + '\n')

driver.quit()
