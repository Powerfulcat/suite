import time
import unittest

from demo2.tools.HTMLTestReportCN import HTMLTestRunner


def main():
    # suite = unittest.TestSuite()
    # # suite.addTest(MyTest("a"))
    # # suite.addTest(MyTest("b"))
    # # 另外一种方法(添加整个类中的方法)
    # suite.addTest(unittest.makeSuite(IwebShopTest))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # =================批量添加========================
    test_dir = "../cases/"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="mytest*.py")

    # 报告存放路径
    report_dir = '../reports/'
    # 获取当前时间
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # 准备报告名称
    report_name = report_dir + now_time + 'Report.html'
    # 开始报告写入文件流
    with open(report_name, 'wb') as f:
        # 初始化报告生成的执行对象
        '''
        stream=:开启的报告文件写入流
        verbosity=:测试执行后的打印格式(默认值为1,可选2,2显示的信息更详细,推荐使用!)
        title=:生成的报告内的标题(可选)
        description=:测试相关环境描述信息(可选)
        '''
        # 英文模板调用
        # runner = HTMLTestRunner(stream=f, verbosity=1, title='iWebShop登录逻辑测试报告',
        #                         description='测试平台:macOS 测试浏览器:Firefox 版本:v35.0.1 测试人:QA')

        # 中文模板调用
        runner = HTMLTestRunner(stream=f, verbosity=2, title='百度登录逻辑测试报告',
                                description='测试平台:macOS 测试浏览器:Firefox 版本:v35.0.1', tester='test03QA')

        runner.run(discover)


if __name__ == '__main__':
    main()
