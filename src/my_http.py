import http.client
import json
# connect.request('GET', '/posts')
# response = connect.getresponse()
# print (response.status, response.reason)
#
# data = response.read().decode()
# print(data)
#
# headers = response.getheaders()
#
# [print (x) for x in headers]

# *********запрос на отправку ****************
# datas = json.dumps({'nameUser':'Ivan'})
# types = {'ContentTpe': 'application/Myjson'}
# connect = http.client.HTTPConnection ('jsonplaceholder.typicode.com')
# # connect.request('GET', '/posts')
# connect.request('POST', '/posts', body=datas, headers=types)
# response = connect.getresponse()
# print (response.status, response.reason)
# data = response.read().decode()
# print(data)
# connect.close()

# *********запрос на получение*********
# connect = http.client.HTTPConnection ('jsonplaceholder.typicode.com')
# connect.request('GET', '/posts/101')
# response = connect.getresponse()
# print (response.status, response.reason)
# data = response.read().decode()
# print(data)
# connect.close()
#
#


# connect = http.client.HTTPConnection ('jsonplaceholder.typicode.com')
# connect.request('GET', '/posts')
#
# # print (response.status, response.reason)
# # data = response.read().decode()
# # print(data)
# headers = response.getheaders()
# [print(x) for x in headers]
# connect.close()
#

# loop ***********GET
connect = http.client.HTTPConnection ('localhost:3000')
connect.request('GET', '/users')
response = connect.getresponse()
print (response.status, response.reason)
data = response.read().decode( "utf-8")
# data_to_print = json.loads(data)# print (data)
print (data)
connect.close()

# # loop ***********POST
# data = {
#       "id": 4,
#       "name": "Abac",
#       "email": "ivan.ivanov@example.com",
#       "age": 40
#     }
# data_to_serv = json.dumps(data)
# connect = http.client.HTTPConnection ('localhost:3000')
# connect.request('POST', '/users', data_to_serv)
# response = connect.getresponse()
# print (response.status, response.reason)
# data = response.read().decode( "utf-8")
# # data_to_print = json.loads(data)# print (data)
# print (data)
# connect.close()

