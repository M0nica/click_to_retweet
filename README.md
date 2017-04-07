# click_to_retweet
A Flask application that allows you to search Twitter for tweets and then click to RT. Additionally, the app generate shareable links of the desired tweet with Twitter's RT parameters. 

`getTweets():`

Uses Twython to search Twitter for tweets (or manually input tweet url); the tweets are then rendered and a `click to tweet` link is generated with the option to `click to tweet` or to share the `click to tweet` link.

The `click to tweet` link when clicked it will direct people Twitter and confirm that they would like RT the specified tweet.
