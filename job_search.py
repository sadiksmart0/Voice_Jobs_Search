import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from get_job_details import extract_job_description


def job_search(state):
    print("+++++++++++++++++++ SEARCHING FOR JOB ++++++++++++++++++++")
    driver = state["driver"]
    job_title = state["title"]
    searchbar = driver.find_element(By.ID, "global-nav-search")
    searchbar.click()
    search_input = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search_input.send_keys(job_title)
    search_input.send_keys(Keys.ENTER)


    wait = WebDriverWait(driver, 10)

    # Locate and click the "See More" button
    view_all_button = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-results__cluster-bottom-banner"))
    )
    view_all_button.click()
    time.sleep(5)

        # Locate all job cards within the container
    job_links = driver.find_elements(By.CSS_SELECTOR, "a.job-card-container__link")
    print(f"{type(job_links)} \n {len(job_links)}")

    job_links = extract_job_description(job_links, driver)
    
    return {"jobs": job_links}
