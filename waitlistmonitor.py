# Import requests (to download the page)
import requests
# Import Time (to add a delay between the times the scape runs)
import time
from selenium.webdriver import Chrome
from pygame import mixer


webdriver = "/Applications/chromedriver"
driver = Chrome(webdriver)
while True:
    driver.get("https://ssb.vcccd.edu/prod/pw_pub_sched.P_Simple_SEARCH?term=202005")
    eng = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select/option[31]")
    eng.click()

    alll = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select/option[1]")
    alll.click()

    sub = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/form/table/tbody/tr[4]/td/center/input[1]")
    sub.click()

    sumita = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[80]/td[1]/font")
    color = sumita.value_of_css_property("color")
    kim = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[82]/td[1]/font")
    color2 = kim.value_of_css_property("color")
    kim2 = driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[83]/td[1]/font")
    color3 = kim2.value_of_css_property("color")

    red = 'rgba(255, 0, 0, 1)'

    if (color != red) or (color2 != red) or (color3 != red):
        mixer.init()
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        if (color != red):
            print("56651")
        elif (color2 != red):
            print("56677")
        else:
            print("57612")
        driver.save_screenshot("screenshot.png")
        break
    else:
        time.sleep(10)
    