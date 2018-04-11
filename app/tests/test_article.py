import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):
  '''
	Test Class to test the behaviour of the Article class
	'''
  def setUp(self):
    '''
    Set up that will run before every Test
    '''
    self.new_article = Articles("Palestinians evacuate the body of Palestinian journalist Yaser Murtaja, 31, who was shot and killed by an Israeli sharpshooter in the Gaza Strip on April 6, 2018 [Ibraheem Abu Mustafa/Reuters]"
 "https://www.aljazeera.com/news/","https://www.aljazeera.com/indepth/opinion/media-mass-deception-180409092703608.html/2018/06/1-lead-image.jpg","2018-06-21T11:00:53Z")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
	unittest.main(verbosity=2)
