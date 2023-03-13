# import requests
#
#
#
# class TestRequests:
#     access_token = ""   # 类变量
#
#     def test_login(self):
#         url = "http://47.242.107.138:9090/home/login"
#         json = {
#             "email": "100@test.com",
#             "password": "111111",
#             "systemName": "ios"
#         }
#         res = requests.post(url=url, json=json)
#         return_data = res.json()
#
#         # access_token = return_data['data']['token']       # 字典获取元素，与json不同，不能..获取，只能一层一层的从对象获取
#         self.access_token = return_data.get('data').get('token')
#         # 字典获取token元素  {'code': 200, 'msg': '操作成功!', 'data': {'token': 'app_token:100:968df295908f4628ad797daaf80c9de6'}}
#         print(self.access_token)
#         code = return_data.get('code')
#         # print(code)
#         # print(return_data)
#         # print(res.request.headers)
#
#     def test_weituo(self):
#         self.test_login() # 将对象统一，通过self.test_login()调用给self对象，使得三个方法的对象都是登录本身
#         url = "http://47.242.107.138:9090/trusteeship"
#         headers = {
#             "token": self.access_token
#         }   # token依赖于test_login方法的return_data的返回的token，
#         # 所以需要在第一个接口里面，得到他的返回值之后，取得token的key，通过他的key去传value，
#         # 通过value的值赋值给全局变量access_token，通过类名来访问
#         res = requests.get(url=url, headers=headers)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#         # print(res.text)                # 响应的字符串格式的数据
#         # print(res.content)             # 响应的bytes字节类型格式的数据
#         # print(res.json())              # 响应json字典格式
#         # print(res.status_code)         # 响应状态码
#         # print(res.reason)              # 响应状态信息
#         # print(res.cookies)             # 响应的cookie信息
#         # print(res.headers)             # 响应头
#         # # 以上都是响应信息
#         # print(res.request.headers)     # 请求信息  请求头
#
#     def test_file(self):
#         self.test_login()
#         url = "http://47.242.107.138:9090/myhome/uploadHeadImage"
#         data = {
#             "file": open(r"E:\33\aa.jpg", "rb")
#         }
#         headers = {
#             "token": self.access_token   # 自负床用“”， 不用“”的是变量
#         }
#         res = requests.post(url=url, files=data, headers=headers)
#         return_data = res.json()
#         print(return_data)
#         print(res.request.headers)
#
