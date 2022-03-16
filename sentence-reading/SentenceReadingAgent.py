from question_translator import translate_string_to_question_frame
from sentence_translator import translate_string_to_sentence_frame
from question_respondent import answer_question_about_sentence


class SentenceReadingAgent:
    def solve(self, sentence, question):
        sentence_frame = translate_string_to_sentence_frame(sentence)
        question_frame = translate_string_to_question_frame(question)
        answer = answer_question_about_sentence(question_frame, sentence_frame)
        return answer
