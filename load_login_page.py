from selenium import webdriver
from selenium.webdriver.common.by import By


def load_login_page(state):
    print("+++++++++++++++++++ LOADING LINKEDIN PAGE ++++++++++++++++++++")
    driver = state["driver"]
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", False)
    options.page_load_strategy = 'normal'
    driver = webdriver.Edge(options=options)
    driver.get("https://www.linkedin.com")
    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in.click()
    
    return {"driver": driver}