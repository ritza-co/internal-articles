---
hide:
- navigation
---

# Trying to teach Claude my daily workflows

I love learning about new AI tools and seeing what I can automate in my day-to-day life. I use AI, but I've never let it actually take control of my browser. When a work friend told me about a Claude skill that lets you prompt Claude Code to control your browser, I was excited to try it.

## Starting with my email

I installed the Claude dev-browser skill and gave it a task to see how it worked: unsubscribing from some marketing emails in Gmail.

It was hard to watch. Claude took screenshots constantly, eating up my precious tokens, and couldn't figure out how to access the new tabs it opened. I tried some prompt engineering in a second attempt, and it successfully unsubscribed from a marketing email, but that felt like dumb luck.

<video src="../assets/ai-browser-automation/unsibscribe-email.mp4" controls type="video/mp4"></video>

I tried to continue with more emails, and it fell apart.

I could have manually unsubscribed from ten emails in the time I spent debugging this. I guess Gmail's UI is just too complex for this kind of task.

## Trying a predetermined workflow

I thought I'd try a different task with more structure. I created a predetermined workflow for Claude to follow: check my Slack messages, navigate to my task management board, and start my time tracker.

The nice thing about the dev-browser skill is that it uses my actual logged-in browser sessions. Claude checked my Slack messages without any authentication issues. It navigated to my task management software, found the tasks assigned to me, read them, and determined what to research for my next instruction.

I had asked it to start my time-tracking software next. Once again, Claude had trouble with the UI. It took a long time to start the tracker and eventually navigate to a website to begin research.

<video src="../assets/ai-browser-automation/research.mp4" controls type="video/mp4"></video>

The simple, predetermined workflow was better than the Gmail experiment, but Claude still required a lot of hand-holding and struggled with some UIs more than others.

## Trying Stagehand

I'd heard about a tool called Stagehand that supposedly allows agents to navigate browser UIs more efficiently. Since the Claude skill required so much supervision, I decided to try writing some Stagehand scripts instead.

I'm planning a trip, so it would be useful to have something check flight prices for me. I found a Google Flights page showing Greek destinations from Johannesburg with their prices.

First, I explored the page using the Claude skill. That took maybe five minutes.

Then, I wrote a Stagehand script to automate the same extraction. It took about 7 seconds.

[Screenshot: Google Flights page with extracted data]

I figured I could use the Claude skill to explore the workflows and UIs, then use Stagehand to automate the process.

## The autonomous agent experiment

I wanted to see if Stagehand could navigate an entire workflow autonomously – not just extract data from a page I'd opened, but actually search for flights across multiple destinations, fill forms, handle date pickers, compare prices, and give me a recommendation.

I wrote a script that gave the agent the goal of finding the cheapest flight from Johannesburg to four different Greek islands.

I expected Stagehand to handle one or two searches before getting confused, but it worked really well.

The agent searched all four destinations and gave me a recommendation.

<video src="../assets/ai-browser-automation/flights-local.mp4" controls type="video/mp4"></video>

The agent found form fields without hardcoded selectors. It handled autocomplete and date pickers.

This felt different. I gave it a goal, and it figured out how to achieve it.

## Deploying to the cloud

The flight search worked well, but I had to sit there and watch it run. Next, I wanted to see whether it could run automatically every morning and alert me when prices drop.

I'd heard about a company called Kernel that provides cloud infrastructure for browser automation. Perhaps I could use Kernel with GitHub Actions to run the Stagehand script on a schedule.

I took the exact script that worked locally and deployed it to Kernel with a GitHub Actions workflow.

<video src="../assets/ai-browser-automation/cloud.mp4" controls type="video/mp4"></video>

The local version worked perfectly. But in the cloud, it struggled. The first search completed fine. Then the second search failed.

I'm not entirely sure why. After the first search, Google Flights changed state, and in the cloud environment, the agent couldn't adapt the way it had locally.

I watched the cloud browser in real time through Kernel's live view. Although cool and helpful for seeing what was happening, it didn't reveal why the agent made the choices it did.

## What I learned

Autonomous agents aren't deterministic. The same code with the same task doesn't guarantee the same results.

The "works on my machine" problem applies to AI agents too. Autonomous agents are powerful, but they're not magic.

There are things that might make this work better: simpler tasks, navigating back to the homepage between searches, using video replays for debugging, a fallback strategy, and trying a website with a simpler UI.

Stagehand's autonomous navigation is impressive when it works. Watching an agent navigate Google Flights, handle complex forms, and compare four destinations without any hardcoded selectors was genuinely cool.

The Claude skill's extension mode works well for accessing logged-in sessions. That's useful, and it's something you can't do easily with some simple scraping scripts.

## Where this is headed

This feels like early-stage technology with rough edges and massive potential.

The tools exist. The capabilities are real. The challenge is making them reliable.

I'm cautiously optimistic. Better debugging tools will make troubleshooting easier, and agent models may get better at state management.

If you want to try these tools yourself:

- **dev-browser:** https://github.com/sawyerhood/dev-browser
- **Stagehand:** https://github.com/browserbase/stagehand
- **Kernel:** https://kernel.ai
