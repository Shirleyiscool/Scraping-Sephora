import requests
from bs4 import BeautifulSoup
import pandas as pd


def scape_product(link, proxy=None):
    """
    A function to scape all the product links from a given brand link.
    """
    try:
        response = requests.get(link, proxies={
                                "http": proxy, "https": proxy}, timeout=15)
    except:
        print(f'\r Unsuccessfully get data for {link.split("/")[4]}', end="")
        return None
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    product_link_lst = []
    try:
        product_box = soup.find_all(attrs={"data-comp": "ProductGrid "})[0]
    # There might be no products for that brand
    except IndexError:
        return []
    for product in product_box.find_all('a',
                                        attrs={"data-comp": "ProductItem "}):
        # use function split to remove text like "grid p12345"
        product_link_lst.append(
            "https://www.sephora.com" + product.attrs['href'].split()[0])
    return product_link_lst


# Read brand links file
product_link_dic = {'brand': [], 'product_links': []}
num_lines = sum(1 for line in open("data/brand_link.txt", "r"))

# Scape all the product links from all the brands links.
# This will take some time!
ct = 1

# Get proxies from http://www.freeproxylists.net/zh/?c=US&pr=HTTPS&u=80&s=ts
px = ['165.22.211.212:3128', '140.227.237.154:1000', '140.227.238.18:1000']
px_idx = 0

for brand_link in open("data/brand_link.txt", "r"):
    brand_name = brand_link.split('/')[4]
    product_link_list = scape_product(brand_link[:-1], proxy=px[px_idx])

    # If one proxy does not work, use another
    while product_link_list is None:
        px_idx += 1
        if px_idx == 3:
            px_idx = 0
        product_link_list = scape_product(brand_link[:-1], proxy=px[px_idx])

    print(f'\r === {ct} / {num_lines} ===  {brand_name} === {px[px_idx]}',
          end="")
    product_link_dic['brand'] += [brand_name] * len(product_link_list)
    product_link_dic['product_links'] += product_link_list
    ct += 1

# Write the result into csv file
product_link_df = pd.DataFrame(product_link_dic)
product_link_df.to_csv('data/product_links.csv', index=False)

# Indicate scraping completion
print(f'Got All product Links! There are {len(product_link_df)} products in '
      f'total.')
