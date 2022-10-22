from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import time
path = "C:/Users/tayal/Downloads/chromedriver_win321/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")

result = {}
def run_code(url):
    array1 = {}
    # url = "https://www.amazon.fr/dp/000108898X"
    d = webdriver.Chrome(executable_path=path, chrome_options=options)
    d.get(url)
    try:
        title = d.find_element_by_id("productTitle").text
    except:
        title = "NA"
    # print(title)
    array1['Product_Name'] = title
    try:
        image = d.find_element(by=By.CLASS_NAME, value = "a-dynamic-image").get_attribute("src")
    except:
        image = "NA"
    # print(image)
    array1['Product_Image'] = image
    try:
        price = d.find_element(by=By.CLASS_NAME, value = "a-color-price").text
    except:
        try:
            price = d.find_element(by=By.CLASS_NAME, value="a-price").text
        except:
            price = "NA"
    # print(price)
    array1['Product_Price'] = price
    try:
        details = d.find_element(by=By.ID, value = "detailBullets_feature_div").text
    except:
        details = "NA"
    if details == "NA":
        try:
            details = d.find_element(by=By.ID, value="productDetails_techSpec_section_1").text
        except:
            details = "NA"
    # print(desc)
    array1['Product_Desc'] = details
    result[f'{url}'] = array1
    d.quit()





if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		run_code(links)

print(result)
with open("sample.json", "w") as outfile:
    json.dump(result, outfile)
# print(json_object)



