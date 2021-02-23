import tkinter as tk
#import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    #nltk.download('punkt')
    url = URL.get("1.0","end").strip()

    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete("1.0","end")
    title.insert("1.0", article.title)
    author.delete("1.0", "end")
    author.insert("1.0", article.authors)
    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete("1.0","end")
    sentiment.insert("1.0",f"Polarity:{analysis.polarity}, Sentiment:{'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral'}")

    title.config(state='disabled')
    author.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


root = tk.Tk()
root.title("News Summarizer & Sentiment Analysis")
root.geometry('800x600')
root.resizable(0,0)
#root.config(bg='black')

fontHeader = ("KG HAPPY", 16,)

label1 = tk.Label(root, text='Title', font=fontHeader)
label1.pack()
title =tk.Text(root,height=1.5,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

label2 = tk.Label(root, text='Authors', font=fontHeader)
label2.pack()
author = tk.Text(root,height=1.5,width=140)
author.config(state='disabled',bg='#dddddd')
author.pack()

label3 = tk.Label(root, text='Summary', font=fontHeader)
label3.pack()
summary = tk.Text(root,height=10,width=140)
summary.config(state='disabled',bg='#dddddd')
summary.pack()

label4 = tk.Label(root, text='Sentiment Overview', font=fontHeader)
label4.pack()
sentiment = tk.Text(root,height=1.5,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

label5 = tk.Label(root, text='Paste your URL here!', font=fontHeader)
label5.pack()
URL = tk.Text(root,height=1.5,width=140)
#URL.config(bg='#dddddd')
URL.pack()

button = tk.Button(root, text="Summarize!",font=fontHeader,command=summarize)
button.config(bg='orange')
button.pack()


root.mainloop()