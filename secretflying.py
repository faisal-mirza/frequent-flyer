import requests
from bs4 import BeautifulSoup
import re

# secret flying's canadian deals
source = requests.get('https://www.secretflying.com/canada-deals/').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

posts = soup.find_all('div', {'class':'article-content-wrapper entry-main-content'})

def search_pattern(pattern, string):
  result = re.search(pattern, string)
  return result

to_pattern = 'Toronto'

deal_list =[]

for post in posts:
    if search_pattern(to_pattern, post.h2.text):
        # deal_list.append(post.h2.text)
        print(post.h2.text)

# print(deal_list)