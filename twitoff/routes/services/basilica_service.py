
from basilica import Connection
import osfrom dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

if __name__ == "__main__":

connection = Connection(API_KEY)
print("CONNECTION", type(connection))

sentences= ["This is a sentenc", 
            "This is a similar sentence",
            "I don't think this sentence is very similar at all..."
            ]


    embeddings = list(connection.embed_sentences(sentences))
    print(embeddings)


    embedding = connection.embed_sentence("Hello World!", model="twitter")
    print(type(embedding))
    print(type(embedding[0]))
    print(len(embedding))