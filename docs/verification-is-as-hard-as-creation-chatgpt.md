---
hide:
  - navigation
---

# Verification is as hard as creation: where ChatGPT falls short

Creating pretty much anything digital got a lot easier over the last twelve months: text, images, code, videos, audio. Whatever you want, there's an AI model to generate it for you now, quickly and cheaply.

ChatGPT got the most attention for its ability to generate text and code. Are writers out of a job?

## Taking a look at translation

Translation as an industry already had their ChatGPT "revolution". Machine translation accuracy has steadily improved over the last few years, reaching accuracy rates in the high 90s for many language pairs. And yet the Swiss government still employs thousands of translators to produce millions of documents in German, French, Italian, and English. The translators I know in Switzerland use specialised translation software to make the process easier, but this is more focused on letting them re-use their _own_ translations, rather than integrating automatic translation from Google Translate or DeepL.

Why? 

Well, it turns out that "high 90s" accuracy isn't good enough. And once you're verifying every single sentence of a translation, it takes as much effort as just doing it yourself. But it's considerably more boring and the AI's suggestions can make a translator doubt their own knowledge, spending more time to verify that they are right and the AI is wrong when they disagree.

## With creation, verification comes free

If you create something, or get someone you trust to create it for you, you get verification for free. Currently, if an AI generates something, you might be fairly sure that it is correct or high quality, but you can't _know_. 

Of course, this problem exists with people too. People make mistakes and they lie. But we can build trust in people over time. It's hard to fire ChatGPT for lying.

## ChatGPT is very confident

If you ask a person to write you a summary of something, they might say something like "I don't know", or "I'm not sure if this is right, but...".

ChatGPT does this sometimes, but sometimes it just makes stuff up completely. In the example below, I asked it to summarize some security vulnerabilities for me. It knows that it can't help me with the one reported in 2023, but it just makes up information for the one from 2020, which was actually related to nginx. It looks like ChatGPT is summarizing [CVE-2019-17026](https://nvd.nist.gov/vuln/detail/CVE-2019-17026) instead.

![Chat CVE](https://i.ritzastatic.com/images/d8832f3a7c774e8aa4fb7a2f9606894f/chatcve.png)

A human might have made some smaller mistakes, but it is unlikely that they would have so confidently made such a big mistake.

## So is AI 'just predictive text' or 'paradigm shifting'?

I've seen a lot of arguments at both extremes, from people claiming that ChatGPT and related models are basically just party tricks with very little value, to those claiming that they will kill the services economy.

"The real answer is probably in between the extremes" is never a very interesting take, but whatever your predictions for the impact on AI, I think it is useful to separate analysis into "creation" and "verification". We've gotten used to getting verification for free, and I expect quality assurance and similar roles to get a lot more popular as we realise that some content is valuable and some isn't, and it's hard to know which is which no matter who or what produced it.

For example, Grammarly suggested that I change the previous sentence to " that some content is valuable and some aren't" and needed me, a human, to verify that suggestion.

