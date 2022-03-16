from sentence_frame import SentenceFrame
import common_words
import re


def translate_string_to_sentence_frame(sentence: str) -> SentenceFrame:
    sentence = sentence.rstrip('.')
    sentence = sentence.replace("'", "")
    words = sentence.split()

    subjects = []
    last_subject_index = 0
    for word_index, word in enumerate(words):
        if word in common_words.names or word in common_words.pronouns:
            subjects.append(word)
            last_subject_index = word_index
            if word_index + 2 < len(words) and words[word_index + 1] == "and":
                subjects.append(words[word_index + 2])
                last_subject_index = word_index + 2
            break

    if len(subjects) == 0:
        for word_index, word in enumerate(words):
            if word.lower() in common_words.articles:
                if word_index + 3 < len(words) and words[word_index + 2] == "of":
                    subjects = words[word_index + 1:word_index + 4]
                    last_subject_index = word_index + 3
                else:
                    subjects.append(words[word_index + 1])
                    last_subject_index = word_index + 1
                break

    verb = words[last_subject_index + 1] if last_subject_index + 1 < len(words) else None

    noun = None
    noun_adjectives = []

    for word_index, word in enumerate(words):
        if word in common_words.articles or word in common_words.quantities \
                or word in common_words.numerals:
            for index in range(word_index + 1, len(words)):
                if words[index] in common_words.prepositions:
                    noun = words[index + 1]
                    noun_adjectives = words[word_index + 1: index - 1]
                    break
                elif index == len(words) - 1:
                    noun = words[index]
                    noun_adjectives = words[word_index + 1: index]
            break

    for word_index, word in enumerate(words):
        if word in common_words.versions_of_to_be and word_index + 1 < len(words) and words[
            word_index + 1] in common_words.adjectives:
            noun_adjectives = words[word_index + 1]

    time_regex = r"((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))"
    time_regex_result = re.search(time_regex, sentence)
    time = None
    if time_regex_result:
        time = time_regex_result.group(1)

    place = None
    for word_index, word in enumerate(words):
        if word in {'at', 'to', 'in'} and words[word_index + 1] not in common_words.verbs:
            possible_place = ""
            for index in range(word_index + 1, len(words)):
                if words[index] in common_words.nouns:
                    possible_place += words[index]
                    break
                else:
                    possible_place += words[index] + " "
            if possible_place != time:
                place = possible_place
                break

    recipient = None
    for word_index, word in enumerate(words):
        if word in {'to'} and word_index + 1 < len(words) and words[word_index + 1] in common_words.names:
            recipient = words[word_index + 1]

    quantities = None
    for word in words:
        if word in common_words.quantities:
            quantities = word

    return SentenceFrame(subjects=subjects, verb=verb, noun=noun, noun_adjectives=noun_adjectives, recipient=recipient,
                         location=place, time=time, quantities=quantities)
