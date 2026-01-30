import requests

# #VIEW USERS
url = "http://127.0.0.1:5000"

response = requests.get(url)

print('Status',response.status_code)
print('Response',response.json())


# # #ADD USER
# url = "http://127.0.0.1:5000/adduser"
#
# data = {'name':'franky','email':'franky@gmail.com'}
#
# response = requests.post(url,json=data)
#
# print('Status',response.status_code)
# print('Response',response.json())

#UPDATE USER
url = "http://127.0.0.1:5000/updateuser"

data = {'id':10,'name':'akainu','email':'akainu@gmail.com'}

response = requests.put(url,json=data)

print('Status',response.status_code)
print('Response',response.json())


