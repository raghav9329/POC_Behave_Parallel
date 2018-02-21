from behave import *
from selenium import webdriver
@given(u"Open browser visit application")
def step_impl(context):
    context.browser=webdriver.Chrome()
    context.browser.get("https://www.facebook.com")
    context.browser.implicitly_wait(30)
@when(u"the page is loaded fill the invalid login id and password")
def step_impl(context):
    login=context.browser.find_element_by_id("email")
    login.send_keys("24jdsdsd")
    password=context.browser.find_element_by_id("pass")
    password.send_keys("123456789")
@when(u"the page is loaded fill the  login id and blank password")
def step_impl(context):
    login=context.browser.find_element_by_id("email")
    login.send_keys("raghav9329@gmail.com")
    password=context.browser.find_element_by_id("pass")
    password.send_keys("")
@when(u"the page is loaded check that it is loaded with secure certificates or not")
def step_impl(context):
    if(context.browser.title=="untrusted Connection"):
        print("This certificate is incorrect")
@when(u"the page is loaded fill the  login id and incorrect password")
def step_impl(context):
    login=context.browser.find_element_by_id("email")
    login.send_keys("raghav9329@gmail.com")
    password=context.browser.find_element_by_id("pass")
    password.send_keys("1234567dad89")
@then(u"click on login button and verify the page")
def step_impl(context):
    sub=context.browser.find_element_by_xpath("//input[@value='Log In']")
    sub.click()
    assert context.browser.title!="facebook"
    context.browser.quit
