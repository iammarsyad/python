Author : Mukliss

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time

# chrome_options = Options()
# chrome_options.headless = True
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()

driver.get('https://data.covid19.go.id/public/index.html')
time.sleep(5.0)

# print(driver.page_source)

konfir = driver.find_element_by_css_selector('.count-konfirmasi.init_count_loading')
kasus_aktif = driver.find_element_by_css_selector('.count-rawat.init_count_loading')
sembuh = driver.find_element_by_css_selector('.count-sembuh.init_count_loading')
mati = driver.find_element_by_css_selector('.count-meninggal.init_count_loading')
print(konfir.text, kasus_aktif.text, sembuh.text, mati.text)

driver.quit()
