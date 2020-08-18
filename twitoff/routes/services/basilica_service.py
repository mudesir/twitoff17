#import basilica
from basilica import Connection


API_KEY = "f696bca3-4682-5f8a-a807-99682d8c72f1"


sentences= ["This is a sentenc", 
            "This is a similar sentence",
            "I don't think this sentence is very similar at all..."]


connection = Connection(API_KEY)


embeddings = list(connection.embed_sentences(sentences))


print(embeddings)