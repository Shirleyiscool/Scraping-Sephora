# Sephora Product Analysis
  - Start date: 02/2019
  - For education: FE 290 - Data and Programming for Analytics @ UCI
  - Author: Shirley Li


Table of Contents
---
   * [About the project](#about-the-project)
   * [Scraping data from Sephora](#scraping-data-from-sephora)
      * [Step 1: Get all the brand links and product links](#step-1-get-all-the-brand-links-and-product-links)
         * [a) From Sephora's Brand list website, we can scrape all the brand links.](#a-from-sephoras-brand-list-website-we-can-scrape-all-the-brand-links)
         * [b) After clicking each brand link, we can see all the product page and scrape all the product links.](#b-after-clicking-each-brand-link-we-can-see-all-the-product-page-and-scrape-all-the-product-links)
      * [Step 2: Get product information](#step-2-get-product-information)
      * [Future Work to Do](#future-work-to-do)
   * [Visualizations and Analysis for Sephora products](#visualizations-and-analysis-for-sephora-products)



## About the project
This project is for the group work of class FE290 during my accounting master study at UCI.
I am the person who is responsible to scape the data and do analysis. This project is just for education.
After my study in MSDS program at USF, I decided to optimize the codes and improve my programming skills
at the same time. So I try to optimize the codes during the winter break in 12/2019. However, there are sill
some things to improve but that would take some time. So this project is going to be updated from time to time.

## Scraping data from Sephora
Here are some steps to scape the product information.

### Step 1: Get all the brand links and product links

Notebook link [here](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/scrape_notebook/1-Brand%26Product_links.ipynb)

#### a) From Sephora's Brand list website, we can scrape all the brand links.
![brand list screenshot](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/image/brand_list_screenshot.png)


12/29/2019: There are **345** brands in total on Sephora website.

#### b) After clicking each brand link, we can see all the product page and scrape all the product links.
![product list screenshot](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/image/product_list_screenshot.png)

12/29/2019: There are **3085** products in total on Sephora website.

**Note**: To show all the product links, the brand link must add `/all?pageSize=300` at the end for scraping.

### Step 2: Get product information

From the product page, we can decide what information we are going to scrape.
![product list screenshot](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/image/product_info_screenshot.png)

Here, we are going to scrape information including product name, product ID, item id, category, brand, price, size, love count, review count, rating.

Since the reviews are coded with JavaScript, we cannot simply scrape them with BeautifulSoup. Instead, Selenium might work, which would be the future work.

But now, we mainly use `get_data` function to scrape product information from each product link.

```
def get_data(product_link):
    """
    Given a product link, return a dictionary of product info
    including product id, product name, brand, category, item
    number, price, size, love counts, review counts, rating and link
    """
    ...
```

However, when we scrape all the product information, it means we have to request Sephora for over 3000 times, and we will take risk being blocked.

To prevent being blocked by Sephora, there are two ways that we can do.

1) Use different VPNs and try to scrape about 1500 links for one time.

2) Use different proxies to request.

For the first way [(VPN)](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/scrape_notebook/2-Product_Info_vpn.ipynb), it would be simple for coding. But it would be inconvenient because you may need to download a vpn app and try to connect it when running the notebook.

For the second way [(proxies)](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/scrape_notebook/2-Product_Info_proxies.ipynb), it is hard to find good proxies online. So far, I cannot find an easy way to automatically scrape proxies and find workable proxies to scrape data. I could get some workable proxies online by hand, but it is also required Selenium to scrape them as they are written in JavaScript. This is to do in the future as well.

After scraping the product information, we save them as a Dataframe with pandas, and export [a csv file](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/scrape_notebook/Sephora_product_info.csv).

### Future Work to Do

1. Try to use Selenium to <br>
  a) Scrape product reviews as well as the user characteristics. <br>
  b) Scrape workable proxies for scraping Sephora without blocking.

2. There might be different items for the same product. (For example, Lips could have different color for the same product.) Therefore, I just scrape the default item for each product. In the future, there might be some ways to scrape all the items for the same product.

3. Regarding the description of the product, the information is not consistent throughout all products. Some might have introduction, while some just leave that blank. If we can also scrape the ingredients for some products, that would be also helpful for product analysis.

3. Organize all the notebooks and summarize all the function as a package or as an API

## Visualizations and Analysis for Sephora products

After [cleaning the data](https://github.com/Shirleyiscool/Scraping-Sephora/tree/master/clean_data), we use Tableau to do visualizations.

The focus is on price as I am planning to do ML to predict price based on other information we got.

What could lead high price?
![What could lead high price?](master/EDA/price.png)

Ratings vs Love Counts:
![Ratings vs Love Counts](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/EDA/rating_vs_lovecount.png)
