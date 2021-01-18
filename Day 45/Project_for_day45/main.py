import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
html_index = response.text

soup = BeautifulSoup(html_index, 'html.parser')

all_of_title_move = soup.find_all(name='h3', class_='title')

title_movie_list = [movie.getText() for movie in all_of_title_move]
title_movie_list.reverse()

print(title_movie_list)

for title_movie in title_movie_list:
    with open(file='Top 100 Movie.txt', mode='a') as file:
        file.write(f"{title_movie}\n")
