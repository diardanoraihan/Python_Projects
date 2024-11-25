from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # the way we want to find the element inside the web page
from selenium.webdriver.common.keys import Keys # keys mean keys we want to press in our keyboards
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from miscellaneous import get_data_adm
import time

# we will create a web driver (that will be downloaded and installed) as an automation tool that controls Google Chrome
# can work with any browser
# https://sites.google.com/chromium.org/driver/
# service = Service(executable_path="/Users/diardanoraihan/Work/GITHUB/Python_Projects/Reminder/9_importing/Web Scraping by Selenium/chromedriver")
service = Service(executable_path="Reminder/9_importing/Web Scraping by Selenium/chromedriver")
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(10)

driver.get("https://google.com")

# If after 5 seconds the element doesn't exist, go ahead and just crash the program
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # clear any prompt inside the text box
input_element.send_keys("kemenparekraf chse" + Keys.ENTER)

# If 'chse kemenparekraf' exists inside of some kind of anchor or link tag, we will access it
# To find multiple pages, use .find_elements then iterate over each element [element_1, element_2, etc]
link = driver.find_element(By.PARTIAL_LINK_TEXT, "CHSE Kemenparekraf")
link.click()

# If after 5 seconds the element doesn't exist, go ahead and just crash the program
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.LINK_TEXT, "Daya Tarik Wisata"))
)
link = driver.find_element(By.LINK_TEXT, "Daya Tarik Wisata")
link.click()

# If after 5 seconds the element doesn't exist, go ahead and just crash the program
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.LINK_TEXT, "Filter"))
)
link = driver.find_element(By.LINK_TEXT, "Filter")
link.click()
time.sleep(1)

# If after 5 seconds the element doesn't exist, go ahead and just crash the program
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID, "province_id"))
)
link = driver.find_element(By.ID, "province_id")
link.click()

link = driver.find_element(By.ID, "province_id")
link.click()


province_dropdown = driver.find_element(By.ID, "province_id")
# Buat objek Select dan pilih 'Jawa Barat' berdasarkan teks
select = Select(province_dropdown)
select.select_by_visible_text("JAWA BARAT")

# Klik Filter setelah memilih Jawa Barat
WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH, "//*[@id='filtersModal']/div/div/div[3]/div/a[2]"))
)
link = driver.find_element(By.XPATH, "//*[@id='filtersModal']/div/div/div[3]/div/a[2]")
link.click()

# Tunggu halaman web untuk update
time.sleep(2)

data = {
'objek_wisata': [],
'alamat': [],
'provinsi': [],
'kab_kota': [],
'kecamatan': [],
'desa': [],
'latitude': [],
'longitude': []
}

# Klik halaman selanjutnya
for i in range(24):
  try:
    print(f'\n++++++++ Accessing Page {i+1} ++++++++')
    WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "card-title"))
    )

    elements = driver.find_elements(By.CLASS_NAME, "card-title")
    tourism_places = []
    for element in elements:
      tourism_places.append(element.text)
      
    print(f"Destinasi Wisata: {', '.join(tourism_places)}")

    for tourism_place in tourism_places:
      try:
        WebDriverWait(driver, 20).until(
          # EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, tourism_place))
          EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, tourism_place))
        )
        
        current_url = driver.current_url
        
        # Akses halaman destinasi wisata
        print(f"Attempt to visit: {tourism_place}")
        link = driver.find_element(By.PARTIAL_LINK_TEXT, tourism_place)
        
        # Validasi apakah elemen terlihat
        if not link.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", link)

        # Gunakan JavaScript atau ActionChains jika klik biasa gagal
        try:
            link.click()
            
        except ElementClickInterceptedException:
            print(f"Element click intercepted for {tourism_place}. Trying JavaScript click.")
            driver.execute_script("arguments[0].click();", link)
        
        # Validasi URL berubah
        WebDriverWait(driver, 10).until(lambda d: d.current_url != current_url)
        print(f"Attempt successful WITHOUT timeout: {driver.current_url}")
        
        # Retrieve data in the new web page
        data_temp = get_data_adm(driver.current_url)
        data['objek_wisata'].append(data_temp['objek_wisata'])
        data['alamat'].append(data_temp['alamat'])
        data['provinsi'].append(data_temp['provinsi'])
        data['kab_kota'].append(data_temp['kab_kota'])
        data['kecamatan'].append(data_temp['kecamatan'])
        data['desa'].append(data_temp['desa'])
        # print(data)
        time.sleep(2)
        
        # Kembali ke halaman sebelumnya
        driver.back()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card-title"))
        )
        
      except TimeoutException:
        
        print(f"Attempt successful WITH timeout: {driver.current_url}")
        print("Page load timeout. Stopping...")
        driver.execute_script("window.stop();")
        
        # Retrieve data in the new web page
        data_temp = get_data_adm(driver.current_url)
        data['objek_wisata'].append(data_temp['objek_wisata'])
        data['alamat'].append(data_temp['alamat'])
        data['provinsi'].append(data_temp['provinsi'])
        data['kab_kota'].append(data_temp['kab_kota'])
        data['kecamatan'].append(data_temp['kecamatan'])
        data['desa'].append(data_temp['desa'])
        
        # driver.save_screenshot("timeout_error.png")
        # Hentikan loading jika timeout
        # Kembali ke halaman sebelumnya
        driver.back()
        time.sleep(1)
        # print(data)
        
    # Klik tombol "Next"
    try:
        print(data)
        print(f"Total current objek wisata: {len(data['objek_wisata'])}")
        
        WebDriverWait(driver, 20).until(
          # EC.presence_of_element_located((By.CLASS_NAME, "bi-caret-right-fill")),
          EC.element_to_be_clickable((By.CLASS_NAME, "bi-caret-right-fill"))
        )
        button_next = driver.find_element(By.CLASS_NAME, "bi-caret-right-fill")
        button_next.click()
        time.sleep(2)
        
    # except TimeoutException:
    except:
        print("Next button not found. Possibly last page.")
        break
  
  except TimeoutException:
    print("Timeout occurred while processing the page.")
    driver.save_screenshot("timeout_error.png")
    break

driver.quit()

print(data)

with open('/Users/diardanoraihan/Work/GITHUB/Python_Projects/Reminder/9_importing/Web Scraping by Selenium/scrapped_data.txt', 'w') as file:
  file.write(data)

