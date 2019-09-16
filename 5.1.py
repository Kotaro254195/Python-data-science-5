from bs4 import BeautifulSoup
import requests

# simply add the website links

url='https://lohitbadiger.herokuapp.com'

# access the result through requests objects

store=requests.get(url)

# I'm checking the response of the website
print(store)

# load the page content
page_content=store.content
# print(page_content)


# create soup object
soup=BeautifulSoup(page_content,'html.parser')
# view the contents
print(soup)


print('__________________________________________')
print(soup.prettify())


print('__________________________________________')
# view the original encoding of the website
print(soup.original_encoding)


print('__________________________________________')
# format the tag a to xml
print(soup.body.a.prettify(formatter='xml'))


print('__________________________________________')
# define a custome function to convert string values to uppercase
def upperCaseFn(strt):
    return strt.upper()

print('__________________________________________')
# format using custom function for outputting string in 

print(soup.body.a.prettify(formatter=upperCaseFn))