from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    # авторизуемся
    browser = webdriver.Chrome(options=options)
    browser.get("https://usnpint.pointclickcare.com/")

    login = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    login.send_keys("cybxlabs.uiaccess")

    password = browser.find_element(By.CSS_SELECTOR, "[type='password']")
    password.send_keys("P@$$w0rd1k")
    button = browser.find_element(By.CSS_SELECTOR, "#id-submit")
    button.click()


    #переходим к Admin --> New Resident
    AdministrationBox = browser.find_element(By.CSS_SELECTOR, "#QTF_AdminTab .arrowDrop")
    action1 = ActionChains(browser)
    action1.move_to_element(AdministrationBox).perform()
    NewResident = browser.find_element(By.XPATH, "//li[@id='QTF_AdminTab'] //a[contains(text(), 'New Resident')]").click()
    time.sleep(2)



    #заполняем краткие сведения
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[tabindex='1']").send_keys("AutoTest")
    surname = browser.find_element(By.CSS_SELECTOR, "input[tabindex = '2']").send_keys("First1")
    dateOfBirth = browser.find_element(By.CSS_SELECTOR, ".pccDateField").send_keys("12/17/2003")
    gender = Select(browser.find_element(By.ID, "idESOLgender"))
    gender.select_by_index("1")
    social_Security = browser.find_element(By.ID, "idESOLssn").send_keys("845-33-7760")
    button = browser.find_element(By.CSS_SELECTOR, "[value = 'Search']").click()



    #окно с наличием совпадений
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    button = browser.find_element(By.CSS_SELECTOR, "[value = Continue]").click()

    # заполняем карточку пациента
    new_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    social_Security = browser.find_element(By.CSS_SELECTOR, "[aria-labelledby='Social_Security_#-AriaId']").send_keys("845-33-0007")
    button = browser.find_element(By.CSS_SELECTOR, "[onclick='saveClient();']").click()
    time.sleep(2)
    browser.refresh()



    # переходим  census/rate
    time.sleep(2)
    administrationBox = browser.find_element(By.CSS_SELECTOR, "#QTF_AdminTab > a")
    action = ActionChains(browser)
    action.move_to_element(administrationBox).perform()
    time.sleep(2)
    administrationBox_click = browser.find_element(By.CSS_SELECTOR, "#QTF_AdminTab > a").click()
    census_rates = browser.find_element(By.XPATH, "//a[contains(text(), 'Census / Rates')]").click()
    new_census = browser.find_element(By.CSS_SELECTOR, "[title='New Census: CTRL-SHIFT-N']").click()


    # оформляем первичный прием
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    calendar = browser.find_element(By.CSS_SELECTOR, ".ui-datepicker-trigger").click()
    current_day = browser.find_element(By.CSS_SELECTOR, ".ui-datepicker-today .ui-state-default").click()
    hour = Select(browser.find_element(By.NAME, "hour")).select_by_value("1")
    min = Select(browser.find_element(By.NAME, "min")).select_by_value("0")
    action = Select(browser.find_element(By.NAME, "action_code_id")).select_by_value("1")
    time.sleep(3)
    payer = Select(browser.find_element(By.NAME, "primary_payer_id")).select_by_value("209")
    time.sleep(2)
    to_from_type = Select(browser.find_element(By.NAME, "adt_tofrom_id")).select_by_value("9086")
    time.sleep(2)
    to_from_location = Select(browser.find_element(By.NAME, "adt_tofrom_loc_id")).select_by_value("-1312")
    time.sleep(10)
    button_save = browser.find_element(By.CSS_SELECTOR, "[title='Save: CTRL-SHIFT-S']").click()
    time.sleep(10)

    # подтвреждаем
    alert = browser.switch_to.alert
    alert.accept()

    # еще раз сохраняем
    button1_save = browser.find_element(By.CSS_SELECTOR, "[onclick='saveCensus();']").click()
    time.sleep(10)


finally:
    time.sleep(5)
    browser.quit()
