import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener, EventFiringWebDriver
)

dict_types = {
    'text':"Willia",
    'email': 'jwil@live.com',
    'password': 'livedepython'
}

nav = Firefox()

nav.get('https://selenium.dunossauro.live/exercicio_07')

class Escuta(AbstractEventListener):
    def before_click(self, elem, browser):
        print("vou clicar")

    def after_click(self, elem, browser):
        print("já cliquei")


listen_nav = EventFiringWebDriver(nav, Escuta())

time.sleep(2)

fields = listen_nav.find_elements_by_css_selector('.form-group')

for ele in fields:
    ele.find_element_by_tag_name('input').click()

nav.close()


