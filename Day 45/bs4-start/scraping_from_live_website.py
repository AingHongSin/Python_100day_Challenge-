from bs4 import BeautifulSoup
import requests

respones = requests.get(url='https://news.ycombinator.com/newest')

yc_web_page = respones.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

#
# all_tag_storyLink = soup.find_all(name='a', class_='storylink')
# for tag in all_tag_storyLink:
#     print(tag.getText())

article_list = []
article_link = []

article_tag  = soup.find_all(name='a', class_='storylink')

for tag in article_tag:
    article_list.append(tag.getText())
    article_link.append(tag.get('href'))

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

heightest_upvote= max(article_score)

heightest_upvote_index = article_score.index(heightest_upvote)

print(article_list[heightest_upvote_index])
print(article_link[heightest_upvote_index])
print(article_score[heightest_upvote_index])
