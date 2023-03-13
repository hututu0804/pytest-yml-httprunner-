# import requests
# from common.requests_tool import RequestsTool
#
#
# class TestRequests:
#     session = requests.session()  # 初始化一个session的对对象-----获得请求的session会话对象
#
#     def test_logins(self):
#         url = "/home/login"
#         json = {
#             "email": "100@test.com",
#             "password": "111111",
#             "systemName": "ios"
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         #'base', 'ceshi_url' 传入这个值，不同的基础路径，就可以获得不同基础路径
#         # res = TestRequests.session.request("post", url=url, json=json)   # 发送请求，通过session发送
#         return_data = res.json()
#         # access_token = return_data.get('data').get('token')
#         access_token = return_data['data']['token']
#         RequestsTool('base', 'ceshi_url').session.headers.update({'token': access_token})   # 因为封装了方法，所以这里实例化RequestsTool()
#         # 往请求头里面设置参数，后续请求头就不需要加token，等于说先调登录接口，然后将token传入到请求头里面
#         print(access_token)
#         print(return_data)
#         print(res.request.headers)
#
#     def test_files(self):
#         url = "/myhome/uploadHeadImage"
#         data = {
#             "file": open(r"E:\33\aa.jpg", "rb")
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, files=data)
#         # res = TestRequests.session.request("post", url=url, files=data)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_put(self):
#         url = "/trusteeship/recharge"
#         json = {
#             "amount": 100
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_take(self):
#         url = "/trusteeship/withdrawal"
#         json = {
#             "amount": 100
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_weituo(self):
#         url = "/trusteeship"
#         res = RequestsTool('base', 'ceshi_url').send_request('get', url)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_revise(self):
#         url = "/myhome/modifyUserDetail"
#         json = {
#             "nickName": "胡图图",
#             "autograph": "胡图图的个性签名"
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_detailed(self):
#         url = "/wallet/billDetails"
#         json = {
#             "type": "-1",
#             "yearMonth": "-1",
#             "currentPage": 1,
#             "pageSize": 5,
#             "init": "true"
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
#     def test_revise(self):
#         url = "/myhome/modifyUserDetail"
#         json = {
#             "nickName": "胡图图",
#             "autograph": "胡图图的个性签名"
#         }
#         res = RequestsTool('base', 'ceshi_url').send_request('post', url, json=json)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)