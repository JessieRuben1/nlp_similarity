# Importing the spacy library.
import spacy

# Loading the english language model and then comparing the similarity between the words.
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Comparing the similarity between the words.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#Working with Vectors
# Comparing the similarity between the words in the sentence.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Working with sentences
# A sentence that we are comparing to the other sentences.
sentence_to_compare = "Why is my cat on the car"

# Creating a list of sentences.
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Creating a model of the sentence to compare.
model_sentence = nlp(sentence_to_compare)

# Comparing the similarity between the sentence_to_compare and the sentences in the list.
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
    

#Note: The similarity between cat and monkey is high, maybe beacause they are animals, also the similarity between monkey and banana is also
#high, this could be because the two are always associated. But the similarity between cat and banna is low.
#An example of high similarity would be cat and lion. 
#Also the similarity compares the context of the sentences, and if the context is the same the similarity score
#will be higher. 