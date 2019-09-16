from bs4 import BeautifulSoup 
from urllib.request import urlopen

url='https://www.simplilearn.com/resources'

webpage=urlopen(url)
sl_soup=BeautifulSoup(webpage,'html.parser')
webpage.close()
# print(sl_soup.contents)

# print(sl_soup.prettify())


print('_______________________________________________')
print(sl_soup.title)

print('_______________________________________________')
for href in sl_soup.findAll('a',href=True):
    print(href['href'])


print('_______________________________________________')
for h2 in sl_soup.findAll('h2'):
    print(h2.string)


print('_______________________________________________')

url2='https://www.simplilearn.com/what-is-tensorflow-article?source=frs_home'
webpage2=urlopen(url2)
sl_article=BeautifulSoup(webpage2,'html.parser')

test=sl_article.find(class_='desig_author empty-text')
print(type(test))
print(test.findAll('p'))


print('_______________________________________________')
first_next_p=test.p
print(first_next_p)

print('_______________________________________________')
find_next_sibling=first_next_p.next_sibling.next_sibling
print(find_next_sibling)