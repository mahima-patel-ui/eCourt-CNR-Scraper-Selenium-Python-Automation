"""
DEBUG VERSION - Court CNR Scraper (Wrapped for API + Manual Use)
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import traceback

# ✅ Wrapping your scraper logic into a function
def scrape_case_details(cnr):
    try:
        print("🔍 Starting browser...")

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")
        time.sleep(3)

        print("✅ Browser started. Navigating to CNR tab...")
        driver.find_element(By.LINK_TEXT, "CNR Number").click()
        time.sleep(2)

        driver.find_element(By.ID, "cnrno").send_keys(cnr)

        print("⏳ Please solve the CAPTCHA manually...")
        input("✅ After solving CAPTCHA, press Enter here to continue...")

        driver.find_element(By.ID, "submit1").click()
        time.sleep(4)

        # Scrape case details
        party_name = driver.find_element(By.XPATH, '//*[@id="petitioner"]')
        filing_date = driver.find_element(By.XPATH, '//*[@id="Filing_number_date"]')
        hearing_date = driver.find_element(By.XPATH, '//*[@id="next_date"]')

        result = {
            "CNR": cnr,
            "party_name": party_name.text,
            "filing_date": filing_date.text,
            "next_hearing": hearing_date.text
        }

        print("\n🎉 Final Output:")
        for k, v in result.items():
            print(f"{k}: {v}")

        driver.quit()
        return result

    except WebDriverException as e:
        print("❌ WebDriver failed to start.")
        traceback.print_exc()
        return {"error": "WebDriver error"}
    except Exception as ex:
        print("❌ An error occurred:")
        traceback.print_exc()
        return {"error": str(ex)}
    finally:
        try:
            input("Press Enter to close browser...")
            driver.quit()
        except:
            pass

# ✅ Manual run mode (like before)
if __name__ == "__main__":
    cnr = input("Enter 16-digit CNR number (e.g., HRFB010018772023): ")
    scrape_case_details(cnr)
