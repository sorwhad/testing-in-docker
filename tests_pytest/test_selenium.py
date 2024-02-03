from selenium import webdriver
import time

def test_selenium():
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities={
            'browserName': 'chrome',
            'javascriptEnabled': True
        }
    )
    driver.get('https://ya.ru')
    time.sleep(10)
    assert driver.current_url == 'https://ya.ru'
    time.sleep(100)
    driver.quit()