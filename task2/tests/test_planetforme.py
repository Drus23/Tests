from conftest import configurate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = configurate()


def test_title():
    driver.get(url="https://planetfor.me/CP8rb83")
    title = driver.title
    assert title == "Панорамные виды Москвы"


def test_block():
    driver.get(url="https://planetfor.me/CP8rb83")
    element = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div/div/div[2]')
    link_list = element.find_elements(By.TAG_NAME, "a")
    assert len(link_list) == 16