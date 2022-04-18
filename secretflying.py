import requests
from bs4 import BeautifulSoup

# secret flying's canadian deals
source = requests.get('https://www.secretflying.com/canada-deals/').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

posts = soup.find_all('div', {'class':'article-content-wrapper entry-main-content'})

for post in posts:
    print(post.h2.text)