# 导包
import os
import unittest
import logging
from api.login_api import LoginApi
import app
from utils import assert_common_utils, read_login_data  # 导入封装的通用断言函数
from parameterized import parameterized


class LoginConfig:
    # 在登录的配置类中增加HEADERS变量
    HEADERS = {"Content-Type": "application/json"}


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义要加载的登录数据的路径
    filename = app.BASE_DIR + "/data/login.json"

    @parameterized.expand(read_login_data(filename))
    def test01_login(self, case_name, jsonData, http_code, success, code, message):
        # 定义登录成功所需要的请求体
        jsonData = jsonData
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块)
        logging.info("登录的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, http_code, success, code, message)


