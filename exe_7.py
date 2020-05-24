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
        print(elem.find_element_by_tag_name('label').text)

    def after_click(self, elem, browser):
        print(elem.find_element_by_tag_name('label').text)


listen_nav = EventFiringWebDriver(nav, Escuta())

time.sleep(3)

fields = listen_nav.find_elements_by_css_selector('.form-group')

for ele in fields:
    field = ele.find_element_by_tag_name('input').wrapped_element
    intype = field.get_attribute('type')
    if intype=='submit':
        field.click()
    else:
        ele.click()
        field.send_keys(dict_types[intype])
