---
hide:
- navigation
---

# Trying to Teach Claude My Daily Workflows

I love learning about new AI tools and seeing what I can automate in my day-to-day life. I use AI, but I've never let it actually take control of my browser. When a friend at work told me about a Claude skill that lets you prompt Claude Code to control your browser, I was excited to try it.

## Starting with my email

I installed the skill and gave it a task just to see how it worked: unsubscribe from some marketing emails in Gmail.

It was hard to watch. Claude took screenshots constantly, eating up my precious tokens, and couldn't figure out how to access new tabs when they opened. I tried some promopt engineering on a second attempt and it successfully unsubscribed from a marketing email, but it really felt like dumb luck.

<video src="../assets/ai-browser-automation/unsibscribe-email.mp4" controls type="video/mp4"></video>

I tried to continue with more emails and it fell apart.

I could have unsubscribed from ten emails manually in the time I spent debugging this. I am guessing Gmail's UI is probably just too complex for this kind of task.

## Trying a predetermined workflow

I thought I'd try a different task with more structure. A predetermined workflow Claude could follow: check my Slack messages, navigate to my task management board, and start my time tracker.

The nice thing about this skill is it uses my actual logged-in browser sessions. Claude checked my Slack messages without any authentication issues. It navigated to my task management software, found my tasks assigned to me, read them and determined what to research for my nex insturction.

I had asked it to, at this stage, start my time tracking software. The UI there really gave Claude trouble and it took a long time before eventually getting it done, and navigating to a website to begin research.

<video src="../assets/ai-browser-automation/research.mp4" controls type="video/mp4"></video>

The simple predetermined workflow was better than the Gmail experiment, but it still required a lot of hand-holding and struggled with some UIs more than others.

## Trying Stagehand

I'd heard about a tool called Stagehand that supposedly allows agents to navigate browser UIs more efficiently. Since the Claude skill was requiring so much hand-holding, I thought I'd try writing some Stagehand scripts instead.

I'm planning a trip, so I thought it would be useful to have something check flight prices for me. I found a Google Flights page showing Greek destinations from Johannesburg with their prices.

First I explored the page using the Claude skill. That took maybe five minutes.

Then I wrote a Stagehand script to automate the same extraction. It took about 7 seconds.

[Screenshot: Google Flights page with extracted data]

I figured I could use the Claude skill for exploring the workflows and UIs, then use Stagehand for automating the process.

## The autonomous agent experiment

I wanted to see if Stagehand could navigate an entire workflow autonomously. Not just extract data from a page I'd opened, but actually search for flights across multiple destinations, fill forms, handle date pickers, compare prices, and give me a recommendation.

I wrote a script that gave the agent a goal to find the cheapest flight from Johannesburg to four different Greek islands for a trip I am planning later this year.

I expected it might handle one or two searches before getting confused, but it worked really well.

The agent searched all four destinations and gave me a recommendation.

<video src="../assets/ai-browser-automation/flights-local.mp4" controls type="video/mp4"></video>

The agent found form fields without hardcoded selectors. It handled autocomplete and date pickers.

This felt different. I'd given it a goal and it figured out how to achieve it.

## Deploying to the cloud

The flight search worked well, but I had to sit there and watch it run. I thought it would be useful to have this run automatically every morning and alert me when prices dropped.

I'd heard about a company called Kernel that provides cloud infrastructure for browser automation. I thought I could use it with GitHub Actions to run the Stagehand script on a schedule.

I took the exact script that worked locally and deployed it to Kernel with a GitHub Actions workflow.

<video src="../assets/ai-browser-automation/cloud.mp4" controls type="video/mp4"></video>

The local version had worked perfectly. But in the cloud, it struggled. The first search completed fine. Then the second search failed.

I'm not entirely sure why. After the first search, Google Flights changed state and the agent couldn't adapt in the cloud environment. Locally it had somehow managed this.

I could watch the cloud browser in real-time through Kernel's live view, which was cool and helpful for seeing what was happening in real time, but didn't reveal anything about why the agent made the choices it made.

## What I learned

Autonomous agents aren't deterministic. The same code with the same task doesn't guarantee the same results.

The "works on my machine" problem applies to AI agents too. Autonomous agents are powerful but they're not magic.

There are things that might make this work better. Simpler tasks. Navigating back to the homepage between searches. Using video replays for debugging. A fallback strategy. Or trying a website with a simpler UI.

Stagehand's autonomous navigation is impressive when it works. Watching an agent navigate Google Flights, handle complex forms, and compare four destinations without any hardcoded selectors was genuinely cool.

The Claude skill's extension mode works well for accessing logged-in sessions. That's useful and something you can't do with easily with some simple scraping scripts.

## Where this is headed

This feels like early-stage technology with rough edges and massive potential.

The tools exist. The capabilities are real. The challenge is making them reliable.

I'm cautiously optimistic. Better debugging tools will make troubleshooting easier and agent models might get better at state management.

If you want to try these yourself:
- **dev-browser:** https://github.com/sawyerhood/dev-browser
- **Stagehand:** https://github.com/browserbase/stagehand
- **Kernel:** https://kernel.ai
