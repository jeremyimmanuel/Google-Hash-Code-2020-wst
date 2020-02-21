# hello this is book class ahaha 😸

class Book:
    def __init__(self, bid, score):
        self.bid = bid
        self.score = score

    def __hash__(self):
        return self.bid
        #return -self.score

    def __eq__(self, other):
        return self.bid == other.bid
    
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __str__(self):
        return str(self.bid)

    # def __repr__(self):
    #     return '''book {
    #         id : %d,
    #         score : %d,
    #     }
    #     ''' % (self.bid, self.score)