#interfaces
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
