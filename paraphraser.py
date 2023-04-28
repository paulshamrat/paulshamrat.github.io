import nltk
from nltk.corpus import wordnet

# Download necessary resources
nltk.download('wordnet')
nltk.download('punkt')

# Function to get synonyms of a word
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

# Function to paraphrase a sentence
def paraphrase_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    new_tokens = []
    for token in tokens:
        if len(token) > 3:
            synonyms = get_synonyms(token)
            if synonyms:
                new_tokens.append(synonyms.pop())
            else:
                new_tokens.append(token)
        else:
            new_tokens.append(token)
    return ' '.join(new_tokens)

# Test the paraphrase_sentence function
sentence = "I went to the park to play with my dog"
paraphrased_sentence = paraphrase_sentence(sentence)
print(paraphrased_sentence)
