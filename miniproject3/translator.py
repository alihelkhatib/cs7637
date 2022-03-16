from phrase import Phrase
from ThematicFrame import Frame

class Translator:
    multi_agents = ('name', 'conjunction', 'name')
    def __init__(self, sentence, question):
        self.sentence = Phrase(sentence, type='sentence')
        self.question = Phrase(question, type='question')
        

    def read(self, phrase):
        frame = Frame()
        self.sentence.scan_chunks(self.multi_agents)
        return frame

    def __repr__(self) -> str:
        return f'Sentence: {self.sentence}\nQuestion: {self.question}'

    
    

    



    

