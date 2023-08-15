from playwright.sync_api import Page
import pytest

#doporučuji zde se podívat jak stopnout některy browsey https://youtu.be/IDrTacdVNRM?t=838
# @pytest.mark.skip_browser("firefox")
# @pytest.mark.only_browser("chrome")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"



def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."


    # pytest --tracing on  --> tento pžíkaz na spuštění testu vytvoří složky kde je v zip výsledek testu
    # zip mohu otevřít zde a podívat se na výsledek testu https://trace.playwright.dev/
    # další možnosti jak využít trace.zip https://youtu.be/IDrTacdVNRM?t=1148

    # na inportovaném pytest.ini mužu nastavit default URL a další parametry