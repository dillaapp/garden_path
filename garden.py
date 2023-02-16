import spacy

# Load the small English language model of spaCy
nlp = spacy.load('en_core_web_sm')


# Find at least 5 garden path sentences from the web or think up your own.
# Store the sentences you have identified or created in a list called gardenpathSentences
gardenpathSentences = [
    'The cotton clothing is made of grows in Mississippi.',
    'The chicken is ready to eat is raw.',
    'The police officer saw the drunk driver with a telescope chased him down.',
    'The magician had a rabbit that he pulled out of his hat was gray.',
    'The hunters shot the deer with rifles ran away.',
]

# Loop through each sentence in the list and perform entity recognition on its tokens
for sentence in gardenpathSentences:
    # Create a spaCy Doc object for the sentence
    doc = nlp(sentence)

    # Loop through each token in the Doc object and print its text and entity type
    for token in doc:
        # If the token has an entity type, print its text and the explanation of the entity type
        if token.ent_type_:
            print(token.text, token.ent_type_, spacy.explain(token.ent_type_))
        else:
            print(token.text, token.ent_type_)

    # Print a line of dashes to separate the output for each sentence
    print('------------------------')

# Two entities that I looked up were "LOC" (locations) and "NORP" (nationalities or religious or political groups).
# "LOC" appeared in the sentence "The police officer saw the drunk driver with a telescope chased him down." where "telescope" was identified as a location.
# It didn't make sense ....it's possible that spaCy was confused by the phrase "with a telescope" and thought it was referring to a location instead of an instrument.

# "NORP" appeared in the sentence "The cotton clothing is made of grows in Mississippi." where "Mississippi" was identified as a nationality or political group.
# It didn't make sense ....it's possible that spaCy was confused by the fact that "Mississippi" can also refer to a tribe of Native Americans, which would fall under the "NORP" category.
