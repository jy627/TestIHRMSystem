# 导包
import unittest
import logging

import app
from api.login_api import LoginApi
from utils import assert_common_utils

# class LoginConfig:
#     HEADERS = {"Content-Type": "application/json"}
# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_api = LoginApi()


    def tearDown(self):
        pass
    # 编写测试的函数
    # 登录成功
    def test01_login_success(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 定义请求头
        # HEADERS = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        # self.assertEqual(200, response.status_code)  # 与用例中文档的响应状态码进行比较断言
        # self.assertEqual(True, response.json().get("success"))  # 与用例文档中的返回json数据中的success的值进行比较
        # self.assertEqual(10000, response.json().get("code"))  # 与用例文档中返回json数据中的code进行比较
        # self.assertIn("操作成功", response.json().get("message"))  # 与用例文档中返回的json数据中的message进行比较
        assert_common_utils(self,response,200,True,10000,"操作成功")


    # 密码错误
    def test02_password_is_error(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "1234567"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13900000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

# 输入的手机号码有英文字符
    def test04_mobile_has_eng(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "138000A0X2", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "1380(*000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空:我们在学习阶段，以为断言失败就是代码写错了。但是实际工作中不是
    # 实际工作中，断言是帮我们测试接口有没有问题的一种技术，所以如果在排查自己技术问题之后
    # 如果断言失败了，那么说明这个接口的测试点有bug
    def test06_moible_is_empty(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_None(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": ""}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参-多出1个参数
    def test08_more_params(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456", "sign": "123"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 少参-缺少mobile
    def test09_less_mobile(self):
        # 定义登录成功所需要的请求体
        jsonData = {"password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test10_less_password(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参：无参案例传入None
    def test11_none_params(self):
        # 定义登录成功所需要的请求体
        jsonData = None
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mboile": "13800000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
