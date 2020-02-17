import requests

import re

URL = 'https://courses.engr.illinois.edu/ece498icc/sp2020/lab1_string.php'
name = "Johan"
netid = "jmufuta2"

my_data = {
    'netid': netid,
    'name': name
}

r = requests.post(url=URL, data=my_data)

my_text = r.text

#(i*i for i in range(10)

my_message = [my_text[i*498] for i in range(400)]
# for value in find_text(my_text):
#     my_message += value
secret = " "

print(secret.join(my_message))