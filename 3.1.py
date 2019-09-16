# I'm goone run this part in jupyter

from bs4 import BeautifulSoup
import re

email_example="""
abc@emailgmail.com
"""

soup_email=BeautifulSoup(email_example,"lxml")
email_ID_regexp=re.compile("\w+@\w+\.\w+")
email_id=soup_email.find(text=email_ID_regexp)
print(email_id)