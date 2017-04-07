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
    response = twitter.search(q=word_to_search + " -filter:retweets AND -filter:replies", result_type="recent", count=10)
    try:
        tweet_list = []
        id_num = 0
        for tweet in response['statuses']:


            tweet['text'] = "<div class='twitter-tweet'>"+ Twython.html_for_tweet(tweet) + '</div>'
            # print(tweet["text"], tweet["id_str"])
            tweet_list.append(tweet['text'])


            ctt_text_area = '<div class="sharebuttons"><a href="https://twitter.com/intent/retweet?tweet_id=' + tweet["id_str"] + '">Click to RT</a> <button onclick="toggleLink(id)" id="button-'+ str(id_num)+'"type="button" class="btn btn-default">Get Click to RT Link</button> <span style="display: none;"><textarea rows="4" cols="50" id="button-'+ str(id_num)+'">' + "https://twitter.com/intent/retweet?tweet_id=" + tweet["id_str"] + '</textarea> <p>Share this link. When clicked it will direct people Twitter and confirm that they would like RT the specified tweet.</p></span></div>'
            tweet_list.append(ctt_text_area)
            id_num = id_num + 1

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
