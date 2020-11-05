import pytest
import emotive_eliza

eliza_inst = emotive_eliza.Eliza(0)

def test_preprocess():
    sentence1 = "I am TeRribly unhApPy."
    new_sentence1 = eliza_inst.preprocess(sentence1)

    sentence2 = "I;; am aFr*a{id} of Spid@er\s."
    new_sentence2 = eliza_inst.preprocess(sentence2)

    sentence3 = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_sentence3 = eliza_inst.preprocess(sentence3)

    # Uppercase --> lowercase
    assert new_sentence1 == "i am terribly unhappy"
    # Strips punctuation/special chars with no extra spaces
    assert new_sentence2 == "i am afraid of spiders"
    # Will remove all specified special chars
    assert new_sentence3 == ""


def test_mood_keywords():
    faux_pas = "I enjoy the musical stylings of cardi b"
    eliza_inst.mood_keywords(faux_pas)
    # Mood decrement
    assert eliza_inst.mood == -1

    redeem = "I debug with a rubber duck"
    eliza_inst.mood_keywords(redeem)
    # Return to neutral (mood increment)
    assert eliza_inst.mood == 0

    likeable = "next to blade runner, akira is a personal favorite of mine"
    eliza_inst.mood_keywords(likeable)
    # Mood decrement
    assert eliza_inst.mood == 1

    # reset/verify instance mood
    eliza_inst.mood = 0
    assert eliza_inst.mood == 0


def test_keywords():
    proc_sentence1 = "i am terribly unhappy"
    new_proc_sentence = eliza_inst.keywords(proc_sentence1)
    print(new_proc_sentence)

    keyword_index = eliza_inst.keyword_list.index("i am")
    print(keyword_index)

    #keywords yields an extra space!! FIX?
    assert new_proc_sentence == "10 terribly unhappy"


#test_preprocess()
#test_mood_keywords()
test_keywords()