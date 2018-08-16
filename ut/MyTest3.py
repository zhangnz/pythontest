import unittest
import xmlrunner
#导入这个模块
class MyTest3(unittest.TestCase):

    def test1(self):
        print('dddd')

    def test2(self):
        print('cccc')

    def test3(self):
        print('eeee')

    def test4(self):
        self.assertEqual(1,2)
    # def test1(self,a,b,c):
    #     print(a, b, c)
    #     self.assertEqual(a+b,c)

if __name__=='__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(MyTest3))
    runner = xmlrunner.XMLTestRunner(output='report')#指定报告放的目录
    runner.run(test_suite)