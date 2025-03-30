# whoami.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time
import os

def on_brand_banner():
    print("""
██╗    ██╗██╗  ██╗ ██████╗  █████╗ ███╗   ███╗██╗
██║    ██║██║  ██║██╔═══██╗██╔══██╗████╗ ████║██║
██║ █╗ ██║███████║██║   ██║███████║██╔████╔██║██║
██║███╗██║██╔══██║██║   ██║██╔══██║██║╚██╔╝██║██║
╚███╔███╔╝██║  ██║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝

        WHOAMI – face intelligence search by ekoms
savior        ---------------------------------------------------
    """)

def search_face(image_path):
    if not os.path.exists(image_path):
        print("[!] File not found.")
        return

    ua = UserAgent()
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("[*] Opening PimEyes...")
        driver.get("https://pimeyes.com/en")

        time.sleep(3)
        try:
            accept = driver.find_element(By.XPATH, '//button[text()="Accept all"]')
            accept.click()
        except:
            pass

        print("[*] Uploading your photo...")
        upload = driver.find_element(By.XPATH, '//input[@type="file"]')
        upload.send_keys(os.path.abspath(image_path))

        print("[*] Searching, please wait...")
        time.sleep(25)

        links = driver.find_elements(By.XPATH, '//a[contains(@href, "https://pimeyes.com/en/")]')

        print("\n[*] Potential Matches:")
        found = False
        for link in links:
            url = link.get_attribute("href")
            if "/en/" in url:
                print(" →", url)
                found = True

        if not found:
            print("No matches found. Try a clearer face photo.")

    except Exception as e:
        print("[!] Error:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    on_brand_banner()
    path = input("Enter the path to your face image (e.g. face.jpg): ")
    search_face(path.strip())
