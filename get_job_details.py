from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def extract_job_description(job_links, driver):
    # Extract job titles and links into a dictionary
    jobs = {}
    for job in job_links:
        title = job.get_attribute("aria-label")  # Job title
        link = job.get_attribute("href")       # Job link
        if title and link:  # Ensure both title and link are available
            jobs[title] = link

    # Print or store the job dictionary
    print(f"Number of jobs found: {len(jobs)}")

    job_info_text = {}

    for title, job_url in jobs.items():
        driver.get(job_url)
        
        # Wait for the page to load
        wait = WebDriverWait(driver, 20)
    

        # Locate and click the "See More" button if present
        see_more_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-description__footer-button"))
        )
        see_more_button.click()
    


    # Wait for the job description container
    
        job_description_container = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article.jobs-description__container"))
        )
        
        driver.execute_script("arguments[0].scrollIntoView();", job_description_container)
    
        # Extract and store the job description text
        job_description = job_description_container.text
        
        # Store the title, description, and URL in the nested dictionary
        job_info_text[title] = {
            "description": job_description,
            "url": job_url
        }

    
    return job_info_text