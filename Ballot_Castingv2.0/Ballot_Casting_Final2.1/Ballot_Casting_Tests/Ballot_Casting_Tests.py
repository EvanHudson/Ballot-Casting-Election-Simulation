from TabulateContext import TabulateContext
from Election_Registry import ElectionRegistry
from FederalElectionStrategy import FederalElectionStrategy
from StateElectionStrategy import StateElectionStrategy
from LocalElectionStrategy import LocalElectionStrategy

class Ballot_Casting_Tests:
    def voteObjectUnitTest(self):
        print('voteObjectUnitTest\n----------------------------------')
    def FederalElectionStrategyUnitTest(self):
        print('FederalElectionStrategyUnitTest\n----------------------------------')
    def StateElectionStrategyUnitTest(self):
        print('StateElectionStrategyUnitTest\n----------------------------------')
    def LocalElectionStrategyUnitTest(self):
        print('LocalElectionStrategyUnitTest\n----------------------------------')
    def TabulateContextUnitTest(self):
        print('TabulateContextUnitTest\n----------------------------------')
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
        valid_vote_object_federal = {
            "voter_id": 1234,
            "candidate_id": 2,
            "position": "president",
            "election_type": "federal"
        }

        valid_vote_object_local = {
            "voter_id": 12345,
            "candidate_id": 2,
            "position": "Mayor",
            "election_type": "local"
        }

        valid_vote_object_state = {
            "voter_id": 12345,
            "candidate_id": 2,
            "position": "Governor",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(valid_vote_object_federal)
        tabulate_context.tabulate_vote(valid_vote_object_local)
        tabulate_context.tabulate_vote(valid_vote_object_state)
        # wrong election types
        print('\n----------------------------------------')
        print('\nWRONG ELECTION TYPE')
        invalid_vote_object_federal = {
            "voter_id": 12345,
            "candidate_id": 2,
            "position": "president",
            "election_type": "Discrete"
        }

        invalid_vote_object_local = {
            "voter_id": 12345,
            "candidate_id": 2,
            "position": "president",
            "election_type": "Confidential"
        }

        invalid_vote_object_state = {
            "voter_id": 12345,
            "candidate_id": 2,
            "Money": "Governor",
            "election_type": "Tis the season"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)
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
        invalid_vote_object_federal = {
            "voter_id": 1000,
            "candidate_id": 2,
            "position": "Governor",
            "election_type": "Federal"
        }

        invalid_vote_object_local = {
            "voter_id": 1000,
            "candidate_id": 2,
            "position": "President",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 1000,
            "candidate_id": 2,
            "position": "The Beatles",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)

        # incorrect candidate ID in election_type
        print('\n----------------------------------------')
        print('\nINCORRECT Candidate Id')
        invalid_vote_object_federal = {
            "voter_id": 12,
            "candidate_id": 3,
            "position": "President",
            "election_type": "Federal"
        }

        invalid_vote_object_local = {
            "voter_id": 13,
            "candidate_id": 10025,
            "position": "Mayor",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 14,
            "candidate_id": 1005,
            "position": "Governor",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)

        # repeated voter ID for position in election_type
        print('\n----------------------------------------')
        print('\nRepeated voter Id')
        invalid_vote_object_federal = {
            "voter_id": 12,
            "candidate_id": 2,
            "position": "President",
            "election_type": "Federal"
        }

        invalid_vote_object_local = {
            "voter_id": 13,
            "candidate_id": 10,
            "position": "Mayor",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 14,
            "candidate_id": 8,
            "position": "Governor",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)
        # repeated voter ID in election_type but for different position
        print('\n----------------------------------------')
        print('\nRepeated voter Id')
        invalid_vote_object_federal = {
            "voter_id": 12,
            "candidate_id": 2,
            "position": "vice President",
            "election_type": "Federal"
        }

        invalid_vote_object_local = {
            "voter_id": 13,
            "candidate_id": 10,
            "position": "Sheriff",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 14,
            "candidate_id": 8,
            "position": "Senator",
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)

        # incorrect format in key
        print('\n----------------------------------------')
        print('\n incorrect format')
        invalid_vote_object_federal = {
            "voter_id": -121,
            "candidate_id": 2,
            "position": 1,
            "election_type": "Federal"
        }

        invalid_vote_object_local = {
            "voter_id": 131,
            "candidate_id": 'hello' ,
            "position": "Mayor",
            "election_type": "local"
        }

        invalid_vote_object_state = {
            "voter_id": 141,
            "candidate_id": 8,
            "position": 1,
            "election_type": "state"
        }
        tabulate_context.tabulate_vote(invalid_vote_object_federal)
        tabulate_context.tabulate_vote(invalid_vote_object_local)
        tabulate_context.tabulate_vote(invalid_vote_object_state)

        print('\a')  # tests done

