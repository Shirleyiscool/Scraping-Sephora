import re
import pandas as pd
import json

with open('data/scraper_result.json') as f:
    result = json.load(f)

# Load product link data frame
pd_links_df = pd.read_csv('data/product_links.csv')
# Add a column of product id
pd_links_df['pd_id'] = [re.findall('P[0-9]{4,7}', link)[0] for link
                        in pd_links_df['product_links']]

# Save product data into data frame
for pid, value in result.items():
    product_result = value[0]
    if len(product_result) == 0:
        continue
    try:
        product_result = product_result[pid]
    except KeyError:
        for k, v in product_result.items():
            product_result = v

    pd_names = ['Name', 'Description']
    for name in pd_names:
        try:
            pd_links_df.loc[pd_links_df['pd_id'] ==
                            pid, name] = product_result[name]
        except KeyError:
            continue

    rating_names = ['AverageOverallRating', 'FirstSubmissionTime',
                    'LastSubmissionTime']
    for name in rating_names:
        try:
            pd_links_df.loc[pd_links_df['pd_id'] == pid,
                            name] = product_result['ReviewStatistics'][name]
        except KeyError:
            continue
    # 'age'
    try:
        age_data = \
            product_result['ReviewStatistics']['ContextDataDistribution'][
                'age'][
                'Values']
        for age_group in age_data:
            pd_links_df.loc[pd_links_df['pd_id'] == pid,
                            f'Age_{age_group["Value"]}'] = age_group['Count']
    except KeyError:
        continue

pd_links_df.to_csv('data/product_data.csv', index=False)

# Save review data into data frame
reviews_dic = {'pd_id': [], 'AuthorId': [], 'Rating': [], 'Title': [],
               'ReviewText': [], 'Helpfulness': [], 'SubmissionTime': [],
               'IsRecommended': [], 'eyeColor': [], 'hairColor': [],
               'skinTone': [], 'skinType': []}

for pid, value in result.items():
    reviews_data = value[1]
    if len(reviews_data) == 0:
        continue

    for review in reviews_data:
        reviews_dic['pd_id'].append(pid)

        # Add review characteristics
        review_names = ['AuthorId', 'Rating', 'Title', 'ReviewText',
                        'Helpfulness', 'SubmissionTime', 'IsRecommended']
        for name in review_names:
            try:
                reviews_dic[name].append(review[name])
            except KeyError:
                reviews_dic[name].append(None)

        # Add users' characteristics
        attr_name = ['eyeColor', 'hairColor', 'skinTone', 'skinType']
        for name in attr_name:
            try:
                reviews_dic[name].append(
                    review['ContextDataValues'][name]['Value'])
            except KeyError:
                reviews_dic[name].append(None)

review_df = pd.DataFrame(reviews_dic)
review_df.to_csv('data/review_data.csv', index=False)
