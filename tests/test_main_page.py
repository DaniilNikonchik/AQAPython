import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

def test_about_us(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_about_us()
    assert main_page.get_current_url() == "https://effective-mobile.ru/about"

def test_contacts(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_contacts()
    assert main_page.get_current_url() == "https://effective-mobile.ru/contacts"

def test_services(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_services()
    assert main_page.get_current_url() == "https://effective-mobile.ru/services"
