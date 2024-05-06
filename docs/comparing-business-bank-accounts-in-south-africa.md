---
hide:
  - navigation
---

# Comparing Business Bank Accounts in South Africa

I've been running Ritza, a technical writing agency, for the last four years. It started as a sole proprietor in the Netherlands and then converted to a B.V. (equivalent to a South African PTY LTD) a couple of years in. Last year, we also registered a PTY LTD in South Africa as we hired some people there full-time, and wanted to move the contractors there under a local entity too.

As part of this, we needed a bank account. South Africa has a mixture of more traditional banks and more modern ones, but no proper "neo banks" like Revolut or Wise that I primarily use for transactional banking in Europe.

My requirements were pretty specific and uncommon, but I'm documenting them here and how each bank did or didn't meet them in case it's useful to someone else.

Here's a summary overview. Note that in cases where I didn't or couldn't sign up, I've filled out some of the features based on what I could find online, my experience using them for personal banking, and/or from reports from people I trust, but it's very possible I made some mistakes. Feel free to let me know if you disagree with any of them or have information about any that I've left as question marks.

![Business banks compared in South Africa](assets/comparing-banks-south-africa.png)

## Requirements

*Note, I didn't actually start with this list. Many of the below I realised were requirements when a specific offering failed to have them, so some of them might seem a bit contrived.*

- **Decent digital banking offering.** Some banks offer only a web app, some only a mobile application. Ideally I wanted both, but had a preference for "only web" if I had to choose, as a big part of business banking relies on uploading and downloading CSV files, which is clunky on a phone or tablet.

- **Bulk payments**. I really don't like repetitive manual work. Contractors and employees generally get paid once a month on the same day, so I want to be able to put in the amounts and references in a simple CSV file and bulk process them.

- **Signing up remotely and online.** I didn't want to have to go into a branch to open the account, or courier physical documents to South Africa.

- **Allows non-resident banking.** The SA entity is owned by a holding company in the Netherlands, which I own. This is a pretty simple structure, but complicated enough for it to be a sticking point with some banks, which either do not allow it or have different requirements.

- **Allows for corporate banking.** I thought this would be default, but some banks that advertise 'a bank account for your business' are restricted to sole proprietor structures.

- **Can send and receive international payments.** I thought this was kind of baseline these days, but some banks do not allow for receiving international payments via SWIFT. I learned that having a SWIFT code doesn't mean you can use it for SWIFT international payments.

- **Can make push payments to SARS.** Again, I didn't realise at the start that this wasn't a given. To pay tax in South Africa, you can't make a standard EFT payment. Instead you need special functionality built into the bank, and not all banks have this, or they only allow you to set up 'pull' payments through E-Filing, instead of 'push' ones initiated from the bank.

Additionally, I'd love to have some modern features that have become standard at neobanks I'm used to like Revolut at Wise, including

- **Virtual cards.** Easy to create different virtual cards for different purposes, and manage them online or in the app

- **Generally good UI.** No loading spinners, I can do everything I need without getting lost in sub menus or having to find documentation.

- **Reliability.** Not always 'down for maintenance', and doesn't crash or show errors in the app.

- **Customer support.** I don't want to have to wait in a queue to talk to a shitty chatbot that crashes half way through a conversation and makes me start over whenever I have a problem (looking at you FNB).

## What I am using at the moment (spoilers)

I haven't found a good option that meets all of the above yet and I'm still looking. The current combination I'm using is a combination of Bidvest and Bank Zero.

- **Bidvest** is more mature and offers good international payments, a web application with bulk payment processing, and a 'banker' -- an actual human who responds to my emails. However its web application is buggy and slow and annoying to use, breaks sometimes, it doesn't offer push payments to SARS, and no virtual cards or mobile application. 

- **Bank Zero** gave me some issues when I was signing up as they couldn't accept the foreign ownership structure. However their customer support on WhatsApp support was excellent and they quickly got management approval for an exception while they figured it out, and got some dev to run some custom SQL against their database to allow my foreign details which didn't match their expected format. This is both good (customer service yay) and terrifying (devs running custom SQL against prod for a company that manages money). They don't offer international payments, but they do have a mobile appilcation and can push to SARS, so I push money across from Bidvest to them for tax payments.

## Detailed comparison

I considered, reached out to, or tried the following banks.

## Bidvest

Currently using, see above. Overall it's OK but very clunky and old fashioned. Nearly everything you do on their web app shows you a loading spinner, even if it's loading a dropdown list of one element that should be static (e.g. 'select from account' where you only have one account). They mix up CSV and XLS formats. They have two separate banking portals that don't have a logical separation. You have to do 2FA via SMS which is not secure. Generally it's a mess, but it has the most features and I was largely happy at first, but soured over time.


- They encouraged me to open a 2-day notice account with a higher interest rate. As we transfer funds from the parent company at the start of the month and pay out contractors at the end, this made sense. They advised up front that there would be a form to fill out to give notice, but that my banker would handle it and all I had to do was email her. I did this and she told me to fill out the forms myself and send them somewhere else. They then ignored this request for nearly a week and only transfered the funds after several followups, which nearly caused issues with meeting payroll. Unacceptaable.

- Their bulk payments feature is very clunky. You have to use xlsx files instead of CSV (though of course the UI asks for a CSV), and then it processes each one in an obvious loop, so they appear one at a time in UI, one every 30 seconds or so, which feels delicate. It worked the first time, so I figured I could live with bad UX, but then last month it just broke and showed a loading spinner for over 30 minutes before I gave up. I asked my banker and she said I would need to call their technical support team about it, which I did not have the time or patience to do.

- No push integration to SARS, so I would have to try set it up via Efiling, which I don't have the patience for. Insteaad I have to transfer to Bank Zero, and push to SARS from there.

## Bank Zero

Currently using, see above. The UX is honestly the worst I have seen. Nothing makes sense and you have to push different parts of what looks like a single UI element on the app to get different functionality. Once you've figured out how to use it, it works, and I see fewer `Java.lang.NullPointerExceptions` randomly now, which is promising I guess?  It only has a mobile app, which apparently has a bulk payments feature, but I haven't tried it yet. I will it this month after last month's disaster with Bidvest.

Overall it has some features that are great, but I would not feel comfortable keeping any meaningful amount of money with them given how brittle and toy-like it feels.

## Investec

Everyone seems to think that they are the best in terms of features and cutomer support. However their already-high requirements are much higher for businesses and non-resident individual accounts, so I was rejected for both. These are the requirements I was given though I think they vary based on a number of factors so YMMV.

**Business requirements**

- A minimum of 30 million annual turnover
- A business in operation for a minimum of three years
- Minimum 5+ million Rands Net Asset Value.

**Non-resident individual requirements**

- Net Asset Value in access of £3 million or currency equivalent
- Cost to company of £300 000 or currency equivalent

## Others

- **Capitec** - responded to my first email, and then ghosted me despite several followups.
- **Nedbank** - responded to my first email, but needed docs notarized and couriered to South Africa.
- **Discovery** - only offers personal banking.
- **Thymebank** - only offers personal banking (even though they offer "for your business, it is only for sole props) and blocks non-SA IP addresses.

I did not consider the following as I have had awful experiences with them in the past.

- **Standard Bank** - literally impossible to close an account if you ever need to. No customer support. Even if you go into the branch to try and fix something that you've tried hours to fix via phone/email etc, then they just give you a phone and connect you to the same low-cost call center that you were trying to deal with before

- **First National Bank (FNB)** - generally awful customer support, no bulk payments, website and app get worse ever year. They are built up of dozens of internal departments and do not try to shield their customers from their convoluted structure at all so every time you try to do anything you will get bounced around between departments, nearly always in some kind of catch-22 loop.

- **ABSA** - this is probably the main player that I have the least experience with and know the least about, so maybe I should give them more serious consideration, but my overall impression is that they are similar to FNB/Standard bank.




