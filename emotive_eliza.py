"""
# COMP 470 - Intro to AI: Project 1
# Eliza psychotherapist chatbot
# Author: Kyle Snow
# 9/16/20 -- 17:11
"""
import random


class Eliza:

    def __init__(self, mood: int):
        self.mood = mood

        self.goodbyes = ["bye", "goodbye", "exit"]

        self.punct_chars = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        self.conj_dict = {"are": "am", "am": "are", "were": "was", "was": "were", "you": "I", "i": "you",
                 "your": "my", "my": "your", "ive": " you've", "youve": "I've", "im": "you're", "youre": "I'm",
                 "me": "you"}

        self.keyword_list = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
                    "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name",
                    "cause",
                    "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike", "yes",
                    "friend", "computer"]


    def eliza(self):
        print("Hello, I am Eliza. Tell me your problems.")
        while (True):
            sentence = input("> ")
            sentence = self.preprocess(sentence)
            # print("pre-process: " + sentence)
            sentence = self.keywords(sentence)
            # print("keyword: " + sentence)
            sentence = self.conjugate(sentence)
            # print("conjugate: " + sentence)
            print(self.buildreply(sentence))


    def list_to_string(self, some_list:list):
        re_strung = " "
        return re_strung.join(some_list)

    def preprocess(self, sentence: str):
        new_sentence = sentence.lower()

        for char in new_sentence:
            if char in self.punct_chars:
                new_sentence = new_sentence.replace(char, "")
        return new_sentence

    def keywords(self, sentence):

        for word in self.keyword_list:
            if word in sentence:
                keyword_index = self.keyword_list.index(word)
                start_index = sentence.find(word)
                upto_index = start_index + len(word)
                new_sentence = str(keyword_index) + " " + sentence[upto_index:]
                return new_sentence
        keyword_index = -1
        new_sentence = str(keyword_index) + " " + sentence
        return new_sentence

    def conjugate(self, sentence):
        new_sentence = []
        sentence = sentence.split()
        for word in sentence:
            if word in self.conj_dict.keys():
                # print(word + " => " + conj_dict[word])
                new_sentence.append(self.conj_dict[word])
            else:
                new_sentence.append(word)
        new_sentence = new_sentence
        return self.list_to_string(new_sentence)

    def getreply(self, rep_num: int):
        reply_list = []
        reply = ""

        if rep_num == -1:
            reply_list = ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
                          "Come, come, elucidate your thoughts.", "Can you elaborate on that?",
                          "That is quite interesting."]
            reply = random.choice(reply_list)
        elif rep_num == 0:
            reply_list = ["Don't you believe that I can *", "Perhaps you would like me to be able to *",
                          "You want me to be able to *"]
            reply = random.choice(reply_list)
        elif rep_num == 1:
            reply_list = ["Perhaps you don't want to *", "Do you want to be able to *"]
            reply = random.choice(reply_list)
        elif rep_num == 2:
            reply_list = ["What makes you think I am *", "Does it please you to believe I am *",
                          "Perhaps you would like to be *", "Do you sometimes wish you were *"]
            reply = random.choice(reply_list)
        elif rep_num == 3:
            reply_list = ["What makes you think I am *", "Does it please you to believe I am *",
                          "Perhaps you would like to be *", "Do you sometimes wish you were *"]
            reply = random.choice(reply_list)
        elif rep_num == 4:
            reply_list = ["Don't you really *", "Why don't you *", "Do you wish to be able to *",
                          "Does that trouble you?"]
            reply = random.choice(reply_list)
        elif rep_num == 5:
            reply_list = ["Tell me more about such feelings.", "Do you often feel *", "Do you enjoy feeling *"]
            reply = random.choice(reply_list)
        elif rep_num == 6:
            reply_list = ["Do you really believe I don't *", "Perhaps in good time I will *", "Do you want me to *"]
            reply = random.choice(reply_list)
        elif rep_num == 7:
            reply_list = ["Do you think you should be able to *", "Why can't you *"]
            reply = random.choice(reply_list)
        elif rep_num == 8:
            reply_list = ["Why are you interested in whether or not I am *", "Would you prefer if I were not *",
                          "Perhaps in your fantasies I am *"]
            reply = random.choice(reply_list)
        elif rep_num == 9:
            reply_list = ["How do you know you can't *", "Have you tried?", "Perhaps you can now *"]
            reply = random.choice(reply_list)
        elif rep_num == 10:
            reply_list = ["Did you come to me because you are *", "How long have you been *",
                          "Do you believe it is normal to be *", "Do you enjoy being *"]
            reply = random.choice(reply_list)
        elif rep_num == 11:
            reply_list = ["Did you come to me because you are *", "How long have you been *",
                          "Do you believe it is normal to be *", "Do you enjoy being *"]
            reply = random.choice(reply_list)
        elif rep_num == 12:
            reply_list = ["We were discussing you, not me.", "Oh, I *", "You're not really talking about me, are you?"]
            reply = random.choice(reply_list)
        elif rep_num == 13:
            reply_list = ["What would it mean to you if you got *", "Why do you want *", "Suppose you got *",
                          "What if you never got *", "I sometimes also want *"]
            reply = random.choice(reply_list)
        elif rep_num == 14:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 15:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 16:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 17:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 18:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 19:
            reply_list = ["Why do you ask?", "Does that question interest you?",
                          "What answer would please you the most?", "What do you think?",
                          "Are such questions on your mind often?", "What is it that you really want to know?",
                          "Have you asked anyone else?", "Have you asked such questions before?",
                          "What else comes to your mind when you ask that?"]
            reply = random.choice(reply_list)
        elif rep_num == 20:
            reply_list = ["Names don't interest me.", "I don't care about names.  Please go on."]
            reply = random.choice(reply_list)
        elif rep_num == 21:
            reply_list = ["Is that the real reason?", "Don't any other reasons come to mind?",
                          "Does that reason explain anything else?", "What other reasons might there be?"]
            reply = random.choice(reply_list)
        elif rep_num == 22:
            reply_list = ["Please don't apologize!", "Apologies are not necessary."]
            reply = random.choice(reply_list)
        elif rep_num == 23:
            reply_list = ["What does that dream suggest to you?", "Do you dream often?",
                          "What persons appear in your dreams?", "Are you disturbed by your dreams?"]
            reply = random.choice(reply_list)
        elif rep_num == 24:
            reply_list = ["How do you do.  Please state your problem."]
            reply = random.choice(reply_list)
        elif rep_num == 25:
            reply_list = ["How do you do.  Please state your problem."]
            reply = random.choice(reply_list)
        elif rep_num == 26:
            reply_list = ["You don't seem quite certain.", "Why the uncertain tone?", "Can't you be more positive?",
                          "You aren't sure?", "Don't you know?"]
            reply = random.choice(reply_list)
        elif rep_num == 27:
            reply_list = ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?",
                          "Are you sure?", "Why no?"]
            reply = random.choice(reply_list)
        elif rep_num == 28:
            reply_list = ["Why are you concerned about my *", "What about your own *"]
            reply = random.choice(reply_list)
        elif rep_num == 29:
            reply_list = ["Can you think of a specific example?", "When?", "What are you thinking of?",
                          "Really, always?"]
            reply = random.choice(reply_list)
        elif rep_num == 30:
            reply_list = ["Do you really think so?", "But you are not sure you *", "Do you doubt *"]
            reply = random.choice(reply_list)
        elif rep_num == 31:
            reply_list = ["In what way?", "What resemblence do you see?", "What does the similarity suggest to you?",
                          "What other connections do you see?", "Could there really be some connection?", "How?"]
            reply = random.choice(reply_list)
        elif rep_num == 32:
            reply_list = ["You seem quite positive.", "Are you sure?", "I see.", "I understand."]
            reply = random.choice(reply_list)
        elif rep_num == 33:
            reply_list = ["Why do you bring up the topic of friends?", "Do your friends worry you?",
                          "Do your friends pick on you?", "Are you sure you have any friends?",
                          "Do you impose on your friends?", "Perhaps your love for your friends worries you."]
            reply = random.choice(reply_list)
        elif rep_num == 34:
            reply_list = ["Do computers worry you?", "Are you frightened by machines?", "Why do you mention computers?",
                          "What do you think machines have to do with your problem?",
                          "Don't you think computers can help people?", "What is it about machines that worries you?"]
            reply = random.choice(reply_list)

        return reply


    def buildreply(self, sentence: str):
        rh_sent = sentence.split()
        reply_num = int(rh_sent[0])
        rh_reply = self.list_to_string(rh_sent[1:])
        lh_reply = self.getreply(reply_num)
        full_reply = lh_reply
        if lh_reply[-1] == '*':
            full_reply = lh_reply[:-1] + rh_reply + "?"
        return full_reply


if __name__ == '__main__':
    eliza_inst = Eliza(0)
    eliza_inst.eliza()
