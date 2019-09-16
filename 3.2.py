from bs4 import BeautifulSoup as bs

htmlfile="3.1.html"
with open(htmlfile,"r")as organization:
    soup=bs(organization, 'html.parser')

print(soup.contents)

print("---------------------------------------------")
table=soup.find("table")
print(type(table))

print("---------------------------------------------")
print(table)

print("---------------------------------------------")
table=soup.find(id="name")
print(table)

print("---------------------------------------------")
print(table.find(id="lohit").string)
# same way
print(table.tr.td.string)

print("---------------------------------------------")
print(table.find(attrs={"class":"lo"}))


print("---------------------------------------------")
search=soup.findAll(text=["whitefield","Bangalore"])
print(search)