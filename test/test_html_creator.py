import unittest
from html_creator import CreateHtml

class TestCreateHtmlClass(unittest.TestCase):

    def setUp(self):
        self.html_creator = CreateHtml()

    def test_simple_method(self):

        self.assertEqual(self.html_creator.simple(h1='test1', b = 'test1', p = 'test1').html,
            '<h1>test1</h1><b>test1</b><p>test1</p>')
        
        self.html_creator.html = ''
        
        self.assertEqual(self.html_creator.simple(test='test').html,
            '<test>test</test>')

if __name__ == '__main__':
    unittest.main()