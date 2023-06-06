import nltk
import os
from dataclasses import dataclass

# setting nltk pickle file path
nltk.data.path.append(os.path.join(os.getcwd(),"nltk"))

@dataclass
class IdentifyPOS:
    def identify(self,string:str)->dict:
        
        paragraph_tokenized = nltk.sent_tokenize(string)
        verb_count = 0
        pronoun_count = 0
        noun_count = 0
        adjective_count = 0
        result = dict()
        for line in paragraph_tokenized:
            words = nltk.word_tokenize(line)
            tagged_words = nltk.pos_tag(words)
            for _, tag in tagged_words: # to get the word replce the placeholder with variable name
                if tag.startswith('V'):
                    verb_count +=1
                if tag.startswith('PR'):
                    pronoun_count +=1
                if tag.startswith('N'):
                    noun_count +=1
                if tag.startswith('JJ'):
                    adjective_count +=1

        result['Nouns'] = noun_count
        result['Pronouns'] = pronoun_count
        result['Adjectives'] = adjective_count
        result['Verbs'] = verb_count
        return result


if __name__ =="__main__":
    paragraph_1 = "Tenali Raman was once walking along a forest path when he was stopped by a merchant. “I’m looking for my camel which has strayed away. Did you see it passing by?” asked the merchant. “Had the camel hurt its leg?” asked Raman."
    paragraph_2 = "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."
    obj = IdentifyPOS()
    print(f"\n\nRunning Test Case 1 : \n{paragraph_1} \n")
    print(obj.identify(paragraph_1))
    print("*"*50)
    print(f"Running Test Case 2 : \n{paragraph_2}\n")
    print(obj.identify(paragraph_2))
    print("*"*50)