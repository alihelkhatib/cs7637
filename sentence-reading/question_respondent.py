from question_frame import QuestionFrame
from sentence_frame import SentenceFrame


def answer_question_about_sentence(question_frame: QuestionFrame, sentence_frame: SentenceFrame) -> str:
    if "Who" in question_frame.question_words:
        if len(question_frame.question_words) == 1:
            return sentence_frame.subjects[0]
        elif "with" in question_frame.question_words:
            subject1 = sentence_frame.subjects[0]
            subject2 = sentence_frame.subjects[1]
            if subject1 in question_frame.subjects:
                return subject2
            return subject1
        elif "to" in question_frame.question_words:
            if sentence_frame.recipient:
                return sentence_frame.recipient
            else:
                return sentence_frame.subjects[0]

    if "What" in question_frame.question_words:
        if len(question_frame.question_words) > 1 and len(sentence_frame.noun_adjectives) > 0:
            return sentence_frame.noun_adjectives[0]
        elif sentence_frame.noun is None:
            return str(" ".join(sentence_frame.subjects))
        return sentence_frame.noun

    if "How" in question_frame.question_words:
        if len(question_frame.question_words) == 1:
            return sentence_frame.verb
        if "far" in question_frame.question_words:
            return sentence_frame.noun
        if "much" in question_frame.question_words:
            return sentence_frame.quantities
        return sentence_frame.noun_adjectives[0]

    if "Where" in question_frame.question_words:
        return sentence_frame.location

    if "time" in question_frame.question_words:
        return sentence_frame.time

    return ""