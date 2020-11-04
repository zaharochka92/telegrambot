
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import time
options = Options()
options.add_argument( "--headless" )
# options.add_argument( "--screenshot test.jpg http://google.com/" )
driver = webdriver.Firefox( firefox_options=options )
driver.get('https://yandex.ru/pogoda/moscow/maps/nowcast?via=mmapwb&le_Lightning=1')
time.sleep(7)
#try:
#    driver.find_element_by_css_selector('.button.c_button.s_button').click()
#except:
#    pass
#try:
#    driver.find_element_by_link_text("Accept").click()
#except:
#    pass
time.sleep(7)
driver.save_screenshot('test.png')
#print (driver.title)
#print (driver.current_url)
#print (driver.page_source)
driver.quit()
sys.exit()
