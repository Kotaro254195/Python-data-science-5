store="""
<!DOCTYPE html

<html>
    <body>
        <div class="organizationlist">
            <ul id="HR">
                <li class="HRmanager">
                    <div class="name">Jack</div>
                    <div class="ID">101</div>
                </li>
                <li>
                    <div class="name">Daren</div>
                    <div class="ID">65</div>
                </li>
            </ul>
        </div>
    </body>
</html>
"""

from bs4 import BeautifulSoup as bs
soup=bs(store, 'html.parser')

tag_li=soup.findAll('li')

print(tag_li[0].find('div',attrs={'class':'name'}).string)
print(tag_li[0].find('div',attrs={'class':'ID'}).string)

print(tag_li[1].find('div',attrs={'class':'name'}).string)
print(tag_li[1].find('div',attrs={'class':'ID'}).string)