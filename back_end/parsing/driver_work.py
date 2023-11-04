from selenium import webdriver
import time

def create_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        options=options
    )
    return driver


def scroll_page(driver):
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

    while True:
        lastLenPage = lenOfPage
        time.sleep(1)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(1)
        if lastLenPage == lenOfPage:
            break


def get_site_code(url):
    driver = create_driver()
    try:
        driver.get(url=url)
        time.sleep(3)
        scroll_page(driver)
        time.sleep(2)
        response = driver.page_source

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return response