import unittest
from ..models import Quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1,'Anon','Lorem ipsum....','http://quotes.stormconsultancy.co.uk/quotes/1')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()

