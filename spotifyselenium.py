# Adds chromedriver binary to path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome()
driver.get("https://open.spotify.com/playlist/7GqS3Cho7pL2umZWTsE3kM")

input("press enter to end script")
