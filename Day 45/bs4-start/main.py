from bs4 import BeautifulSoup


with open('website.html') as file:
    contects = file.read()

soup = BeautifulSoup(contects, 'html.parser')

# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify)
# print(soup.a)

all_anchor_tag = soup.find_all(name='a')
# print(all_anchor_tag)

# for tag in all_anchor_tag:
#     print(tag.getText())

# heading = soup.find(name='h1', id='name')
# print(heading)

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

