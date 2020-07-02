# This file will have two functions.
# Functions
# 1. test_scores_service(app_url) – Will test our web service.
# Will get the application URL as an input, open a browser to that URL, select the score
# element in our web page, check that it is a number between 0 to 1000 and return a
# boolean value if it’s true or not.
# 2. main_function() –
# Will call our tests function.
# The main function will return -1 as an OS exit code if the tests failed and 0 if it passed.

import sys, os, subprocess
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\\Studies\\DevOps\\chromedriver.exe")



def test_scores_service(app_url):
    driver.get(app_url)
    score = driver.find_element_by_id("score").text
    if int(score) <= 1000 and int(score) >= 0:
        driver.quit()
        return True
    else:
        driver.quit()
        return False


def main_function():
    host_ip = os.popen("docker-machine ip").read()
    url='http://'+str(host_ip[0:14])+':8777'
    result = test_scores_service(url)
    if result == True:
        return sys.exit(0)
    else:
        return sys.exit(-1)

if __name__ == '__main__':
    main_function()

