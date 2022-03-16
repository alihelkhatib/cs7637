from SentenceReadingAgent import SentenceReadingAgent


def test():
    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    sentence_3 = "Bring the box to the other room."
    question_10 = "Where should the box go?"

    sentence_4 = "There are a thousand children in this town."
    question_11 = "How many children are in this town?"

    sentence_5 = "Give us all your money."
    question_12 = "Who should you give your money to?"
    question_13 = "How much of your money should you give us?"

    sentence_6 = "This year David will watch a play."
    question_14 = "Who will watch a play?"

    sentence_7 = "The water is blue."
    question_15 = "What is blue?"

    sentence_8 = "She told her friend a story."
    question_16 = "What did she tell?"

    sentence_9 = "There is snow at the top of the mountain."
    question_17 = "What is on top of the mountain?"

    sentence_10 = "Frank was busy last night."
    question_18 = "When was Frank busy?"

    sentence_11 = "The sound of rain is cool."
    question_19 = "What has a cool sound?"
    question_20 = "What is cool?"
    
    s12 = "The house is made of paper."
    q21 = "What is the house made of?"

    print("Passed" if test_agent.solve(sentence_1, question_1) == "Ada" else "question_1 Failed")  # "Ada"
    print("Passed" if test_agent.solve(sentence_1, question_2) == "note" else "question_2 Failed")  # "note" or "a note"
    print("Passed" if test_agent.solve(sentence_1, question_3) == "Irene" else "question_3 Failed")  # "Irene"
    print("Passed" if test_agent.solve(sentence_1, question_4) == "short" else "question_4 Failed")  # "short"

    print("Passed" if test_agent.solve(sentence_2, question_5) == "David" else "question_5 Failed")  # "David"
    print("Passed" if test_agent.solve(sentence_2, question_6) == "school" else "question_6 Failed")  # "school"
    print("Passed" if test_agent.solve(sentence_2, question_7) == "mile" else "question_7 Failed")  # "mile" or "a mile"
    print("Passed" if test_agent.solve(sentence_2, question_8) == "walk" else "question_8 Failed")  # "walk"
    print("Passed" if test_agent.solve(sentence_2, question_9) == "8:00AM" else "question_9 Failed")  # "8:00AM"

    print("Passed" if test_agent.solve(sentence_3, question_10) == "the other room" else "question_10 Failed")  # "the other room"
    print("Passed" if test_agent.solve(sentence_4, question_11) == "thousand" else "question_11 Failed")  # "thousand"
    print("Passed" if test_agent.solve(sentence_5, question_12) == "us" else "question_12 Failed")  # "us"
    print("Passed" if test_agent.solve(sentence_5, question_13) == "all" else "question_13 Failed")  # "all"
    print("Passed" if test_agent.solve(sentence_6, question_14) == "David" else "question_14 Failed")  # "David"
    print("Passed" if test_agent.solve(sentence_7, question_15) == "water" else "question_15 Failed")  # "water"
    print("Passed" if test_agent.solve(sentence_8, question_16) == "story" else "question_16 Failed")  # "story"
    print("Passed" if test_agent.solve(sentence_9, question_17) == "snow" else "question_17 Failed")  # "snow"
    print("Passed" if test_agent.solve(sentence_10, question_18) == "last" else "question_18 Failed")  # "last night"
    print("Passed" if test_agent.solve(sentence_11, question_19) == "rain" else "question_19 Failed")  # "rain"
    print("Passed" if test_agent.solve(sentence_11, question_20) == "sound of rain" else "question_20 Failed")  # "sound of rain"




if __name__ == "__main__":
    test()
