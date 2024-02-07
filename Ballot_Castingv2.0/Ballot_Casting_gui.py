#gui
class ballotGui:
    def gui(self):
        print('            Ballot Casting Verification MVP')
        print('-------------------------------------------------------------------')
        print('|          1.     Simulated Election                             |')
        print('|          2.     Manual Vote Object                             |')
        print('|          3.     Tests                                          |')
        print('|          4.     Exit                                           |')
        print('-------------------------------------------------------------------')
        option=input(':')
        option=(int)(option)
        if(option==1):
            federalPos=input('Federal Position: ')
            federal1_candidate=input('Federal candidate 1: ')
            federal2_candidate=input('Federal candidate 2: ')
            statePos=input('State Position: ')
            state1_candidate=input('State candidate 1: ')
            state2_candidate=input('State candidate 2: ')
            localPos=input('Local Position: ')
            local1_candidate=input('Local candidate 1: ')
            local2_candidate=input('Local candidate 2: ')

            numberVoters=input('Number of voters: ')
            numberErrors=input('Errors: ')

            print(f'starting simulated election of {numberVoters} voters')
        elif(option==2):
            print('Enter manual vote object for verification')
            voteId=input('VoteId: ')
            candidateId=input('candidateId: ')
            position=input('position: ')
            electionType=input('electionType: ')
            #put into verify/tabulate
        elif(option==3):
            print('Exiting')
            exit()
        else:
            print('enter valid option')
while True:
    ballot_Gui=ballotGui()
    ballot_Gui.gui()
