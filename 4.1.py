
school="""
<address>

    <head>
        <title>This is spiceup academy</title>
    </head>

    <body>       

        <schools>
            <p>
                <b>This is located in the heart of Banglore city Koramangala</b>

            </p>
            <classrooms>
                <classroom id="555F">
                    <teacher>Lohit</teacher>
                    <subject>Python and Machine Learning</subject>
                    <dob>30-10-2019</dob>
                    <date>10-10-2019</date>
                    <review>Amazing story ahead</review>
                </classroom>

                <good id="666F">
                    <teacher>Susumu</teacher>
                    <subject>Php and python</subject>
                    <dob>02-10-2010</dob>
                    <date>03-20-1099</date>
                    <review>This is in the banglore</review>
                </good>

                <bad id="777F">
                    <teacher>Kotya</teacher>
                    <subject>Ruby on Machine Learning</subject>
                    <dob>20-20-1000</dob>
                    <date>20-101-00</date>
                </bad>

            </classrooms>
        </schools>
    </body>
</address>
"""

from bs4 import BeautifulSoup as bs
ss=bs(school,'html.parser')
print("___________________________________________")

print(ss.contents)

print("___________________________________________")
print(ss.address)

print("___________________________________________")
print(ss.head)
print()
print(ss.head.title)

print("___________________________________________")
#navigate down:in this im using descendants to get next tag
for me in ss.head.descendants:
    print(me)

print("___________________________________________")
# this will go to the next tag
# here there is no tag in after the <teacher> Tag so this will give me string
for me in ss.teacher.descendants:
    print(me)

print("___________________________________________")
# navigate down usinig the stripped string method

# now we will get string value present inside the html documents
for string in ss.stripped_strings:
    print(repr(string))

print("___________________________________________")
for vwq in ss.stripped_strings:
    print(vwq)

print("___________________________________________")
print(ss.head.title.parent)

print("___________________________________________")
navigate_up=ss.subject
print(navigate_up)

print("___________________________________________")
back_and_forth=ss.address.bad
ok=next_element=back_and_forth.next_element.next_element
print(ok)