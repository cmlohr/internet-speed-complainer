from selenium import webdriver
import time

class SpeedCheck:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="_YOUR_DRIVER_PATH_")
        self.webpage = "https://www.speedtest.net/"


    def get_speed(self):
        self.driver.get(self.webpage)
        print(">>> webpage loaded")

        time.sleep(2)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        print(">>> scan begun")
        print("wait...")
        time.sleep(60)
        print(">>> scan complete")
        time.sleep(2)


    def download_speed(self):
        print(">>> getting download")
        download_check = self.driver.find_element_by_css_selector(
            "#container > div > div.main-content > div > div > div > "
            "div.pure-u-custom-speedtest > "
            "div.speedtest-container.main-row > div.main-view > div > "
            "div.result-area.result-area-test > div > div > "
            "div.result-container-speed.result-container-speed-active "
            "> div.result-container-data > "
            "div.result-item-container.result-item-container-align"
            "-center > div > div.result-data.u-align-left > span")
        download_result = download_check.text
        print(f'{download_result}Mbps')
        return download_result



    def upload_speed(self):
        time.sleep(1)
        print(">>> getting upload")
        upload_check = self.driver.find_element_by_css_selector(
            "#container > div > div.main-content > div > div > div > "
            "div.pure-u-custom-speedtest > "
            "div.speedtest-container.main-row > div.main-view > div > "
            "div.result-area.result-area-test > div > div > "
            "div.result-container-speed.result-container-speed-active > "
            "div.result-container-data > "
            "div.result-item-container.result-item-container-align-left "
            "> div > div.result-data.u-align-left > span")
        upload_result = upload_check.text
        print(f'{upload_result}Mbps')
        return upload_result


    def quit(self):
        self.driver.quit()

