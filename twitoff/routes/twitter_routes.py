from flask import Blueprint, render_template, jsonify
from twitoff.models import db, User, Tweet, parse_records
from twitoff.services.twitter_service import twitter_api_client
from twitoff.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user(screen_name=None):
    print(screen_name)

    #api = twitter_api_client()

    twitter_user = twitter_api.get_user(screen_name)
    

    db_user = User.query.get(twitter_routes.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db_session.commit()

    
    tweets = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=150)
    print("TWEETS COUNT:", len(statuses))


    all_tweets = [status.full_text for status in tweets]
    embeddingS = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", LEN(embedding))


    for index, status in enumerate(tweets):
        print(index)
        print(status.full_text)
        print("____")

        embedding = embeddingS[index]

        embedding = basilica_api_client.embed_sentence(status, full_text, model="twitter")
        print(len(embedding))

        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id 
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)

    db.session.commit()

    return "OK"
