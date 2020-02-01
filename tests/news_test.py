import unittest
from app.models import Articles

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''
def setup (self):
    '''
    Set up method that will run before every test
    '''
    self.new_article = Articles('id','name','author','title','description','url','publicshedAt','urlToImage')
if __name__ == '__name__':
    unittest.main()