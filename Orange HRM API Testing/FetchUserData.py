import requests

url ="https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
response = requests.get(url, auth=('admin', 'admin123'))
print(response.status_code)
print(response.text)


