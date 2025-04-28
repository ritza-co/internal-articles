---
hide:
  - navigation
---

# Bad (but common) LLM criticisms 

I'm 50/50 on whether AI is over or underhyped right now. 

## Overhyped?

Sometimes it feels like every single conversation is about AI. Friends who never used to talk about tech are talking about it. I hear AI conversations on the train. Every startup pivoted to AI. Every Enterprise rebranded to AI. 

And yet, at a high level there's very little evidence that AI has had a super meaningful impact on.. anything? Yes it can write code, but most software engineers I know are still working at the same jobs, which are mainly similar. Most universities are still running the same classes, and dealing with plagiarism and cheating in the same way. Indiehackers and SaaS founders are using AI a lot to write more code faster, but when I use their products, they still feel the same. They have the same interfaces, the same level of polish, and the same amount of features.

## Underhyped? 

Each model can do more than the previous one. I use LLMs every day to do things that would have taken me longer before, or to do things that I would not have been able to do before. [Job postsings](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE) for software engineers continue to decline. We're probably [still early](https://trends.google.com/trends/explore?date=all&q=google,chatgpt&hl=en-GB) in terms of ChatGPT adoption. People are figuring out how to build and integrate AI into new things all the time.

## AI discussion and debate is important

I know a lot of people who are 'all in' on AI, and a lot of people who are complete AI skeptics. The people I tend to align with the most have more nuanced or uncertain views somewhere in between ("ENLIGHTENED CENTERISTS"!!). It's clear the world doesn't really agree about what AI is or how important it is at the moment, so discussion and debate is important.

But there are also a lot of lazy criticisms that I don't think are at all valid. And it can be hard to differentiate [between an argument and a contradiction](https://www.youtube.com/watch?v=ohDB5gbtaEQ). So here's a list of bad criticisms that I think are uninteresting and don't add to the conversation. I'm mainly writing these down so I can link to them when I try to discuss these topics with people, to encourage less bad, boring AI discussion and leave space for more good, interesting AI discussion.

## Bad AI criticisms

### I asked for X but expected Y. I didn't get Y so LLMs are bad.

People think of AI as 

* I ask it to do something
* It tries to do it
* I judge whether it did it well or not

But there's a whole lot of murkiness around _how well you asked it_ and _how often you asked it_. LLMs have high variability, so you might be impressed or unimpressed by their output from one day to the next, even if you hold everything else equal. People also often have a mental model of what they expect as output for a given input, and then judge the LLM's output by how closely it matches their expectation. Sometimes the AI might produce an objectively 'good' output for a given input that is still very different from what the user wanted or expected, and this will lead the user to call the LLM 'bad'. It's not always obvious when an LLM output is just different from what was expected and when it is objectively worse than what was expected.

Some of this can be addressed by providing more detailed prompts. Often, if you want the LLM to do something that would have taken you 30-60 minutes to do 'by hand', you need to spend 5 minutes writing the prompt. People often spend 10 seconds writing the prompt and then 30 minutes shouting at the LLM to try again by giving it 5-10 word messages at a time. I generally feed LLMs a text file instead of using a chat interface, and I spend time 'composing' the prompt in the .txt file, similarly to how I'd write an email to someone - adding paragraphs of instructions, context, examples, and backspacing or retyping stuff as my mental model of what I want becomes clearer.

### I asked it for X and it did it badly, so LLMs are bad

There's a common meme since like the 1970s that AI is defined something like 

_AI: A machine that can do the things that humans can do that machines can't do_

So this definition moves all the time. At some point people thought that a computer that could beat the best human chess players would need to be intelligent. Once we got that, we said chess is just calculations, and a machine would need to be able to play Go to be truly intelligent. Now we have that too, and the definition just keeps retreating. Eventually people retreat to "oh but the AI doesn't have a soul", or "the AI doesn't have consciousness", and while these things may be true, they are very tricky claims. Philosphers have been debating for centuries whether humans really "have consciousness" and there isn't an easy way to prove whether something has or doesn't have consciousness. 

There's no doubt that LLMs today can do many things (create a web app, image, essay, mathematical proof, etc etc). Any one of these things might have been a multi-year PHD project just a few years ago, that culminated in a shitty proof-of-concept and hastily slapped "towards" prefix added to the thesis of "automatically creating web applications with neutral networks" or whatever. So if you're judging LLMs today by how well they perform on tasks that we wouldn't even have _attempted_ 2-3 years ago, then your criticism is bad and you should feel bad.

### I asked it for X and It made a really awful mistake like deleting my codebase or database so LLMs are bad

Humans are fallible. Interns (and senior engineers) at tech companies make $XXX,XXX mistakes all the time. People still hire interns (and senior engineers). Yes it's good to share widely the worst LLM mistakes so that people can prepare for them, but just because LLMs f up sometimes doesn't mean they are bad.

### It's just fancy autocomplete

I think it's very clear now that LLMs are pracitcally 'not just fancy autocomplete'. The differences in what you could do with your phone's keyboard or MS Word's autocomplete feature and what you can do with LLMs are evidently massive. If anyone fights me on this point, I'll extend this section, but I mainly see non-technical people who have barely used LLMs and are taking the ostrich strategy to pretend that they don't exist as using this talking point to explain why they are bad.

### `<more to come>` 

## Good AI criticisms

### The rate of improvement for LLMs has slowed

LLMs now are much better than they were 3 years ago. But it's not clear that they're fundamentally better. We've had years of refinement and tweaking and tuning and bigger models and different ideas (e.g. reasoning), and each of these has shown some improvement. But many people claim that it's evident that "LLMs are the worst they'll ever be" and that soon they'll be self improving and we'll see exponential improvements.

It's possible that LLMs can keep getting better as we feed them more data, and as they start to create the ideas and algorithms to improve LLMs further, but it's at all self-evident that there are no limits here. Current LLMs have ingested nearly all data that we have, and while there is ongoing research into augmenting this with synthetic (LLM-generated) data, it's not clear that LLMs can learn more from LLM-generated content. The internet is a wonderful resource that at this point contains approximately all human knowledge. LLMs now have this knowledge. We might be 'near the top of the S curve', or we might be only half way up. I think any argument (preferably with some evidence or new idea) that relates to the rate of improvement of LLMs is interesting.





 

