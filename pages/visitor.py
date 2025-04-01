from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from endpoints.base_endpoints import Status
from script.script import check_AJAX
from person_dto.dto import add_passport_visitor_dto


class VisitorPage(Status):

    def __init__(self,browser):
        self.browser, self.wait = browser

    def wait_for_ajax(self):

        try:
            self.wait.until(
            lambda driver: driver.execute_script("return window.checkActiveAjaxRequests();") == 0
            )
        except Exception as e:
            print(f"Таймаут: не все AJAX-запросы завершены.{e}")

    def add_vis(self):
        self.browser.execute_script(check_AJAX())
        self.wait_for_ajax()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class = "wui-menu"]//div[text() = "Архив"]')))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class = "wui-menu"]//div[text() = "Посетители"]'))).click()
        #self.wait_for_ajax()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class = "box box-table"]')))
        # self.wait.until(EC.presence_of_element_located((By.XPATH,   '//span[text() = "Поиск"]')))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button [text() = "Добавить"]'))).click()
        self.wait_for_ajax()
        self.browser.save_screenshot('ABT1.png')
        # add_btn = self.browser.find_element(By.XPATH, '//button [text() = "Добавить"]')
        #add_btn.click()
        #assert add_btn.text == 'Добавить','текст кнопки не совпал'

        dto = add_passport_visitor_dto()
        print(dto)
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "last_name"]'))).send_keys(dto['last_name'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "first_name"]'))).send_keys(dto['first_name'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "middle_name"]'))).send_keys(dto['middle_name'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "phone"]'))).send_keys(dto['phone'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "fixed_line_phone"]'))).send_keys(dto['fixed_line_phone'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "company_name"]'))).send_keys(dto['company_name'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "office"]'))).send_keys(dto['office'])
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name = "department"]'))).send_keys(dto['department'])
        #
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text() = "Паспортные данные"]')))
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '// button[text() = "Добавить фото паспорта "]')))
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '// div[text() = "Данные транспорта"]')))
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, '// button[text() = "Отмена"]')))
        #  self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button [text() = "Сохранить"]'))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '// div[@class ="wui-switch__ctrl"]'))).click()

        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '// div[@class ="wui-input wui-input_small"] // input')))

        for element in elements:
            i = element.get_attribute("name")
            element.send_keys(dto[i])
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//label[@class = "wui-select__ctrl" and text() = "Выберите пол"]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[@class = "wui-select__option" and text() = "{dto['gender']}"]'))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button [text() = "Сохранить"]'))).click()
        sleep(5)
