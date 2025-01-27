import requests
from bs4 import BeautifulSoup
# # # import json
# # # # params = {"userId" : 1}
response = requests.get('https://javarush.com/quests/lectures/ru.javarush.python.core.lecture.level13.lecture07')
# # # #
soup = BeautifulSoup (response.text, 'html.parser')
print (response.status_code)
# # # #
print(soup)
# # #
# # # print(response.json())
# # # #
# # #
# # # data = {"useName":"Cu-cu"}
# # # data_json = json.dumps(data)
# # #
# # # # response = requests.post ('https://jsonplaceholder.typicode.com/posts', json = data_json)
# # # # print (response.status_code)
# # # # response = requests.get ('https://jsonplaceholder.typicode.com/posts')#
# # # # print (response.json ())
# # #
# # # # response  = requests.put ('https://jsonplaceholder.typicode.com/posts/1', data_json)
# # # # print (response.status_code)
# # #
# # # response = ''
# # # try:
# # #     response = requests.get('https://kost-droid.github.io/Inet_test/1')
# # #     response.raise_for_status()
# # # except requests.exceptions.HTTPError as err:
# # #     print(f'Wrong {err}')
# # # except Exception as err:
# # #     print(err.args)
# # # else:
# # #     print (response.reason)
# # #     print (response.headers ['expires'])
# # #     print (response.content)
# # import requests
# #
# # params = {'key1': 'value1', 'key2': 'value2'}
# # response = requests.get('https://httpbin.org/get', params=params)
# # print(response.url)
#
#
# import requests
#
# data = {
#     'username': 'example1000',
#     'password': 'password'
# }
# response = requests.get ('https://httpbin.org/post')
# print (response.content [100])
# # response = requests.post('https://httpbin.org/post', data=data)
# # print(response.json())
#
# import requests
# import os
#
# # file = open ('example.txt', 'w')
# # file.write('Hi !!!')
# # file.close()
# #
# # files = {'files': open ('example.txt' , 'rb')}
# #
# # response = requests.post ('https://httpbin.org/post', files=files)
# # print (response.json())
# response = requests.get ('https://httpbin.org/post')
# print (response.json())

