from playwright.sync_api import Page
import pytest

def test_tlacitek_menu(page: Page):
    page.goto("/")
    # tlačítko články
    page.locator('//*[@id="menu"]/ul/li[1]/strong/a').click()
    # tlačítko Hlavní stránka
    page.locator('//*[@id="menu"]/ul/li[1]/strong/a').click()
    # tlačítko O mně
    page.locator('//*[@id="menu"]/ul/li[2]/strong/a').click()
    # tlačítko Hlavní stránka
    page.locator('//*[@id="menu"]/ul/li[1]/strong/a').click()
    