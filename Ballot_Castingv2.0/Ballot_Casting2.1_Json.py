import sys

console_output = True   # for debug outputs
tests = True    # for tests outputs

# Strategy Interfaces
class ElectionType:
    def verify(self, vote_object):
        pass

class VerifyLocal:
    def verify(self, vote_object):
        pass

class VerifyState:
    def verify(self, vote_object):
        pass

class VerifyFederal:
    def verify(self, vote_object):
        pass

# Election Registry
class ElectionRegistry:
    def __init__(self):
        self.used_voter_ids = {
            'federal': set(),
            'local': set(),
            'state': set()
        }

    def register_vote(self, voter_id, election_type):
        if voter_id in self.used_voter_ids[election_type]:
            print(f'Voter ID {voter_id} has already been used for {election_type} election.')
            return False
        else:
            self.used_voter_ids[election_type].add(voter_id)
            print(f'Voter ID {voter_id} registered successfully for {election_type} election.')
            return True

# Concrete Strategy Classes
class FederalElectionStrategy(ElectionType, VerifyFederal):
    def __init__(self, election_registry):
        self.election_registry = election_registry

    def verify(self, vote_object):
        if console_output:
            print('\nFederal Verification Strategy')

        # Handles wrong keys
        required_keys = ["voter_id", "candidate_id", "position", "election_type"]
        if not all(key in vote_object for key in required_keys):
            if console_output:
                print('Missing Key(s)')
            return False
        
        #gets variables from vote object
        voter_id = vote_object.get("voter_id")
        candidate_id = vote_object.get("candidate_id")
        position = vote_object.get("position")
        election_type = vote_object.get("election_type")
        
        # Check voter ID format
        if not isinstance(voter_id, int) or voter_id <= 0:
            if console_output:
                print('Invalid Voter ID Format')
            return False

        # Check candidate ID format
        if not isinstance(candidate_id, int) or candidate_id <= 0:
            if console_output:
                print('Invalid Candidate ID Format')
            return False

        # Check position format
        if not isinstance(position, str) or not position:
            if console_output:
                print('Invalid Position Format')
            return False
        # Check election type format
        if not isinstance(election_type, str) or not election_type:
            if console_output:
                print('Invalid Election Type Format')
            return False

        # Print what's in vote objects and sets them as variables for use in verification and sets strings to lowercase
        position = vote_object.get("position").lower()
        election_type = vote_object.get("election_type").lower()
        if console_output:
            print(f'Voter Id: {voter_id}')
            print(f'Candidate Id: {candidate_id}')
            print(f'Position: {position}')
            print(f'Election Type: {election_type}')

        # Check if the voter ID has already been used
        if not self.election_registry.register_vote(voter_id, election_type):
            if console_output:
                print(f'Voter ID {voter_id} has already been used for {election_type} election.')
            return False

        # Handles wrong positions
        valid_positions = ["president", "vice president", "senator", "representative"]
        if position not in valid_positions:
            if console_output:
                print('Wrong Position')
            return False

        # Handles wrong candidate ID
        if position == "president" and candidate_id <= 2:
            print('')
        elif position == "vice president" and candidate_id <= 2:
            print('')
        elif position == "senator" and candidate_id <= 10:
            print('')
        elif position == "representative" and candidate_id <= 10:
            print('')
        else:
            if console_output:
                print('Bad CandidateId')
            return False

        return True

class LocalElectionStrategy(ElectionType, VerifyLocal):
    def __init__(self, election_registry):
        self.election_registry = election_registry

    def verify(self, vote_object):
        if console_output:
            print('\nLocal Verification Strategy')
        # Handles wrong keys
        required_keys = ["voter_id", "candidate_id", "position", "election_type"]
        if not all(key in vote_object for key in required_keys):
            if console_output:
                print('Missing Key')
            return False
        #gets variables from vote object
        voter_id = vote_object.get("voter_id")
        candidate_id = vote_object.get("candidate_id")
        position = vote_object.get("position")
        election_type = vote_object.get("election_type")
        
        # Check voter ID format
        if not isinstance(voter_id, int) or voter_id <= 0:
            if console_output:
                print('Invalid Voter ID Format')
            return False

        # Check candidate ID format
        if not isinstance(candidate_id, int) or candidate_id <= 0:
            if console_output:
                print('Invalid Candidate ID Format')
            return False

        # Check position format
        if not isinstance(position, str) or not position:
            if console_output:
                print('Invalid Position Format')
            return False
        # Check election type format
        if not isinstance(election_type, str) or not election_type:
            if console_output:
                print('Invalid Election Type Format')
            return False

        # Print what's in vote objects and sets them as variables for use in verification and sets strings to lowercase
        position = vote_object.get("position").lower()
        election_type = vote_object.get("election_type").lower()
        if console_output:
            print(f'Voter Id: {voter_id}')
            print(f'Candidate Id: {candidate_id}')
            print(f'Position: {position}')
            print(f'Election Type: {election_type}')


        # Check if the voter ID has already been used
        if not self.election_registry.register_vote(voter_id, election_type):
            if console_output:
                print(f'Voter ID {voter_id} has already been used for {election_type} election.')
            return False

        # Handles wrong positions
        valid_positions = ["mayor", "city council member", "commissioner", "school board member", "sheriff", "district attorney"]
        if position not in valid_positions:
            if console_output:
                print('Wrong Position')
            return False
        
        # Handles wrong candidate ID
        if position == "mayor" and candidate_id <= 2:
            print('')
        elif position == "city council member" and candidate_id <= 10:
            print('')
        elif position == "commissioner" and candidate_id <= 10:
            print('')
        elif position == "school board member" and candidate_id <= 10:
            print('')
        elif position == "sheriff" and candidate_id <= 10:
            print('')
        elif position == "district attorney" and candidate_id <= 10:
            print('')
        else:
            if console_output:
                print('Bad CandidateId')
            return False

        return True

class StateElectionStrategy(ElectionType, VerifyState):
    def __init__(self, election_registry):
        self.election_registry = election_registry

    def verify(self, vote_object):
        if console_output:
            print('\nState Verification Strategy')
        # Handles wrong keys
        required_keys = ["voter_id", "candidate_id", "position", "election_type"]
        if not all(key in vote_object for key in required_keys):
            if console_output:
                print('Missing Key')
            return False

                #gets variables from vote object
        voter_id = vote_object.get("voter_id")
        candidate_id = vote_object.get("candidate_id")
        position = vote_object.get("position")
        election_type = vote_object.get("election_type")
        
        # Check voter ID format
        if not isinstance(voter_id, int) or voter_id <= 0:
            if console_output:
                print('Invalid Voter ID Format')
            return False

        # Check candidate ID format
        if not isinstance(candidate_id, int) or candidate_id <= 0:
            if console_output:
                print('Invalid Candidate ID Format')
            return False

        # Check position format
        if not isinstance(position, str) or not position:
            if console_output:
                print('Invalid Position Format')
            return False
        # Check election type format
        if not isinstance(election_type, str) or not election_type:
            if console_output:
                print('Invalid Election Type Format')
            return False

        # Print what's in vote objects and sets them as variables for use in verification and sets strings to lowercase
        position = vote_object.get("position").lower()
        election_type = vote_object.get("election_type").lower()
        if console_output:
            print(f'Voter Id: {voter_id}')
            print(f'Candidate Id: {candidate_id}')
            print(f'Position: {position}')
            print(f'Election Type: {election_type}')


        # Check if the voter ID has already been used
        if not self.election_registry.register_vote(voter_id, election_type):
            if console_output:
                print(f'Voter ID {voter_id} has already been used for {election_type} election.')
            return False

        # Handles wrong positions
        valid_positions = ["governor", "senator", "representative", "assembly member", "attorney general", "secretary of state"]
        if position not in valid_positions:
            if console_output:
                print('Wrong Position')
            return False
        # Handles wrong candidate ID
        if position == "governor" and candidate_id <= 2:
            print('')
        elif position == "senator" and candidate_id <= 10:
            print('')
        elif position == "representative" and candidate_id <= 10:
            print('')
        elif position == "assembly member" and candidate_id <= 10:
            print('')
        elif position == "attorney general" and candidate_id <= 10:
            print('')
        elif position == "secretary of state" and candidate_id <= 10:
            print('')
        else:
            if console_output:
                print('Bad CandidateId')
            return False

        return True

# Context Class
class TabulateContext:
    def __init__(self, election_registry):
        self.verify_strategy = None
        self.election_registry = election_registry

    def tabulate_vote(self, vote_object: dict) -> None:
        election_type = vote_object.get("election_type", "").lower()

        if election_type == "federal":
            self.verify_strategy = FederalElectionStrategy(self.election_registry)
        elif election_type == "local":
            self.verify_strategy = LocalElectionStrategy(self.election_registry)
        elif election_type == "state":
            self.verify_strategy = StateElectionStrategy(self.election_registry)
        else:
            print(f"Unknown election type: {election_type}. Not tabulated.")
            return

        if self.verify_strategy.verify(vote_object):
            self._perform_tabulation(vote_object)
        else:
            print("Vote verification failed. Not tabulated.")

    def _perform_tabulation(self, vote_object: dict) -> None:
        # Implement the actual tabulation logic here
        candidate_id = vote_object.get("candidate_id")
        position = vote_object.get("position")
        print(f"Vote tabulated for candidate {candidate_id} for the position of {position}")

# Example Usage:
election_registry = ElectionRegistry()
tabulate_context = TabulateContext(election_registry)
# General TESTS
if tests:
    print("\nGENERAL TESTS\n")
else:
    sys.exit()

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

# incorrect voter ID in election_type
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
