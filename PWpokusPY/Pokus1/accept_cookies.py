import re
from playwright.sync_api import Page, expect


def test_homepage_lukan_cz_accept_cookies(page: Page):
    page.goto("https://lukan.cz/")
    get_accept = page.get_by_text("Accept")
    get_accept.click()

    #vypíše titulek stánky
    print( page.title())

    #Vytvoříme foto stránky
    page.screenshot(path="screenshot/lukan.png")


def test_homepage_lukan_cz_decline_cookies(page: Page):
    page.goto("https://lukan.cz/")
    get_decline = page.get_by_text("Decline")
    get_decline.click()