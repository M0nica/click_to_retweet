from flask import Flask, render_template, redirect, url_for, request
from twython import Twython, TwythonError
import config
from flask import Markup


# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('entry.html')


@app.route("/entry", methods=['POST'])

def getTweets():
    word_to_search = format(request.form['word_to_search'])
    response = twitter.search(q=word_to_search + " -filter:retweets", result_type="recent", count=5)
    try:
        tweet_list = []
        for tweet in response['statuses']:
            tweet['text'] = "<div class='twitter-tweet'>"+ Twython.html_for_tweet(tweet) + '<a href="https://twitter.com/intent/retweet?tweet_id=' + tweet["id_str"] + '">Click to RT</a></div>'
            # print(tweet["text"], tweet["id_str"])
            tweet_list.append(tweet['text'])

        if len(tweet_list) > 0:
            results = " <br> ".join(tweet_list)
        else:
            results = "No tweets were found."

        results = Markup(results)


    except TwythonError as e:
        print(e)
    return  render_template('results.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)
