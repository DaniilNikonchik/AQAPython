from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://effective-mobile.ru"

    # Локаторы для блоков
    about_us_locator = "text=О нас"
    contacts_locator = "text=Контакты"
    services_locator = "text=Услуги"
    
    def open(self):
        self.page.goto(self.url)
    
    def click_about_us(self):
        self.page.click(self.about_us_locator)
    
    def click_contacts(self):
        self.page.click(self.contacts_locator)
    
    def click_services(self):
        self.page.click(self.services_locator)
    
    def get_current_url(self):
        return self.page.url
