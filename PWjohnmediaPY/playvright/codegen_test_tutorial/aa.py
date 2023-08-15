from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.aaaauto.cz/")
    page.get_by_role("button", name="Přijmout vše").click()
    page.get_by_role("button", name="Značka Vyberte značku").click()
    page.get_by_text("Škoda (2793)").first.click()
    page.get_by_role("button", name="Model Vyberte model").click()
    page.get_by_text("Citigo(40)").click()
    page.get_by_role("button", name="Rok Vyberte stáří vozu").click()
    page.get_by_text("Do 10 let").click()
    page.get_by_role("button", name="Cena Vyberte cenu").click()
    page.get_by_text("Do 200 000 Kč", exact=True).click()
    page.get_by_role("button", name="Kategorie Vyberte kategorii").click()
    page.locator("#hpFilterNG").get_by_text("Úsporné vozy").click()
    page.get_by_role("button", name="Hledat").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)