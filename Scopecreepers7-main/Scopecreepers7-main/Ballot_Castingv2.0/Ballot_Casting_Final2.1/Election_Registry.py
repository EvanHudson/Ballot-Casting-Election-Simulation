
# Election Registry
class ElectionRegistry:
    def __init__(self):
        self.used_voter_positions = {
            'federal': {},
            'local': {},
            'state': {}
        }

    def register_vote(self, voter_id, election_type, position):
        if voter_id in self.used_voter_positions[election_type]:
            if position in self.used_voter_positions[election_type][voter_id]:
                print(f'Voter ID {voter_id} has already voted for position {position} in {election_type} election.')
                return False
            else:
                self.used_voter_positions[election_type][voter_id].add(position)
                print(f'Voter ID {voter_id} registered successfully for position {position} in {election_type} election.')
                return True
        else:
            self.used_voter_positions[election_type][voter_id] = {position}
            print(f'Voter ID {voter_id} registered successfully for position {position} in {election_type} election.')
            return True

