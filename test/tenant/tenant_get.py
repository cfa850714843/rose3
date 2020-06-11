# coding: utf-8
from selenium.webdriver import *

chrome = Chrome()


def fun1():
    url = 'http://test.aps.zetyun.cn/user/login'
    chrome.get(url)
    chrome.find_element_by_id("loginname").send_keys("bone")
    chrome.find_element_by_id("password").send_keys("123456")
    chrome.find_element_by_class_name("button___d8u5l").click()

    chrome.find_element_by_class_name("ant-col").click()

    chrome.close()
    pass


if __name__ == '__main__':
    fun1()
