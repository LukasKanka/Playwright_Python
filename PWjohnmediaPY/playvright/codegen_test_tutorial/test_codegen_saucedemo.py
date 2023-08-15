from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

# v codegen vygeneruji v mém případě zatím code v pytest
# https://playwright.dev/python/docs/codegen#recording-a-test

# video jakým vše možným způsobem se dá použít playwright codegen je zde: https://youtu.be/IRTeqUXkPbA
# třeba jeémožné ho použít na nacvakání jako na iPhone, nebo daným rozlišení stránky
# velikost textu se zobrazí v nastavení parametrů přímo v testu