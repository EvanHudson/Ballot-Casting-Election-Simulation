import unittest
from vote_object import Vote_Object

class TestVoteObject(unittest.TestCase):

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
    


    def test_setvoter_id(self):
        print('test_setvoter_id')
        self.assertEqual(self.vote1.voter_id, 123)
        self.vote1.setvoter_id(321)
        self.assertEqual(self.vote1.voter_id, 321)

        self.vote1.setvoter_id('abc')
        self.assertEqual(self.vote1.voter_id, 'abc')
    
    def test_setcandidate_id(self):
        print('test_setcandidate_id')
        self.assertEqual(self.vote1.candidate_id, 1)
        self.vote1.setcandidate_id(2)
        self.assertEqual(self.vote1.candidate_id, 2)

        self.vote1.setcandidate_id('abc')
        self.assertEqual(self.vote1.candidate_id, 'abc')

    def test_setposition(self):
        print('test_setpostion')
        self.assertEqual(self.vote1.position, 'president')
        self.vote1.setposition('mayor')
        self.assertEqual(self.vote1.position, 'mayor')

    def test_setelection_type(self):
        print('test_setelection_type')
        self.assertEqual(self.vote1.electionType, 'federal')
        self.vote1.setelection_type('local')
        self.assertEqual(self.vote1.electionType, 'local')

    def test_vote(self):
        print('test_vote')
        self.assertEqual(self.vote1.vote(), {'voter_id':123, 'candidate_id':1, 'position':'president', 'election_type':'federal'})

        


if __name__ == '__main__':
    unittest.main()
