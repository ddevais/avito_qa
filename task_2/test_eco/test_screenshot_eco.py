from playwright.sync_api import sync_playwright

from task_2.pages.eco import EcoPage


def test_screenshot_co2_item():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        eco_page = EcoPage(page)
        eco_page.navigate()
        eco_page.screenshot_co2_item()
        browser.close()


def test_screenshot_water_item():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        eco_page = EcoPage(page)
        eco_page.navigate()
        eco_page.screenshot_water_item()
        browser.close()


def test_screenshot_energy_item():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        eco_page = EcoPage(page)
        eco_page.navigate()
        eco_page.screenshot_energy_item()
        browser.close()
