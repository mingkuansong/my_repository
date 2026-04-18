import time
import unittest

from run.BSTestRunner import BSTestRunner


def runner():
    # 测试用例目录
    case_dir = '../testcase'
    # 测试报告目录
    report_dir = '../reports'

    # 给测试报告命名
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_name = report_dir + '/' + now + '_test_report.html'

    # 筛选用例
    testcase = unittest.defaultTestLoader.discover('../testcase', pattern='*_test.py')

    # 执行用例，生成报告
    with open(report_name, 'wb') as f:
        my_runner = BSTestRunner(stream=f, title='我的测试报告', description='腾讯QQapp')
        my_runner.run(testcase)

if __name__ == '__main__':
    runner()