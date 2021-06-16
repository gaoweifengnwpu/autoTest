from selenium import webdriver

from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome()
browser.maximize_window()
#2.通过浏览器向服务器发送URL请求
browser.get("https://192.73.0.127:3000/login.html")
# sleep(3)
#3.刷新浏览器
login=['secur','secur@123']
#4.设置浏览器的大小
# browser.set_window_size(100,800)
# 安全员登录
browser.find_element_by_xpath("//*[@id='details-button']").click()
browser.find_element_by_xpath("//*[@id='proceed-link']").click()
browser.find_element_by_xpath("//*[@id='name']").send_keys(login[0])
browser.find_element_by_xpath("//*[@id='pwd']").send_keys(login[1])
browser.find_element_by_xpath("//*[@id='login']").click()
