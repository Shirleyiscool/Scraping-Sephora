# Sephora Product Analysis
  - Start date: 02/2019
  - For education: FE 290 - Data and Programming for Analytics @ UCI
  - Author: Shirley Li

# About the project
This project is for the group work of class FE290 during my accounting master study at UCI.
I am the person who is responsible to scape the data and do analysis. This project is just for education.
After my study in MSDS program at USF, I decided to optimize the codes and improve my programming skills
at the same time. So I try to optimize the codes during the winter break in 12/2019. However, there are sill
some things to improve but that would take some time. So this project is going to be updated from time to time.

# Scraping data from Sephora
Here are some steps to scape the product information.

## Step 1: Get all the brand links and product links from Sephora and save them into text file.

From Sephora's Brand list website, we can scrape all the brand links.
![brand list screenshot](https://github.com/Shirleyiscool/Scraping-Sephora/blob/master/image/brand_list_screenshot.png)

### Step 2: Get product information from each product links and save them into Excel file.

### Notes:
   1) Not all the information can be obtained as some products have different page design. Therefore, beautiful soup has limits to scrape the data. In this current version, I just simply use na to replace those information that is null or goes error.
   2) Reviews are not obtained for the current version.
   3) Data analytics was simple when I did this project. Coding for this part will be uploaded later.
