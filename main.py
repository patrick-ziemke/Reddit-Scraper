# r/TodayILearned scraper
# random fact generator

import praw
import tkinter
from tkinter.font import Font

# Get fact from r/TodayILearned Scraper Reddit API
# This API is soooo slow but it is the only one available...
def getFact():
    reddit = praw.Reddit(client_id='zid0IOqQ_OhU6A', \
                     client_secret='vVuqwoU_NuDSrolGQ55F8YiYX8E', \
                     user_agent='TILscraper', \
                     username='monsterback23', \
                     password='CFKLWcw7$')

    # choosing a random submission from r/todayilearned
    subreddit = reddit.subreddit('todayilearned')
    submission = subreddit.random()

    # parse title and remove 'TIL' tag from the beginning
    # also removing extra words
    print("Grabbing new fact ...")
    title = submission.title
    lst = title.split()
    lst.pop(0)

    # removing first word to increase sentence clarity, and capitalizing first word
    if lst[0] == 'of' or lst[0] == 'about' or lst[0] == 'that' or lst[0] == '-' or lst[0] == ':':
        lst.pop(0)
    lst[0] = lst[0].capitalize()
    fact = ' '.join(lst)
    print("Fact: " + fact)
    return fact

# button function for replacing fact with new fact
def newFact():
    text.delete(1.0, tkinter.END)
    text.insert(tkinter.END, getFact())

# tkinter GUI set up
root = tkinter.Tk()
root.geometry("650x500")
root.title('r/TodayILearned Scraper')

# styling tkinter root window

# WIDGETS BELOW
myFont = Font(family="Times New Roman", size=18)

titleTxt = tkinter.Text(root, height=2, width=30)
titleTxt.configure(font=myFont)
titleTxt.insert(tkinter.END, 'r/TodayILearned Facts')
titleTxt.pack()

text = tkinter.Text(root, height=12, width=30, pady=10, wrap='word')
text.configure(font=myFont)
text.pack()
text.insert(tkinter.END, getFact())
button = tkinter.Button(root, text="Random Fact", width=25, command=newFact)
button.pack()

root.mainloop()