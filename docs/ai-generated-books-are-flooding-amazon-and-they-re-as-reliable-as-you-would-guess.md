---
title: AI-generated books are flooding Amazon (and they're as reliable as you would guess)
hide:
  - navigation
---

# AI-generated books are flooding Amazon (and they're as reliable as you would guess)

As `low_tech_love` pointed out [on Hacker News](https://news.ycombinator.com/item?id=35687868), an author called Tom Lesley has pushed out over 40 tech books already this year, and we're not even done with April yet. 

These books have titles like "Web Developer : Learn how to create web applications in Python using frameworks like Django, Flask, and Pyramid", and cover topics ranging from Python, through data science, and onto things like "Internet of Things".

I wrote a tech book once, and it took many many months, so it already seems likely that Tom is getting a lot of help from either many other humans or from a large language model such as GPT4.

Let's do some digging.

## "As a large language model"

One [HN commenter](https://news.ycombinator.com/item?id=35687868) already pointed out [a review](https://www.amazon.com/product-reviews/B0BWVH451G) that shows a video of the "Internet of Things" book with an excerpt reading "As an AI language model", a phrase associated with GPT4 which tends to use this when you ask it for some output that is beyond its capabilities or goes against its ethical restrictions.

It's already interesting to me that someone has the technological sense to set up a publishing pipeline using GPT and hooking it into Amazon, but somehow can't (or doesn't see the need to) do some basic filtering for obvious mistakes like this.

## Looking at the sample for "Web Developer"

I've written a bunch of articles about Django and Flask before, so I picked the "Web Developer" book which covers different Python frameworks and opened up the free sample.

Early on is a comparison of different Python frameworks. The red bits are misleading or wrong -- neither Flask nor Django follows the MVC pattern that other frameworks use, Pyramid doesn't include a CRM but rather integrates with SQLAlchemy and other ORMs.

![](https://i.ritzastatic.com/images/f6c930632dd04d8da0bd642f1de9ffb9/upload_23a81439922c92b3a66e44f52e88262d.png)

This is pretty standard AI stuff - mainly right, but with small details that are wrong. The one that jumps out more at me is that Pyramid is free software so "pay only for what you use" doesn't make any sense.

With a bit of Google-fu, we can find a tech consulting firm called Pyramid that uses this phrase though, which is probably what confused the language model -- not a mistake a human would be likely to make.

![](https://i.ritzastatic.com/images/7ebaee8eda804ad19bf5b02aadd8ddd9/upload_c0a3c17af890e2ed1cb499aab2fff19c.png)

## Does AI threaten technical writers? 

Language models are good at explaining code and generating code samples, both of which are key ingredients in a lot of technical writing. But we're still far from the point where AI can generate entire articles or books.

I've written before about how [verification is as hard as creation](https://ritza.co/articles/verification-is-as-hard-as-creation-chatgpt/) and while I was very impressed by GPT4 and [its ability to generate technical articles](https://ritza.co/articles/verification-is-as-hard-as-creation-chatgpt/), I think it's going to be a few years at least until AI can perform the tasks of even a very junior technical writer.
