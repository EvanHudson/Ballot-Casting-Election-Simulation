from Strategy_interfaces import ElectionType, VerifyState
console_output=True
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

        # gets variables from vote object
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

        # Check if the voter ID has already voted for the position in this election type
        if not self.election_registry.register_vote(voter_id, election_type, position):
            if console_output:
                print(f'Voter ID {voter_id} has already voted for position {position} in {election_type} election.')
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
