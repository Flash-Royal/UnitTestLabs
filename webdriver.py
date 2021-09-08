import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def test_discord_title():
    chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")

    chrome_driver.get("https://discord.com")
    chrome_driver.maximize_window()

    title = "Discord | Ваше место для общения и отдыха"
    assert title == chrome_driver.title

    sleep(2)
    chrome_driver.close()

def test_discord_click():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")

        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        sleep(2)
        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_login():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()

        sleep(10)
        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()


def test_discord_send_text():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(5)

        chrome_driver.find_element_by_xpath("//a[@aria-label = 'YourFriend (личное сообщение)']").click()
        text = "Привет"
        sleep(2)

        email_text = chrome_driver.find_element_by_xpath("//div[@aria-label='Написать @YourFriend']")
        email_text.send_keys(text)
        email_text.send_keys(Keys.ENTER)
        sleep(2)

        sleep(2)
        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_call_and_off():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(5)

        chrome_driver.find_element_by_xpath("//a[@aria-label='YourFriend (личное сообщение)' or @aria-label= 'не прочитано, YourFriend (личное сообщение)']").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//div[@aria-label='Начать голосовой звонок']").click()
        sleep(5)

        chrome_driver.find_element_by_xpath("//button[@aria-label='Отключиться']").click()
        sleep(2)

        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_email_to_chanell():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(10)

        chrome_driver.find_element_by_xpath("//div[@aria-label = ' YourChat']").click()
        sleep(2)

        text = "Не обращайте внимания, всего лишь бот"
        email_text = chrome_driver.find_element_by_xpath("//div[@aria-label = 'Написать #флудилка📡']")
        email_text.send_keys(text)
        email_text.send_keys(Keys.ENTER)
        sleep(2)

        sleep(2)
        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_call_to_chanell():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()
        
        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()
        
        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(10)

        chrome_driver.find_element_by_xpath("//div[@aria-label = ' YourChat']").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//a[@aria-label='Посольство Башкортостана (голосовой канал)']").click()
        sleep(2)

        sleep(2)
        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_quit_from_account():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(10)

        chrome_driver.find_element_by_xpath("//button[@aria-label='Настройки пользователя']").click()
        sleep(4)

        chrome_driver.find_element_by_xpath("//div[contains(text(), 'Выйти')]").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@class='button-38aScr lookFilled-1Gx00P colorRed-1TFJan sizeMedium-1AC_Sl grow-q77ONN']").click()
        sleep(2)

        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_delete_email_in_chanell():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(10)

        chrome_driver.find_element_by_xpath("//div[@aria-label = ' YourChat']").click()
        sleep(2)

        text = "Не обращайте внимания, всего лишь бот"
        email_text = chrome_driver.find_element_by_xpath("//div[contains(text(), '{0}')]".format(text))

        actions = ActionChains(chrome_driver).move_to_element(email_text)
        actions.perform()

        email = email_text.find_element_by_xpath("..")
        email = email.find_element_by_xpath("..")
        email.find_element_by_xpath(".//div[@aria-label = 'Ещё']").click()

        chrome_driver.find_element_by_xpath("//div[@id = 'message-actions-delete']").click()
        sleep(2)
        chrome_driver.find_element_by_xpath("//div[contains(text(), 'Удалить')]").click()
        sleep(2)

        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()

def test_discord_create_and_delete_server():
    try:
        chrome_driver = webdriver.Chrome(executable_path= "chromedriver.exe")
        chrome_driver.get("https://discord.com")
        chrome_driver.maximize_window()

        chrome_driver.find_element_by_class_name("appButton-2wSXh-").click()

        text = "Your Email"
        email_text = chrome_driver.find_element_by_name("email")
        email_text.send_keys(text)
        sleep(2)
        
        password = "Your Password"
        email_text = chrome_driver.find_element_by_name("password")
        email_text.send_keys(password)
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(10)

        chrome_driver.find_element_by_xpath("//div[@aria-label = 'Добавить сервер']").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@class='container-UC8Ug1']").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//button[@class='container-UC8Ug1']").click()
        sleep(2)

        text = "Test Server"
        text_field = chrome_driver.find_element_by_xpath("//input[@class='inputDefault-_djjkz input-cIJ7To']")
        text_field.send_keys(Keys.CONTROL + "a")
        text_field.send_keys(Keys.DELETE)
        text_field.send_keys(text)
        sleep(2)

        create = chrome_driver.find_element_by_xpath("//div[contains(text(), 'Создать')]")
        create.find_element_by_xpath("..").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//div[@aria-label= ' Test Server']").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//h1[contains(text(), text)]").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//div[contains(text(), 'Настройки сервера')]").click()
        sleep(2)

        chrome_driver.find_element_by_xpath("//div[contains(text(), 'Удалить сервер')]").click()
        sleep(2)

        text_field = chrome_driver.find_element_by_xpath("//input[@id = 'text-entry-confirm']")
        text_field.send_keys(text)
        sleep(2)

        but = chrome_driver.find_element_by_xpath("//div[@class = 'contents-18-Yxp' and contains(text(), 'Удалить сервер')]")
        but.find_element_by_xpath("..").click()
        sleep(4)

        chrome_driver.close()
    except:
        sleep(2)
        chrome_driver.close()
