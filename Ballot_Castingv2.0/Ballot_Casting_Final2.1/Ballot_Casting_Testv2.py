from TabulateContext import TabulateContext
from Election_Registry import ElectionRegistry
from FederalElectionStrategy import FederalElectionStrategy
from StateElectionStrategy import StateElectionStrategy
from LocalElectionStrategy import LocalElectionStrategy
from vote_object import Vote_Object
#unit tests
from test_TabulateContext import TestTabulateContext
from test_FederalElectionStrategy import TestFederalElectionStrategy
from test_StateElectionStrategy import TestStateElectionStrategy
from test_LocalElectionStrategy import TestLocalElectionStrategy
from test_vote_object import TestVoteObject

class Ballot_Casting_Tests:
    def voteObjectUnitTest(self):
        print('voteObjectUnitTest\n----------------------------------')
        test_instance = TestVoteObject()
        test_instance.setUp()
        test_instance.tearDown()

    def FederalElectionStrategyUnitTest(self):
        print('FederalElectionStrategyUnitTest\n----------------------------------')
        test_instance = TestFederalElectionStrategy()
        test_instance.setUp()
        test_instance.tearDown()

    def StateElectionStrategyUnitTest(self):
        print('StateElectionStrategyUnitTest\n----------------------------------')
        test_instance = TestStateElectionStrategy()
        test_instance.setUp()
        test_instance.tearDown()

    def LocalElectionStrategyUnitTest(self):
        print('LocalElectionStrategyUnitTest\n----------------------------------')
        test_instance = TestLocalElectionStrategy()
        test_instance.setUp()
        test_instance.tearDown()

    def TabulateContextUnitTest(self):
        print('TabulateContextUnitTest\n----------------------------------')
        test_instance = TestTabulateContext()
        test_instance.setUp()
        test_instance.tearDown()
    def strategiesTests(self):
            # Example Usage:
        election_registry = ElectionRegistry()
        tabulate_context = TabulateContext(election_registry)
        # General TESTS
        if self:
            print("\nGENERAL TESTS\n")
        else:
            print('')

        # Automatic selection of strategy based on election_type
        print('\n----------------------------------------')
        print('\nCORRECT FORMAT')
       
        valid_vote_object_federal = Vote_Object(1234,2, 'President', 'federal')
        valid_vote_object_local = Vote_Object(1234,2, 'Mayor', 'local')
        valid_vote_object_state = Vote_Object(1234,2, 'Governor', 'state')
         
        print('Inputting: 1234, 2, president, federal')
        tabulate_context.tabulate_vote(valid_vote_object_federal.vote())
        print('Inputting: 1236, 2, Governor, state')
        tabulate_context.tabulate_vote(valid_vote_object_state.vote())
        print('Inputting: 1235, 2, Mayor, local')
        tabulate_context.tabulate_vote(valid_vote_object_local.vote())


       
       # wrong election types
        print('\n----------------------------------------')
        print('\nWRONG ELECTION TYPE')
        invalid_vote_object_federal = Vote_Object(12345,2,'President','federation') 
       
        invalid_vote_object_local = Vote_Object(12345,2,'Mayor','location')

        invalid_vote_object_state = Vote_Object(12345,2,'Governor','Tis the season')

        print('\nInputting: 12345,2,President,federation')
        tabulate_context.tabulate_vote(invalid_vote_object_federal.vote())
        print('\nInputting: 12345,2,Mayor,location')
        tabulate_context.tabulate_vote(invalid_vote_object_local.vote())
        print('\nInputiing: 12345,2,Governor,Tis the season')
        tabulate_context.tabulate_vote(invalid_vote_object_state.vote())
       
       # wrong keys
        print('\n----------------------------------------')
        print('\nWRONG KEYS')
        invalid_vote_object_federal = {
            "voter": 12345,
            "candidate_id": 2,
            "position": "president",
            "election_type": "federal"
        }

        invalid_vote_object_local = {
            "voter_id": 12345,
            "data": 2,
            "position": "mayor",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 12345,
            "candidate_id": 2,
            "Money": "Governor",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)

        # incorrect positions in election_type
        print('\n----------------------------------------')
        print('\nINCORRECT POSITIONS')
        invalid_vote_object_federal = Vote_Object(1000,2,'Governor','Federal')

        invalid_vote_object_local = Vote_Object(1000,2,'President','local')

        invalid_vote_object_state = Vote_Object(1000,2,'The Beatles','state')
           
        print('\nInputting: 1000,2,Governor,Federal')
        tabulate_context.tabulate_vote(invalid_vote_object_federal.vote())
        print('\nInputting: 1000,2,President,State')
        tabulate_context.tabulate_vote(invalid_vote_object_state.vote())
        print('\nInputting: 1000,2,The Beatles,State')
        tabulate_context.tabulate_vote(invalid_vote_object_local.vote())
      
      # incorrect candidate ID in election_type
        print('\n----------------------------------------')
        print('\nINCORRECT Candidate Id')
        invalid_vote_object_federal = Vote_Object(12,3,'President','Federal') 

        invalid_vote_object_local = Vote_Object(13, 10025,'Mayor','local')

        invalid_vote_object_state = Vote_Object(14,1005,'Governor','state')
         
        print('\nInputting: 12,3,President,Federal')
        tabulate_context.tabulate_vote(invalid_vote_object_federal.vote())
        print('\nInputting: 14,1005,Governor,state')
        tabulate_context.tabulate_vote(invalid_vote_object_state.vote())
        print('\nInputting: 13, 10025,Mayor,local')
        tabulate_context.tabulate_vote(invalid_vote_object_local.vote())
       
        

        # repeated voter ID for position in election_type
        print('\n----------------------------------------')
        print('\nRepeated voter Id')
        invalid_vote_object_federal = Vote_Object(12,2,'President','Federal')
            
        invalid_vote_object_local = Vote_Object(13,10,'Mayor','local')

        invalid_vote_object_state = Vote_Object(14,8,'Governor','state')
        
        print('\nInputting:: 12,2,President, Federal')
        tabulate_context.tabulate_vote(invalid_vote_object_federal.vote())
        print('\nInputting:: 13,10,Mayor,local')
        tabulate_context.tabulate_vote(invalid_vote_object_local.vote())
        print('\nInputting:: 14,8,Governor,state')
        tabulate_context.tabulate_vote(invalid_vote_object_state.vote())
     
     # repeated voter ID in election_type but for different position
        print('\n----------------------------------------')
        print('\nRepeated voter Id for different position')
        valid_vote_object_federal = Vote_Object(12,2,'vice President','Federal')
            
        valid_vote_object_local = Vote_Object(13,10,'Sheriff','local')

        valid_vote_object_state = Vote_Object(14,8,'Senator','state')
           
        print('\nInputting:: 12,2,vice President,Federal')
        tabulate_context.tabulate_vote(valid_vote_object_federal.vote())
        print('\nInputting:: 12,2,Senetor,state')
        tabulate_context.tabulate_vote(valid_vote_object_state.vote())
        print('\nInputting:: 12,2,Sheriff,local')
        tabulate_context.tabulate_vote(valid_vote_object_local.vote())
        

        # incorrect format in key
        print('\n----------------------------------------')
        print('\n incorrect format')
        invalid_vote_object_federal = Vote_Object(-121,2,1,'Federal')

        invalid_vote_object_local = Vote_Object(131,'hello','Mayor','local')
            
        invalid_vote_object_state = Vote_Object(141,8,1,'state')
            
        print('\nInputting:: -121,2,1,Federal')
        tabulate_context.tabulate_vote(invalid_vote_object_federal.vote())
        print('\nInputting:: 141,8,1,state')       
        tabulate_context.tabulate_vote(invalid_vote_object_state.vote())
        print('\nInputting:: 131,hello,Mayor,local')
        tabulate_context.tabulate_vote(invalid_vote_object_local.vote())
     

        print('\a')  # tests done
