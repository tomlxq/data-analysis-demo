from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import csv
import time
driver = webdriver.Chrome("D:/tools/chromedriver.exe")

driver.get("https://www.baidu.com/")