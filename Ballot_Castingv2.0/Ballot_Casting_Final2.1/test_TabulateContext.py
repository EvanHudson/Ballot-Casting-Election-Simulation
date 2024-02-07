import unittest
from TabulateContext import TabulateContext
from Election_Registry import ElectionRegistry
from TabulateContext import TabulateContext
from vote_object import Vote_Object

class TestTabulateContext(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        print('setUp')
        self.vote1 = Vote_Object(123,2,'president','federal')
        self.vote2 = Vote_Object(124,2,'senator','state')
        self.vote3 = Vote_Object(125,2, 'mayor', 'local')
        self.election_registry = ElectionRegistry()
        self.tabulate_context = TabulateContext(self.election_registry)
    


    def test_tabulate_vote_federal(self):
        print('test_federal')
        self.assertIsNone(self.tabulate_context.tabulate_vote(self.vote1.vote()))

    def test_tabulate_vote_state(self):
        print('test_state')
        self.assertIsNone(self.tabulate_context.tabulate_vote(self.vote2.vote()))

    def test_tabulate_vote_local(self):
        print('test_local')
        self.assertIsNone(self.tabulate_context.tabulate_vote(self.vote3.vote()))
    
    def test_tabulate_vote_mispellFail(self):
        print('test_fail_mispell')
        self.vote1.setelection_type('fed')
        self.assertIsNone(self.tabulate_context.tabulate_vote(self.vote1.vote()))


if __name__ == '__main__':
    unittest.main()
