from bs4 import BeautifulSoup

html_doc="""<!DOCTYPE html>
<html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, inital-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="chorm">

        <title> Kotaro Website Document</title>
        </head>
<body>
        <h1> Heading Tag</h1>
            <b>""This is 'comment' l""</b>

            <p title="This is about me" class="test">My first website web scrape</p>
                <div class="cities">
                <h2>London</h2>
                <h2>Mumbai</h2>

                </div>

</body>
</html>"""

soup=BeautifulSoup(html_doc, 'html.parser')
print('-------------Type of the soup---------------')
print(type(soup))

print("-------print the soup ----------")
print(soup)

print("----------print tag--------------")
tag=soup.p
print(tag)

print('-------------Type of the comment---------------')
comment=soup.b.string
print(type(comment))

print('------------im printing comment')
print(comment)

print('------------print comment by slicing ---------')
print(comment[0:])
print('-----------------------------------')
print(comment[0:10])
print('-----------------------------------')
print(comment[0:10:2])

print('---------------print tag.string----------------')
print(tag.string)

print('---------------print tag.attrs---------------')
print(tag.attrs)

