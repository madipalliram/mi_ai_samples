def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

Sentence1 = "My Name is AB"
Sentence2 = "AB is my Name"

query=Sentence1.split(" ")
document=Sentence2.split(" ")
print(jaccard_similarity(query,document))