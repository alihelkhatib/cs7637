class Frame:
    def __init__(self, agent=None, verb=None, beneficiary=None, thematic_object=None, instrument=None, coagent=None) -> None:
        self.agent = agent
        self.verb = verb
        self.beneficiary = beneficiary
        self.thematic_object = thematic_object
        self.instrument = instrument
        self.coagent = coagent

    