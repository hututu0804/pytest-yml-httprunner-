import requests
import pytest
import json
from common.yaml_tool import read_testcase_file
from common.requests_tool import RequestsTool


class TestRequests:
    # access_token = ""   # 类变量

    @pytest.mark.parametrize('caseinfo', [read_testcase_file('/testcases/get_token.yml')])
    # 数据驱动---@pytest.mark.parametrize(参数名称,参数值)
    # 装饰器可以实现用例参数化,实现自定义参数名称，并进行传入参数数据; 参数为列表中嵌套字典则需要加[]/或者在yaml_tool里面读取文件时，
    # 返回的值加上：return value[]
    def test_login(self, caseinfo):
        RequestsTool('base', 'ceshi_url').analysis_yaml(caseinfo)  # 调用analysis_yml方法，初始化对象调用，实例类
        pass

    # @pytest.mark.parametrize('caseinfo', [read_testcase_file('/testcases/recharge.yml')])
    # def test_weituo(self, caseinfo):
    #     RequestsTool('base', 'ceshi_url').analysis_yaml(caseinfo)
        pass

    @pytest.mark.parametrize('caseinfo', [read_testcase_file('/testcases/sc_files.yml')])
    def test_files(self, caseinfo):
        RequestsTool('base', 'ceshi_url').analysis_yaml(caseinfo)
        pass
    #     url = "http://47.242.107.138:9090/home/login"
    #     json = {
    #         "email": "100@test.com",
    #         "password": "111111",
    #         "systemName": "ios"
    #     }
    #     res = requests.post(url=url, json=json)
    #     return_data = res.json()
    #
    # # access_token = return_data['data']['token']       # 字典获取元素，与json不同，不能..获取，只能一层一层的从对象获取 self.access_token =
    # return_data.get('data').get('token')
    # print(code) # print(return_data) # print(res.request.headers)
    #
    # def test_weituo(self):
    #     self.test_login() # 将对象统一，通过self.test_login()调用给self对象，使得三个方法的对象都是登录本身
    #     url = "http://47.242.107.138:9090/trusteeship"
    #     headers = {
    #         "token": self.access_token
    #     }   # token依赖于test_login方法的return_data的返回的token，
    #     # 所以需要在第一个接口里面，得到他的返回值之后，取得token的key，通过他的key去传value，
    #     # 通过value的值赋值给全局变量access_token，通过类名来访问
    #     res = requests.get(url=url, headers=headers)
    #     return_data = res.json()
    #     print(return_data)
    #     print(res.request.headers)
    #
    # def test_file(self):
    #     self.test_login()
    #     url = "http://47.242.107.138:9090/myhome/uploadHeadImage"
    #     data = {
    #         "file": open(r"E:\33\aa.jpg", "rb")
    #     }
    #     headers = {
    #         "token": self.access_token   # 自负床用“”， 不用“”的是变量
    #     }
    #     res = requests.post(url=url, files=data, headers=headers)
    #     return_data = res.json()
    #     print(return_data)
    #     print(res.request.headers)
    #
