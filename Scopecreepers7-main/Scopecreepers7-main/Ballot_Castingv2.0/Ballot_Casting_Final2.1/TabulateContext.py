# Context Class
from FederalElectionStrategy import FederalElectionStrategy
from StateElectionStrategy import StateElectionStrategy
from LocalElectionStrategy import LocalElectionStrategy
class TabulateContext:
    def __init__(self, election_registry):
        self.verify_strategy = None
        self.election_registry = election_registry
        self.candidate_votes={}

    def tabulate_vote(self, vote_object: dict) -> None:
        election_type = str(vote_object.get("election_type", ""))
        if not election_type.isdigit():
            election_type = election_type.lower()

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

        # Update candidate_votes dictionary
        if candidate_id not in self.candidate_votes:
            self.candidate_votes[candidate_id] = 1
        else:
            self.candidate_votes[candidate_id] += 1

        print(f"Vote tabulated for candidate {candidate_id} for the position of {position}")

    def print_final_results(self):
        total_votes=0
        # Print total votes for all candidates after all votes have been tabulated
        print("\nFinal Results from Tabulation Class:")
        for cid in self.candidate_votes:
            print(f"Total votes for candidate {cid}: {self.candidate_votes[cid]}")
            total_votes+=self.candidate_votes[cid]
        print(f'Total Votes: {total_votes}')
    def record(self):
        return self.candidate_votes
