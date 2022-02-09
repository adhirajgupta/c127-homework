from bs4 import BeautifulSoup
from jinja2 import Undefined
import pandas
import requests
from pprint import pprint

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url).text
# print(page)

soup = BeautifulSoup(page,'html.parser')

table = soup.find('table')
tr1 = table.tr
# print(tr1)

th_tags = tr1.find_all('th')
# print(th_tags)


value_headers = []

for value in th_tags:
    try:
        header = value.find('a').text.rstrip('\n')
        # print(header)
        if(header):
            value_headers.append(header)
    except AttributeError:
        header2 = value.text.rstrip('\n')
        # print(header2)
        if(header2):
            value_headers.append(header2)

value = []

# print(value_headers)
value_headers.pop(0)
# value.append(value_headers)

tbody = table.find('tbody')
tr2 = tbody.find_all('tr')
tr2.pop(0)
# pprint(tr2[0])


for tr in tr2:
    td_tags = tr.find_all('td')
    # pprint(td_tags)
    value_table = []
    for td in td_tags:
        try:
            value1 = td.find('a').text.rstrip('\n')
            # pprint(value1)
            value_table.append(value1)
        except IndexError:
            value2 = td.contents[1]
            # pprint(value2)
            value_table.append(value2)
        except AttributeError:
            value3 = td.text.rstrip('\n')
            # pprint(value3)
            value_table.append(value3)
    value_table.pop(0)
    # print(value_table)
    value.append(value_table)
    
    

print(value_headers)

df = pandas.DataFrame(value,columns=value_headers)
df.to_csv('base.csv',index=False,)