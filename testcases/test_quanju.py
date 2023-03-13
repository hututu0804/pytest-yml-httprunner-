# import requests
# from common.yaml_tool import write_extract_file
# from common.yaml_tool import read_extract_file
#
# class TestRequests:
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
#         # print(return_data)
#         # 把中间变量写入extract.yml文件
#         extract_data = {"token": return_data['data']['token']}
#         write_extract_file(extract_data)
#     #
#     def test_weituo(self):
#         #self.test_login()  # 将对象统一，通过self.test_login()调用给self对象，使得三个方法的对象都是登录本身
#         url = "http://47.242.107.138:9090/trusteeship"
#         headers = {
#             "token": read_extract_file("token")
#         }
#         res = requests.get(url=url, headers=headers)
#         return_data = res.json()
#         print(return_data)
#         # print(res.request.headers)     # 请求信息  请求头
#     #
#     # def test_file(self):
#     #     self.test_login()
#     #     url = "http://47.242.107.138:9090/myhome/uploadHeadImage"
#     #     data = {
#     #         "file": open(r"E:\33\aa.jpg", "rb")
#     #     }
#     #     headers = {
#     #         "token": self.access_token   # 字符串用“”， 不用“”的是变量
#     #     }
#     #     res = requests.post(url=url, files=data, headers=headers)
#     #     return_data = res.json()
#     #     print(return_data)
#     #     print(res.request.headers)
#     #
