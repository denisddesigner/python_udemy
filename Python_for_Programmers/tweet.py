# Get list of twitter followers
import twitter
import random

api = twitter.Api(consumer_key="MvB6UQcURydZ2Rk7akuF8kPUv",
				  consumer_secret="JTBEaoZ4eX265ojTadW3G9AYJkD7ym35CCg9ERbs8aZJcL3LVE",
				  access_token_key="2782032722-ba2B9Mcp0jvRjd2u0jOQRjLW2tnyfx2ObA4kzIC",
				  access_token_secret="RikJRCPog75EKdlMhe0vTqhyV0u2mC0dDtaZG9u6XMfEV"
	)

followers = api.GetFollowers()
# print([u.name for u in followers])
# print(len(users))


# Choose 1 at random

randomIndex = random.randint(0,len(followers) -1)
randomFollower = followers[randomIndex]

print(randomFollower.screen_name)

# Tweet at them

tweet = "@{} you are the random follower of the day.".format(randomFollower.screen_name)
print(tweet)
api.PostUpdate(tweet)
print(tweet)
print("Thanks for tweeting!")