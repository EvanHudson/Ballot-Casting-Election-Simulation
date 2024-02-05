import tkinter as tk
import random
from TabulateContext import TabulateContext
from Election_Registry import ElectionRegistry
from FederalElectionStrategy import FederalElectionStrategy
from LocalElectionStrategy import LocalElectionStrategy
from StateElectionStrategy import StateElectionStrategy
from Ballot_Casting_Testv2 import Ballot_Casting_Tests
from tkinter import simpledialog
from vote_object import Vote_Object
import time

class BallotGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Ballot Casting Verification MVP")
        self.tabulate_federal = TabulateContext(ElectionRegistry())  # Create an instance of TabulateContext
        self.tabulate_local = TabulateContext(ElectionRegistry())  # Create an instance of TabulateContext
        self.tabulate_state = TabulateContext(ElectionRegistry())  # Create an instance of TabulateContext

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Choose an option:").pack(pady=10)

        tk.Button(self.root, text="Simulated Election", command=self.simulated_election).pack(pady=5)
        tk.Button(self.root, text="Manual Vote Object", command=self.manual_vote_object).pack(pady=5)
        tk.Button(self.root, text="Tests", command=self.tests).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)

    def simulated_election(self):
        federal_pos = simpledialog.askstring("Simulated Election", "Federal Position:")
        federal1_candidate = simpledialog.askstring("Simulated Election", "Federal Candidate 1:")
        federal2_candidate = simpledialog.askstring("Simulated Election", "Federal Candidate 2:")
        state_pos = simpledialog.askstring("Simulated Election", "State Position:")
        state1_candidate = simpledialog.askstring("Simulated Election", "State Candidate 1:")
        state2_candidate = simpledialog.askstring("Simulated Election", "State Candidate 2:")
        local_pos = simpledialog.askstring("Simulated Election", "Local Position:")
        local1_candidate = simpledialog.askstring("Simulated Election", "Local Candidate 1:")
        local2_candidate = simpledialog.askstring("Simulated Election", "Local Candidate 2:")

        number_voters=0 #added so  specifies interger input
        number_voters = simpledialog.askinteger("Simulated Election", "Number of voters:")
        number_errors_federal = 0
        number_good_federal=0
        number_errors_state = 0
        number_good_state=0
        number_errors_local = 0
        number_good_local=0

        #tabulation variables
        self.candidate_votes={}
        fed_winner=1
        st_winner=1
        loc_winner=1

        
        print(f'Starting simulated election of {number_voters} voters')
        #federal votes
        for i in range(number_voters):
            error = random.randint(1, 10)
            vote = Vote_Object(i + 1, None, federal_pos, 'federal')
            if error > 3:
                vote.random_good()
                number_good_federal += 1
            else:
                vote.random_bad()
                number_errors_federal += 1
            self.tabulate_federal.tabulate_vote(vote.vote())

        self.tabulate_federal.print_final_results()
        print(f'federal good: {number_good_federal} bad:{number_errors_federal}')
        #state votes
        for i in range(number_voters):
            error = random.randint(1, 10)
            vote = Vote_Object(i + 1, None, state_pos, 'state')
            if error > 3:
                vote.random_good()
                number_good_state += 1
            else:
                vote.random_bad()
                number_errors_state += 1
            self.tabulate_state.tabulate_vote(vote.vote())

        

        #local votes
        for i in range(number_voters):
            error = random.randint(1, 10)
            vote = Vote_Object(i + 1, None, local_pos, 'local')
            if error > 3:
                vote.random_good()
                number_good_local += 1
            else:
                vote.random_bad()
                number_errors_local += 1
            self.tabulate_local.tabulate_vote(vote.vote())

        #seeing who won for each from tabulation

        #print statements for who won
            
        # Federal Winner
        self.candidate_votes = self.tabulate_federal.record()
        for cid in self.candidate_votes:
            if self.candidate_votes[cid] > self.candidate_votes[fed_winner]:
                fed_winner = cid

        if 1 in self.candidate_votes and 2 in self.candidate_votes:
            if self.candidate_votes[1] == self.candidate_votes[2]:
                federal1_candidate = 'Tie'

        # State Winner
        self.candidate_votes = self.tabulate_state.record()
        for cid in self.candidate_votes:
            if self.candidate_votes[cid] > self.candidate_votes[st_winner]:
                st_winner = cid

        if 1 in self.candidate_votes and 2 in self.candidate_votes:
            if self.candidate_votes[1] == self.candidate_votes[2]:
                state1_candidate = 'Tie'

        # Local Winner
        self.candidate_votes = self.tabulate_local.record()
        for cid in self.candidate_votes:
            if self.candidate_votes[cid] > self.candidate_votes[loc_winner]:
                loc_winner = cid

        if 1 in self.candidate_votes and 2 in self.candidate_votes:
            if self.candidate_votes[1] == self.candidate_votes[2]:
                local1_candidate = 'Tie'


        print('\nWINNERS\n------------------------------------')

            
        if(fed_winner==1):
            print(f'\nFederal {federal_pos} Winner: {federal1_candidate}')
            fed_winner=federal1_candidate
        elif(fed_winner==2):
            print(f'Federal {federal_pos} Winner: {federal2_candidate}')
            fed_winner=federal2_candidate
        if(st_winner==1):
            print(f'State {state_pos} Winner: {state1_candidate}')
            st_winner=state1_candidate
        elif(st_winner==2):
            print(f'State {state_pos} Winner: {state2_candidate}')
            st_winner=state2_candidate
        if(loc_winner==1):
            print(f'Local {local_pos} Winner: {local1_candidate}')
            loc_winner=local1_candidate
        elif(loc_winner==2):
            loc_winner=local1_candidate
            print(f'Local {local_pos} Winner: {local2_candidate}')
        #winner+ titles
        title_fed = f"{federal_pos} {fed_winner}"
        title_st = f"{state_pos} {st_winner}"
        title_loc = f"{local_pos} {loc_winner}"
            
        winners = {
            "Federal": title_fed,
            "State": title_st,
            "Local": title_loc,
        }
        self.display_winners_animation(winners)
        
        #print statements for checking accuracy of tabulaition class in cathcing the errors

        print('\nPrint statements for checking accuracy of tabulaition class\n------------------------------------')

        print('\nFEDERAL\n------------------------------------')
        print(f'\nFederal Good Votes sent in: {number_good_federal}\nFederal Bad Votes sent in:{number_errors_federal}')
        self.tabulate_federal.print_final_results()

        print('\nSTATE\n------------------------------------')
        print(f'\nState Good Votes Sent In: {number_good_state} \nState Bad Votes Sent In:{number_errors_state}')
        self.tabulate_state.print_final_results()
                
         
        print('\nLOCAL\n------------------------------------')
        print(f'\nLocal Good Votes Sent In: {number_good_local} \nLocal Bad Votes Sent In:{number_errors_local}')
        self.tabulate_local.print_final_results()
                    
    def display_winners_animation(self, winners):
        canvas = tk.Canvas(self.root, width=400, height=200)
        canvas.pack()
        i=3
        for position, winner in winners.items():
            text = canvas.create_text(200, 50, text=f"{position} Winner: {winner}", font=("Times New Roman", 12))
            for _ in range(20):  # Bouncing animation loop
                canvas.move(text, 0, i)
                self.root.update()
                time.sleep(0.05)
            i+=1
            time.sleep(3)  # Pause between animations
        time.sleep(5)
        canvas.destroy()

    def manual_vote_object(self):
        vote_id = simpledialog.askstring("Manual Vote Object", "Vote ID:")
        candidate_id = simpledialog.askstring("Manual Vote Object", "Candidate ID:")
        position = simpledialog.askstring("Manual Vote Object", "Position:")
        election_type = simpledialog.askstring("Manual Vote Object", "Election Type:")
        if (vote_id.isdigit()):
            vote_id=int(vote_id)
        if(candidate_id.isdigit()):
            candidate_id=int(candidate_id)
        print('Manual Vote Object Verification')


        
        # Call the verify/tabulate functions with the entered data from the user
        vote_object = {
            "voter_id": vote_id,
            "candidate_id": candidate_id,
            "position": position,
            "election_type": election_type
        }
        self.tabulate_vote(vote_object)
    def tests(self):
        tests=Ballot_Casting_Tests()
        tests.voteObjectUnitTest()
        tests.FederalElectionStrategyUnitTest()
        tests.StateElectionStrategyUnitTest()
        tests.LocalElectionStrategyUnitTest()
        tests.TabulateContextUnitTest()
        tests.strategiesTests()
    def tabulate_vote(self, vote_object):
        # You can use the classes and functions from Ballot_Casting2.2_Json.py here
        election_registry = ElectionRegistry()
        tabulate_context = TabulateContext(election_registry)
        tabulate_context.tabulate_vote(vote_object)

if __name__ == "__main__":
    root = tk.Tk()
    app = BallotGui(root)
    root.mainloop()
