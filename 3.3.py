from bs4 import BeautifulSoup as bs

# create the document
book_shop_doc="""

<catelog>
    <head> <title>The web book catelog</title></head>
        <p class="title"> <b>The Book Catelog</b></p>

        <books>
            <book id="bk001">
                <Author>hightTower</Author>
                <genre>Fiction</genre>
                <price>44.30</price>
                <pub_data>2000-10-10</pub_data>
                <review> An amazing story of nothing</review>
            </book>

            <book id="bk002">
                <author>nagata, Suanne</author>
                <title>Becoming somebody</title>
                <genre>Biograpy</genre>
                <review>A master Piece o the art</review>
            </book>

            <book id="bk003">
                <author>Oberg,Bruce</author>
                <title>The Poet's First Poem</title>
                <genre>Poem</genre>
                <price>29.3</price>
                <review>The lease Poetic Poems</review>
            </book>
        </books>
</catelog>
"""

#create a soup objects
book_soup=bs(book_shop_doc,'html.parser')

# print the catelog tag
print(book_soup)

print("___________________________________________")
# create a sup objects
print(book_soup.catelog)

print("___________________________________________")
print(book_soup.head)

print("___________________________________________")
title_tag=book_soup.title
print(title_tag)

print("___________________________________________")
# navigate down the dexcendants and print dem
for descen in book_soup.head.descendants:
    print(descen)

print("___________________________________________")
# navigate down using stripped string method
for strip in book_soup.stripped_strings:
    print(repr(strip))
# repr is almost same with str


print("___________________________________________")
# navigating up using the parent method
print(title_tag.parent)

print("___________________________________________")
element_soup=book_soup.catelog.books
print(element_soup)

print("___________________________________________")
next_element=element_soup.next_element.next_element
# next_element や previous_elementなどは２つでセット
print(next_element)


print("___________________________________________")
previous_element=next_element.previous_element.previous_element
print(previous_element)

print("___________________________________________")
next_sibling=book_soup.catelog.books.book
print(next_sibling)