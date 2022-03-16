class QuestionFrame:
    def __init__(self, question_words: list, subjects: list, noun: str):
        self.question_words = question_words
        self.subjects = subjects
        self.noun = noun

    def __repr__(self):
        return f"question words: {self.question_words}\nsubjects: {self.subjects}\nnoun: {self.noun}"
