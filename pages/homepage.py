from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from script.script import check_AJAX


class HomePage:

    def __init__(self,browser):
        self.browser, self.wait = browser


    def open(self):
        self.browser.get('http://192.168.4.137:8000/auth')
        self.browser.execute_script(check_AJAX())

    def wait_for_ajax(self):

        try:
            self.wait.until(
            lambda driver: driver.execute_script("return window.checkActiveAjaxRequests();") == 0
            )
        except Exception as e:
            print(f"Таймаут: не все AJAX-запросы завершены.{e}")


    def auth(self):
        locators = {

                "login_wrapper": ("xpath", "//div[@class='login__wrapper']"),
                "logo": ("xpath", "//img[@class='login__logo-img']"),
                "text_login": ("xpath", "//div[@class='login__title-box']/span[text()='Авторизация']"),
                "eye_icon": ("xpath", "//div[@class='eye_icon']"),

                "username_input": ("xpath", "//input[@name='username']"),
                "password_input": ("xpath", "//input[@name='password']"),
                "logout_button": ("xpath", "//span[text()='Выйти']"),

                "login_button": ("xpath", "//button[text()='Войти']")}


        self.wait_for_ajax()
        self.wait.until(EC.visibility_of_element_located(locators["login_wrapper"]))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class ="login__logo-img"]')))

        #text_auth = self.browser.find_element(By.XPATH, "//input[@placeholder='Введите логин']")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span [text() = 'Авторизация']")))
        auth_2 = self.wait.until(EC.visibility_of_element_located(locators["username_input"]))
        auth_2.send_keys('root')
        text_login = self.wait.until(EC.visibility_of_element_located(locators["password_input"]))
        text_login.send_keys('123456')
        self.wait.until(EC.presence_of_element_located((locators["login_button"]))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class = "wui-menu"]//div[text() = "Архив"]')))
        self.wait_for_ajax()
        #self.wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@class ="sidebar-img"]')))
        #self.wait.until(EC.visibility_of_element_located((By.XPATH, "//body")))
        #self.browser.implicitly_wait(5)
        #self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Выйти']"))).click()
        # self.browser.refresh()
        self.browser.save_screenshot('ABT.png')