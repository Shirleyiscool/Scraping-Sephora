import re
import time

import pandas as pd
import requests
import json

# Load product link data frame
pd_links_df = pd.read_csv('data/product_links.csv')
# Add a column of product id
pd_links_df['pd_id'] = [re.findall('P[0-9]{4,7}', link)[0] for link
                        in pd_links_df['product_links']]


def scrape_reviews(p_id, proxy=None):
    url = 'https://api.bazaarvoice.com/data/reviews.json'
    params = {
        'Filter': f'ProductId:{p_id}',
        'Sort': 'Helpfulness:desc',
        'Limit': 100,
        'Offset': 0,
        'Include': 'Products,Comments',
        'Stats': 'Reviews',
        'passkey': 'rwbw526r2e7spptqd2qzbkp7',
        'apiversion': 5.4
    }

    reviews = []
    loop = 0

    while True:
        params['Offset'] = len(reviews)

        # Make the same request that Javascript makes
        try:
            r = requests.get(url, params=params, proxies={
                "http": proxy, "https": proxy}, timeout=15)
        except:
            print(f'{proxy} Cannot connect!')
            return None, None
        if loop == 0:
            try:
                product = r.json()['Includes']['Products']
            except KeyError:
                product = []

        # break if we have an error or have all the reviews
        if (r.status_code != 200) or (
                len(reviews) >= r.json()['TotalResults']):
            break

        # add the list of results to current results
        reviews.extend(r.json()['Results'])

        # Give a pause, so we don't get blocked
        time.sleep(0.2)
        loop += 1

    # Show how many reviews we scraped
    print(f'{p_id}: {len(reviews)} reviews')
    time.sleep(0.5)
    return product, reviews


# Scrape Product and Review Data
result = {}
proxies = ['140.227.174.216:1000', '140.227.175.225:1000',
           '140.227.224.177',
           '140.227.237.154:1000', '140.227.173.230:1000',
           '140.227.238.18:1000',
           '165.22.211.212:3128', '140.227.225.38:1000',
           '52.191.103.11:3128']
px_id = 0
loop = 0

for pid in pd_links_df['pd_id']:
    loop_ = loop % 1000
    if (loop_ < 900) and (loop_ >= 150):
        product, reviews = None, None
        while True:
            if px_id == len(proxies):
                px_id = 0
            product_data, reviews_data = scrape_reviews(pid,
                                                        proxy=proxies[px_id])
            if product_data is not None:
                break
            px_id += 1

    # Use my own server to connect
    else:
        product_data, reviews_data = scrape_reviews(pid)
    loop += 1

    print(f'{proxies[px_id]} || {loop:04d}/{len(pd_links_df)}')
    result[pid] = [product_data, reviews_data]

json_result = json.dumps(result)
f = open("data/scraper_result.json", "w")
f.write(json_result)
f.close()
