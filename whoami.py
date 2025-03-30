import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
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

  WHOAMI – face search by ekoms savior
        ---------------------------------------------------
    """)

def search_face(image_path):
    if not os.path.exists(image_path):
        print("[!] File not found.")
        return

    ua = UserAgent()
    
    print("[*] Launching stealth browser...")
    driver = uc.Chrome(headless=True, use_subprocess=True)
    
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
            if url:
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
    path = input
