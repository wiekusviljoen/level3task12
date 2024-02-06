import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

tokens = nlp('cat apple monkey banana ')
for tokenl in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)


# Similarities of cat, monkey, banana: 
# "cat" and "monkey" is more similar than "cat" and "banana" because both cats and monkeys are animals. This is how language models like spaCy's can understand and measure connections between words based on how they are commonly used together.

# Differences between "en_core_web_sm" and "en_core_web_md": 
# The "sm" model is smaller and more efficient, while the "md" model is larger and more comprehensive. Due to its smaller size, the "sm" model may provide faster processing but may lack some advanced features present in the "md" model.