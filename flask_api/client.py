import requests

# #VIEW USERS
# url = "http://127.0.0.1:5000"
#
# response = requests.get(url)
#
# print('Status',response.status_code)
# print('Response',response.json())


# # #ADD USER
# url = "http://127.0.0.1:5000/adduser"
#
# data = {'name':'franky','email':'franky@gmail.com'}
#
# response = requests.post(url,json=data)
#
# print('Status',response.status_code)
# print('Response',response.json())

# #UPDATE USER
# url = "http://127.0.0.1:5000/updateuser"
#
# data = {'email': 'yasof@gmail.com', 'id': 11, 'name': 'yasof'}
#
# response = requests.put(url,json=data)
#
# print('Status',response.status_code)
# print('Response',response.json())

#DELETE USER
url = "http://127.0.0.1:5000/deleteuser"

data = {'email': 'franky@gmail.com', 'id': 11, 'name': 'franky'}

response = requests.delete(url,json=data)

print('Status',response.status_code)
print('Response',response.json())


