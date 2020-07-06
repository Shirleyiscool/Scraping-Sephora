import requests
from bs4 import BeautifulSoup

# Get Response of "brandlist" Website from Sephora
band_lst_link = "https://www.sephora.com/brands-list"
response = requests.get(band_lst_link)

# Use BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Scraping brand links and save them into a list
brand_link_lst = []
main_box = soup.find_all(attrs={"data-comp": "BrandsList Container Box "})[0]
for brand in main_box.find_all('li'):
    brand_link_lst.append("https://www.sephora.com" +
                          brand.a.attrs['href']+"/all?pageSize=300")

# Write brand links into a file:
with open('brand_link.txt', 'w') as f:
    for item in brand_link_lst:
        f.write(f"{item}\n")

# Indicate scraping completion
print(f'Got All Brand Links! There are {len(brand_link_lst)} brands in total.')
