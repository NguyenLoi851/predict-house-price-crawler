from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

PATH = './chromedriver'
service = Service(PATH)

# driver.get("https://www.nhatot.com/mua-ban-nha-dat?page=11")
# time.sleep(3)
# # print(driver.title)
# main = driver.find_element(By.CLASS_NAME,'AdBody_adPriceNormal___OYFU')
# print(main.text)
# # print(driver.page_source)
# driver.quit()

class House:
    area: str = ''
    price: str = ''
    bedroom_amount: str = ''
    bathroom_amount: str = ''
    floor_amount: str = ''
    legal_document: str = ''
    land_feature: str = ''
    type: str = ''
    furnish_status: str = ''
    location: str = ''
    length: str = ''
    width: str = ''
    living_area: str = ''
    main_door_direction: str = ''
    listing_time: str = ''

def crawl_each_page(i):
    try:
        driver = webdriver.Chrome(service=service)
        url = 'https://www.nhatot.com/mua-ban-nha-dat?page={}'.format(i)
        driver.get(url=url)
        # time.sleep(10)
        # href_child_house = driver.find_elements(By.CLASS_NAME, 'AdBody_adPriceNormal___OYFU')
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'ListAds_ListAds__rEu_9'))
        )
        id_tag_parent = driver.find_element(By.CLASS_NAME, 'ListAds_ListAds__rEu_9')
        href_child_house_tags = id_tag_parent.find_elements(By.TAG_NAME, 'a')
        url_houses = list()
        for href_child_house_tag in href_child_house_tags:
            if 'https' in str(href_child_house_tag.get_attribute('href')):
                # print(href_child_house_tag.get_attribute('href'))
                url_houses.append(str(href_child_house_tag.get_attribute('href')))
        # print(url_houses)
        driver.quit()

        for url_house in url_houses:
            subdriver = webdriver.Chrome(service=service)
            houseInstance = House()
            subdriver.get(url=url_house)

            try:
                WebDriverWait(subdriver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,'fz13'))
                )
                location = subdriver.find_element(By.CLASS_NAME, 'fz13')
                houseInstance.location = str(location.text.split(',')[-1].split('\n')[0])
            except Exception as elocation:
                print(elocation)
            
            try:
                WebDriverWait(subdriver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,'AdDecriptionVeh_date__SpYR1'))
                )
                time = subdriver.find_elements(By.CLASS_NAME, 'AdDecriptionVeh_date__SpYR1')[1]
                houseInstance.listing_time = str(time.text)
            except Exception as etime:
                print(etime)

            try:
                WebDriverWait(subdriver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,'AdParam_adParamValue__IfaYa'))
                )
                features = subdriver.find_elements(By.CLASS_NAME,'AdParam_adParamValue__IfaYa')
                # print(feature.get_attribute('itemprop'))
                for feature in features:
                    # print(feature.get_attribute('itemprop'))
                    name = str(feature.get_attribute('itemprop'))
                    # print(feature.text.split()[0])
                    if name == "size":
                        houseInstance.area = feature.text.split()[0]
                        # print("area", houseInstance.area)
                    if name == "price_m2":
                        houseInstance.price = feature.text.split()[0]
                        # print("price", houseInstance.price)
                    if name == "rooms":
                        houseInstance.bedroom_amount = feature.text.split()[0]
                        # print("bedroom", houseInstance.bedroom_amount)
                    if name == "toilets":
                        houseInstance.bathroom_amount = feature.text.split()[0]
                        # print("bathroom", houseInstance.bathroom_amount)
                    if name == "floors":
                        houseInstance.floor_amount = feature.text
                        # print("floor", houseInstance.floor_amount)
                    if name == "width":
                        houseInstance.width = feature.text
                        # print("width", houseInstance.width)
                    if name == "length":
                        houseInstance.length = feature.text
                        # print("length", houseInstance.length)
                    if name == "living_size":
                        houseInstance.living_area = feature.text.split()[0]
                        # print("living size", houseInstance.living_area)
                    if name == "furnishing_sell":
                        houseInstance.furnish_status = feature.text
                        # print("furnish", houseInstance.furnish_status)
                    if name == "house_type":
                        houseInstance.type = feature.text
                        # print("type", houseInstance.type)
                    if name == "property_road_condition":
                        houseInstance.land_feature = feature.text
                        # print("condition", houseInstance.land_feature)
                    if name == "direction":
                        houseInstance.main_door_direction = feature.text
                        # print("direction", houseInstance.main_door_direction)
                    if name == "property_legal_document":
                        houseInstance.legal_document = feature.text
                        # print("legal document", houseInstance.legal_document)
                    
                subdriver.quit()
                csvwriter.writerows([[houseInstance.area, houseInstance.price, houseInstance.bedroom_amount, houseInstance.bathroom_amount, houseInstance.floor_amount, houseInstance.legal_document, houseInstance.land_feature, houseInstance.type, houseInstance.furnish_status, houseInstance.location, houseInstance.length, houseInstance.width, houseInstance.living_area, houseInstance.main_door_direction, houseInstance.listing_time]])
            except Exception as efeatures:
                print(efeatures)
    except Exception as e:
        print(e)

try:
    fields = ['Area', 'Price', 'Bedroom amount', 'Bathroom amount', 'Floor amount', 'Legal document', 'Land feature', 'Type', 'Furnish status', 'Location', 'Length', 'Width', 'Living area', 'Main door direction', 'Listing time']
    filename = 'test.csv'
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        # crawl_each_page(11)
        for i in range(1, 10):
            crawl_each_page(i)
            print(i)
except Exception as emain:
    print(emain)