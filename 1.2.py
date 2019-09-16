from bs4 import BeautifulSoup as bs

store="""
<!DOCTYPE html

<html lang="en">
    <head>
        <meta charset="UTF-8">

        <title>This is 2nd one</title>
    </head>


    <body>
        <p class="new">Lohit</p>
        <h1 class="new">Lohit Badiger </h1>

        <h2>London</h2>
        <h2>Mumbai</h2>

        <b> <!--"New Comment line"--> </b>
    </body>
</heml>
"""

soup=bs(store, 'html.parser')
print('------------print html code-------------')
print(soup)

print('------------print p_tag.string---------------')
tag1=soup.p
print(tag1.string)

print('------------print h1_tag.string---------------')
tag2=soup.h1
print(tag2.string)

print('------------print b_tag comment-----------')
tag3=soup.b
print(tag3)
