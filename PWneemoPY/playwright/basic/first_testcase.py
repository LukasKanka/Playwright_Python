from playwright.sync_api import Page
import pytest


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Přijmout vše").click()
    page.get_by_label("Najít").click()
    page.get_by_label("Najít").fill("playwright")
    page.get_by_label("Hledat Googlem").first.click()
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... playwright.dev https://playwright.dev").click()


