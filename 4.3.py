from bs4 import BeautifulSoup as bs

data_SL="""
<ul class="content-col discover">
    <h5>discover</h5>
    <li><a href="/resources"></a></li>
    <li><a href="/http://community.simplilearn.com/" id="users">Free Resources</a></li>
    <li><a href="career-data-labs" id="lab">Career Data labs</a></li>
    <li><a href="/scholarships-for-veterans" id="scholarship"></a></li>
    <li><a href="http://www.simplilearn.com/feed/" id="rss">RSS FEED</a></li>
</ul>
"""

soup_SL=bs(data_SL,'html.parser')
# If I do this I get all info
print(soup_SL)

print("______________________________________")
print(soup_SL.get_text())


print("______________________________________")
from bs4 import SoupStrainer

tags_with_lablink=SoupStrainer(id='lab')

print(bs(data_SL,'html.parser',parse_only=tags_with_lablink))

print("______________________________________")
print(bs(data_SL,'html.parser',parse_only=tags_with_lablink).prettify())