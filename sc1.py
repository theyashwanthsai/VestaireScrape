import requests
from bs4 import BeautifulSoup
import json

# url = "https://www.vestiairecollective.com/women-clothing/dresses/jacquemus/green-linen-lannee-97-jacquemus-dress-35053779.shtml"  

url = "https://www.vestiairecollective.com/men-shoes/trainers/gucci/multicolour-cloth-gucci-trainers-34517413.shtml"  

# url = "https://www.vestiairecollective.com/women-bags/handbags/gucci/red-leather-gg-marmont-oval-gucci-handbag-35884160.shtml"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")


price_tag = soup.find("span", {"data-cy": "product_price"})
price = price_tag.text.strip() if price_tag else "Price not found"


name_tag = soup.find("div", {"data-cy": "productTitle_name"})
name = name_tag.text.strip() if name_tag else "name not found"


div_element = soup.find('div', class_='vc-images_imageContainer__D7OIG')
inner_elements = div_element.find_all('img') 






print("Name:", name)
print("Price:", price)

for element in inner_elements:
    print(element.get('src'))  


image_urls = []

div_containers = soup.find_all('div', class_='lazyload-wrapper vc-images_imageContainer__D7OIG')

for div_container in div_containers:
    img_tag = div_container.find('img')
    if img_tag:
        image_url = img_tag.get('src')
        image_urls.append(image_url)

# print(image_urls)

    
# for x in soup.find_all('script', {"id": "__NEXT_DATA__"}):
#     print(x)


js = soup.find_all('script', {"id": "__NEXT_DATA__"})
json_data_list = []

# Loop through the extracted script tags
for script_tag in js:
    # Get the content of the script tag
    script_content = script_tag.string
    
    # Convert the script content to a Python dictionary
    try:
        json_data = json.loads(script_content)
        json_data_list.append(json_data)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

# Write the JSON data to a file
with open("output.json", "w") as json_file:
    json.dump(json_data_list, json_file, indent=4)




productDescription = json_data['props']['pageProps']['product']['originalDescription']


