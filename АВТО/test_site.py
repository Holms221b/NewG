from pages.homepage import HomePage
from pages.visitor import VisitorPage


def test_open_abt(browser):
    #for _ in range(3):

        homepage = HomePage(browser)
        homepage.open()
        homepage.auth()
        visitor = VisitorPage(browser)
        visitor.add_vis()


    #клик на посетители
    # btn = browser.find_element(By.XPATH, '//div[@class = "wui-menu"]//div[text() = "Посетители"]').click()
    # sleep(5)
    # #клик на добавить
    # btn_1 = browser.find_element(By.XPATH, '//button [text() = "Добавить"]').click()
    # sleep(5)




