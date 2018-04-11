import unittest
from app.models import Source

class News_sourceTest(unittest.TestCase):
  """
  Test Class to test the behaviour of the News_source class
  """
  def setUp(self):
    """
    Set up tat will run before every Test
    """
    self.new_source =Source("bbc-sport","BBC SPORT", "The home of BBC Sport online.","http://www.bbc.co.uk/sport","sport")

  def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
  unittest.main(verbosity=2)
