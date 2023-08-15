from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.aaaauto.cz/")
    page.get_by_role("button", name="Přijmout vše").click()
    page.get_by_role("button", name="Značka Vyberte značku").click()
    page.get_by_text("Škoda").first.click()
    page.get_by_role("button", name="Model Vyberte model").click()
    page.get_by_text("Citigo").first.click()
    page.get_by_role("button", name="Rok Vyberte stáří vozu").click()
    page.get_by_text("Do 10 let").click()
    page.get_by_role("button", name="Cena Vyberte cenu").click()
    page.get_by_text("Do 200 000 Kč", exact=True).click()
    page.get_by_role("button", name="Kategorie Vyberte kategorii").click()
    page.locator("#hpFilterNG").get_by_text("Úsporné vozy").click()
    page.get_by_role("button", name="Hledat").click()