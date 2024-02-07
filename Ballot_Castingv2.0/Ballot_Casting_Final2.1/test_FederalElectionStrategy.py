import unittest
from vote_object import Vote_Object
from Election_Registry import ElectionRegistry
from FederalElectionStrategy import FederalElectionStrategy

class TestFederalElectionStrategy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')
        

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        print('setUp')
        self.vote1 = Vote_Object(123,1,'president','federal')
        self.vote2 = Vote_Object(124,2,'senator','state')
        self.vote3 = Vote_Object(125,2, 'mayor', 'local')
        self.election_registry = ElectionRegistry()
        self.local1 = FederalElectionStrategy(self.election_registry)

    def tearDown(self):
        print('tearDown\n')

    def test_verify(self):
        print('test_verify')
        self.assertFalse(self.local1.verify(self.vote3.vote()))
        self.assertTrue(self.local1.verify(self.vote1.vote()))
        self.assertTrue(self.local1.verify(self.vote2.vote()))

        self.vote1.setposition('mayor')
        self.vote1.setelection_type('local')
        self.assertFalse(self.local1.verify(self.vote1.vote()))



if __name__ == '__main__':
    unittest.main()
