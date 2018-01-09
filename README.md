# RedditCrawler.py
A reddit crawler designed to get the subreddit and scan the first page of hot, top, or new posts. The scan grabs the JSON data and parses through to find the relevant title and URL for each post. The URL should be clickable in most situations, but some web-based editors/consoles won't let you follow it (like pythonanywhere).

To use, choose what kind of posts you want to see, enter subreddit, enjoy.

#Note: I had to set a program sleep so it didn't continuoulsy ping reddit's API. I also set it to stop trying to ping if it tried too many times or would take too long. This usually happens when it's a bad subreddit.
