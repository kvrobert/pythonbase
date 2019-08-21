# File object

#f = open('test.txt', 'r')

import requests

with open('test.txt', 'r') as f:

    SIZE_TO_READ = 250


    f_content = f.read(SIZE_TO_READ)
    print(f.name)
    print(f_content)
#
    #    while len(f_content) > 0:
    #        print(f_content, end='')
#   f_content = f.read(SIZE_TO_READ)

payload = {'param1': 10, 'param2': "this is the second param"}
payload_post = {'lang': 'hun', 'content': "Some of text to use REX to extract entities"}

r = requests.get('http://httpbin.org/get?age=10&seconds=hello')
r2 = requests.get('http://httpbin.org/get', params=payload)
r_post = requests.post( 'http://httpbin.org/post', data=payload_post)


#print(r.text)
#print(r2.text)

r_dict = r_post.json()
print(r_dict["form"])

#print(r.url)
#print(r2.url)