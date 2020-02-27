import unittest

from project import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"hello":"world"}\n')

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/route_not_exist', content_type='html/text')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
