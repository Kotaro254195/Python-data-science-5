# import the required library
from bs4 import BeautifulSoup

# import the web scraping file which is 2.1.html
HTMLFILEPATH="2.1.html"
with open(HTMLFILEPATH,'r')as organization:
    soup=BeautifulSoup(organization, 'html.parser')

# view the contents from the soup
print(soup.contents)

print('-----------------------------------')
tag_li=soup.find('li')
print(tag_li)
print(type(tag_li))


print('-----------------------------------')
# select the 'HR' id
find_id=soup.find(id="HR")
print(find_id)


print('-----------------------------------')
print(find_id.div.string)


print('-----------------------------------')
# search for the perticular css attr
search_for_stringOnly=soup.find(text=['LOHITTTTT','KOTA'])
print(search_for_stringOnly)


print('-----------------------------------')
# search for the perticular css attr
search_for_stringOnly=soup.findAll(text=['LOHITTT','KOTA'])
print(search_for_stringOnly)
search_for_stringOnly=soup.findAll(text=['Lohit','KOTA'])
print(search_for_stringOnly)


print('-----------------------------------')
# to get the 'class' of ITmanager
css_class_search=soup.find(attrs={"class":"ITmanager"})
print(css_class_search)


print('-----------------------------------')
def is_account_manager(tag):
    return tag.has_attr('id') and tag.get('id')=="Finance"

is_sccount_manager=soup.find(is_account_manager)
# print(is_sccount_manager.li.div.string)
print(is_sccount_manager)


print('-----------------------------------')
for tag in soup.findAll(True):
    print(tag.name)


print('-----------------------------------')
# this step to get class of HRManager
# this is present as list

find_class=soup.findAll(class_='HRManager')
print(type(find_class))

# Now I'm printing the HRmanager Tag index of 9
print(find_class)
print()
print(find_class[0])


print('-----------------------------------')
find_class=find_class[0]
find_parent=find_class.find_parents('ul')
print(find_parent)


print('-----------------------------------')

findclasses=soup.findAll(class_='HRManager')
findparent=findclasses[2].find_parents('ul')
print(findparent)


print('-----------------------------------')
org=soup.find(id='IT')
print(org)
print()


print('-----------------------------------')
next_sibling=org.findNextSiblings()
print(next_sibling)


print('-----------------------------------')
all_previous=org.findPrevious()
print(all_previous)


print('-----------------------------------')
all_next=org.findAllNext()

print(all_next)


