from selenium.webdriver.common.by import By


def login_to_linkedin(state):
    print("+++++++++++++++++++ LOGIN IN TO LINKEDIN ++++++++++++++++++++")
    driver = state["driver"]
    login_page = driver.find_element(By.CLASS_NAME, "header__content__heading ").text
    if login_page == "Sign in":
        print(login_page)
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        
        username_input.send_keys("USERNAME")
        password_input.send_keys("PASSWORD")
    
        login_page = driver.find_element(By.XPATH, "/html/body/div/main/div[3]/div[1]/form/div[4]/button")
        login_page.click()
        return {"driver": driver}
    
    #When passwords & username is set on remembered    
    elif login_page == "Welcome Back":    
        print(login_page)
        login_page = driver.find_element(By.CLASS_NAME, "member-profile__details")
        login_page.click()
        return {"driver": driver}
    
    #When login is in place but not set on remember
    elif login_page == "Welcome back":
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("B00kw0rm1")
        login_page = driver.find_element(By.XPATH,  "/html/body/div/main/div[4]/div[1]/div[3]/form/div[2]/button")
        login_page.click()
        
        return {"driver": driver}