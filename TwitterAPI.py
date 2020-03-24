import tweepy


consumer_key = "nhHrjqZwIjyYzU3xEmJuLuJIa"
consumer_secret = "pO903Og1uzV9njcWgudEDkMtI3seSdJtB5u26kOshLozbCSXHl"
access_token = "214375061-vxTrIRarPsDrHNinlHqNWCoxSEjCbvQCLG4BNrYy"
access_token_secret = "BSsWrm0NqeFiafZRIih9SlD9jZFNJroaBKXfcoZ9yKWMZ"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "google",
                           since = "2014-02-14",
                           until = "2014-02-15",
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)
csvFile.close()