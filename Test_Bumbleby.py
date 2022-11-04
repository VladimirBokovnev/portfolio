import time


import select
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Вход на сайт Бамблби
s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")

#Ввод логина и пароля
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("vladimirbokovnev@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").click
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)

#Переход в форму Паспорт, заполнение ФИО
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.CSS_SELECTOR, "#surname").send_keys("Боковнев")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Владимир")
driver.find_element(By.CSS_SELECTOR, "#patronymic").clear()
driver.find_element(By.CSS_SELECTOR, "#patronymic").send_keys("Александрович")

#Выбор даты в датапикере Дата рождения
driver.find_element(By.NAME, "date").click()
date= "14 май 2004"
month_year= "май 2004"
for c in range(12):
    month=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/span").text
    if month== month_year:
        days=driver.find_elements(By.CSS_SELECTOR, ".mx-date-row:nth-child(2) > .cell:nth-child(3) > div")
        for i in days:
            if i.get_attribute("title")==("2004-05-14"):
                i.click()
                time.sleep(1)
                break
        break
    else:
        arrow_button=driver.find_element(By.CSS_SELECTOR, ".mx-btn-icon-left")
        arrow_button.click()
        time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td[5]").click()

#Заполнение серии паспорта
driver.find_element(By.CSS_SELECTOR, "#passportSeries").clear()
driver.find_element(By.CSS_SELECTOR, "#passportSeries").send_keys("1234")

#Заполнение номера паспорта
driver.find_element(By.CSS_SELECTOR, "#passportNumber").clear()
driver.find_element(By.CSS_SELECTOR, "#passportNumber").send_keys("567890")

#Выбор даты в датапикере Дата выдачи. Применяем обычное заполнение для проверки функции простого ввода
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys("14.05.2022")
#driver.find_element(By.ID, "dateOfIssue").click()
#date1= "14 май 2022"
#month_year1= "май 2022"
#for c in range(12):
#    month1=driver.find_element(By.CSS_SELECTOR, ".mx-calendar-header-label").text
#    if month1== month_year1:
#        days1=driver.find_elements(By.CSS_SELECTOR, ".mx-date-row:nth-child(3) > .cell:nth-child(3) > div")
#        for k in days1:
#            if k.get_attribute("title")==("2022-05-14"):
#                k.click()
#                time.sleep(2)
#                break
#        break
#    else:
#        arrow_button1=driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/button[2]")
#        arrow_button1.click()
#        time.sleep(2)
#driver.find_element(By.CSS_SELECTOR, "tr.mx-date-row:nth-child(3) > td:nth-child(6)").click()

#Скроллинг вниз
driver.execute_script("window.scrollTo(0, 450)")
time.sleep(1)

#Заполнение кода подразделения
driver.find_element(By.CSS_SELECTOR, "#code").click()
driver.find_element(By.CSS_SELECTOR, "#code").clear()
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("123456")

#Заполнение СНИЛС
driver.find_element(By.CSS_SELECTOR, "#cardId").clear()
driver.find_element(By.CSS_SELECTOR, "#cardId").send_keys("12345678900")
driver.find_element(By.CSS_SELECTOR, "#issued").send_keys("ОВД")

#Заполнение номера телефона
driver.find_element(By.CSS_SELECTOR, "#phone").click()
driver.find_element(By.CSS_SELECTOR, "#phone").clear()
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("9008000000")

#Прикрепление документов
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:/Users/Honor/Downloads/Манул/Manul2.jpg")
time.sleep(1)

#Заполнение поля Адрес и отправка данных на проверку
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Ростов-на-Дону, Буденновский пр-кт")
time.sleep(1)
adress=driver.find_element(By.CSS_SELECTOR,".vue-dadata__input")
adress.send_keys(Keys.DOWN)
adress.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)").click()

#Подтверждение паспорта через админку
driver.get("https://adminqa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.ID, "admin_email").send_keys("moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
driver.find_element(By.NAME, "commit").click()
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=2200&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&order=id_desc")
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)

#Идем обратно на сайт и разлогиниваемся
time.sleep(3)
driver.get("https://qa.neapro.site/cabinet/documents/")
time.sleep(3)
driver.find_element(By.XPATH, ".//*[@id='__layout']/div/div[1]/div/div[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[1]/div/div").click()
time.sleep(3)

#Возвращаемся в админку и удаляем данные паспорта для подготовки к повторному тесту
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=2200&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&order=id_desc")
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[7]/div/a[3]").click()
driver.switch_to.alert.accept()
