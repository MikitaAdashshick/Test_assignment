from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome()
driver.get('https://netpeak.ua/')
wait = WebDriverWait(driver, 10)
assert len(driver.window_handles) == 1
original_window = driver.current_window_handle
dropdownmenu = driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]').click()
link1 = driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[3]/div/div[2]/ul[1]/li[3]/div/a')
driver.execute_script("arguments[0].click();", link1)
link2 = driver.find_element_by_xpath('//*[@id="rec278626926"]/div/div/div[10]/a').click()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
assert "Работа в Netpeak: обращение руководителя, видео и презентация о карьере в Нетпик" in driver.title
value = driver.find_element_by_xpath ('/html/body/div[5]/div/div/div[2]/div/a').is_enabled()
driver.close()
driver.switch_to.window(original_window)
link3 = driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[2]/ul/li[1]/a').click()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
link4 = driver.find_element_by_id('login').send_keys('kikhk')
link5 = driver.find_element_by_id('password').send_keys('lolol')
value != driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button').is_enabled()
chckbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/md-checkbox/div[1]').click()
link6 = driver.find_element_by_xpath( '//*[@id="loginForm"]/div[5]/button').click()
toast = driver.find_elements_by_xpath('/html/body/md-toast/div/span')
s = len(toast)
if(s>0):
      print("Element exist")
else:
   print("Element does not exist")
login_color = Color.from_string(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/md-input-container/label').value_of_css_property('color')) 
password_color =  Color.from_string(driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/md-input-container/label').value_of_css_property('color')) 
assert login_color.rgb == 'rgb(221, 44, 0)'
assert password_color.rgb == 'rgb(221, 44, 0)'
driver.quit()