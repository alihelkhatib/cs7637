from question_frame import QuestionFrame
import common_words


def translate_string_to_question_frame(question: str) -> QuestionFrame:
    question = question.rstrip("?")
    question = question.replace("'", "")
    words = question.split()

    question_words = []
    for word_index, word in enumerate(words):
        if word in common_words.verbs or word in common_words.other:
            question_words = words[:word_index]
            break

    last_word = words[len(words) - 1]
    if last_word in common_words.prepositions:
        question_words.append(last_word)

    subjects = []
    for word_index, word in enumerate(words):
        if word in common_words.names:
            subjects.append(word)
            if word_index + 2 < len(words) and words[word_index + 1] == "and":
                subjects.append(words[word_index + 2])
            break

    noun = None
    for word_index, word in enumerate(words):
        if word in common_words.articles:
            noun = words[word_index + 1]
            break

    return QuestionFrame(question_words=question_words, subjects=subjects, noun=noun)





