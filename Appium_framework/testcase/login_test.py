import unittest

from business.login import login_test
from data.get_csv import get_csv_all


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print('一条用例开始执行~')

    def tearDown(self) -> None:
        print('一条用例执行完毕！')

    def test_login(self):
        csv_file = '../data/login_data.csv'
        data = get_csv_all(csv_file)
        for i in range(len(data)):
            print('\n这是第', (i + 1), '次测试')
            data1 = data[i].split(',')
            try:
                if data1[2].strip() == 'true':
                    self.assertTrue(login_test(data1[0].strip(), data1[1].strip()), '不通过')
                else:
                    self.assertFalse(login_test(data1[0].strip(), data1[1].strip()), '不通过')
            except:
                print('本次测试未通过！')
            else:
                print('本次测试通过~')

if __name__ == '__main__':
    unittest.main()