import praw
from random import *
from flask import Flask, render_template


app = Flask(
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/')
def home(): 
	
	reddit_read_only = praw.Reddit(client_id="aPee9PV4m46RnXhZy2OFIg",
	client_secret="GfpuhUwyQM2Ll2j3CmKumCyvD34x_A",
	user_agent="RandomShitposts")

	subreddit = reddit_read_only.subreddit("shitposts")

# Display the name of the Subreddit
	# print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
	# print("Title:", subreddit.title)

# Display the description of the Subreddit
	# print("Description:", subreddit.description)

	posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

	posts_dict = {"Title": [], "Post Text": [], "Post URL": []}

	for post in posts:
    # Title of each post
		posts_dict["Title"].append(post.title)

    # Text inside a post
		posts_dict["Post Text"].append(post.selftext)

    # URL of each post
		posts_dict["Post URL"].append(post.url)

	post_title = posts_dict["Title"][randint(0, len(posts_dict["Title"]))]
	post_url = posts_dict["Post URL"][randint(0, len(posts_dict["Post URL"]))]

	# print(post_url)

	return render_template('index.html', post_url=post_url)
  	
	
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
	)