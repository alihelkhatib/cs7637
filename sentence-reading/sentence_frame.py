class SentenceFrame:
    def __init__(self, subjects: list, verb: str, noun: str = None, adjectives: list = None, recipient: str = None,
                 location: str = None, time: str = None, quantities: str = None):
        self.subjects = subjects
        self.verb = verb
        self.noun = noun
        self.adjectives = adjectives
        self.recipient = recipient
        self.location = location
        self.time = time
        self.quantities = quantities

    def __repr__(self):
        return f"subjects words: {self.subjects}\nverb: {self.verb}\nnoun: {self.noun}" \
               f"\nadjectives: {self.adjectives}\nrecipent: {self.recipient}" \
               f"\nlocation: {self.location}\ntime: {self.time}\nquantities: {self.quantities}"
