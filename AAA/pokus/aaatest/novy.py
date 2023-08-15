from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.cz/?gws_rd=ssl")
    page.get_by_role("button", name="Přijmout vše").click()
    page.get_by_label("Najít").click()
    page.get_by_label("Najít").fill("test")