import os


class EcoPage:

    def __init__(self, page):
        self.page = page
        self.co2_item = page.locator(
            "xpath=//div[text()='не попало в атмосферу']/ancestor::div[@class='desktop-impact-item-eeQO3']"
        )
        self.water_item = page.locator(
            "xpath=//div[text()='было сохранено']/ancestor::div[@class='desktop-impact-item-eeQO3']"
        )
        self.energy_item = page.locator(
            "xpath=//div[text()='было сэкономлено']/ancestor::div[@class='desktop-impact-item-eeQO3']"
        )

    def navigate(self):
        self.page.goto("https://www.avito.ru/avito-care/eco-impact")

    def screenshot_item(self, item, filename):
        folder_path = "output"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        item.screenshot(path=file_path)

    def screenshot_co2_item(self):
        self.screenshot_item(self.co2_item, 'co2.png')

    def screenshot_water_item(self):
        self.screenshot_item(self.water_item, 'water.png')

    def screenshot_energy_item(self):
        self.screenshot_item(self.energy_item, 'energy_item.png')
