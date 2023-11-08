# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
#这里需要导入测试文件
#import test_login
import youdao
testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
#testunit.addTest(unittest.makeSuite(test_login.do_test))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
# #执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)
# 定义个报告存放路径，支持相对路径
filename = 'result.html'
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行详情:：')
#执行测试用例
runner.run(testunit)
