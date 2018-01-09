import requests, time

#Checks to see if the user wants to run the program
def runCrawler():
    running = ""
    while(running != "Y" or running !="N"):
        running = input("\nDo you want to try again or check out another subreddit? [Y/N]: ")
        if(running == "Y"):
            return True
        elif(running == "N"):
            return False

#Gets the subreddit the user wants to see for hot posts
def setThreadHot():
    subreddit = input("\nPlease enter the subreddit you are looking for: ")
    url = 'http://www.reddit.com/r/' + subreddit + '.json'
    return url

#Gets the subreddit the user wants to see for new posts
def setThreadNew():
    subreddit = input("\nPlease enter the subreddit you are looking for: ")
    url = 'http://www.reddit.com/r/' + subreddit + '/new/.json'
    return url

#Gets the subreddit the user wants to see for top posts
def setThreadTop():
    subreddit = input("\nPlease enter the subreddit you are looking for: ")
    url = 'https://www.reddit.com/r/' + subreddit + '/top/.json'
    return url

#Checks to see what the user wants to see(new, hot, top)
def threadType():
    type = ""
    while(type != "1" or type != "2" or type != "3"):
        print("\n1) Hot Posts \n2) New Posts \n3) Top Posts")
        type = input("\nWhat kind of posts would you like to see?: ")
        if(type == "1"):
            print("\n\u001b[31;1mLet's see the hot posts for this subreddit!\u001b[0m")
            break
        elif(type == "2"):
            print("\n\u001b[32mLet's see the new posts for this subreddit!\u001b[0m")
            break
        elif(type == "3"):
            print("\n\u001b[33;1mLet's see the top posts for this subreddit!\u001b[0m")
            break
    return type


#--------------------------------------------------START PROGRAM-------------------------------------------------------------
print("\u001b[36;1m\nWelcome to the Reddit Crawler!\u001b[0m\n")
print("This reddit crawler shows the title and URL of all the posts on a subreddit of your choice!")
running = True
while(running):
    type = threadType()
    #Sets URL to the correct reddit page
    if(type == "1"):
        url = setThreadHot()
    elif(type == "2"):
        url = setThreadNew()
    elif(type == "3"):
        url = setThreadTop()
    print("\u001b[32;1m")
    print(url + "\n")
    print("\u001b[0m")
    getAPI = True
    tries = 1
    while(getAPI):
        #If the program has tried several times and doesn't see the JSON in time, breaks the loop
        if(tries >= 10):
            print("\u001b[31mWe could keep trying but either this isn't a valid subreddit or Reddit is giving us the silent treatment.\u001b[0m\n")
            break
        #Gets the JSON info, iterates through to get the title and url of each post
        try:
            r = requests.get(url)
            data_search = r.json()
            if(data_search["data"]["before"] == 'None' and data_search["data"]["after"] == 'None'):
                print("Sorry, looks like this isn't a valid subreddit.")
                break
            test = data_search["data"]["children"]
            postnum = 1
            for post in test:
                print(str(postnum) + ") " + post['data']['title'])
                print("\t\u001b[32;1m" + post['data']['url'] + "\u001b[0m\n")
                #print('\tScore = ' + str(post['data']['score']) + "\n")
                postnum+=1
            getAPI = False
        except KeyError:
            time.sleep(1)
        tries+=1
    time.sleep(2)
    running = runCrawler()
print("\n\u001b[35;1mThanks for using my Reddit crawler! Have a good one!\u001b[0m")