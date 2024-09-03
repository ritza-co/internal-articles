---
hide:
  - navigation
---

# Analysing 10 years of 'who is hiring' HN data

Every month [Hacker News](https://news.ycombinator.com) starts two threads

* "Who is Hiring" - a place for companies to advertise tech roles that they are hiring for
* "Who wants to be hired" - a place for tech workers looking for jobs to post their skills and what they are looking for

These have been posted regularly for the last ten years now. There have been a [few other attempts](https://hn.algolia.com/?q=who+is+hiring+data+) at analysing the data and drawing conclusions from it, but none that did exactly what I was looking for, so here's a new one.

## Are there more positions or candidates?

While 'who is hiring' has always been more popular, the number of comments on the 'who is hiring' thread has trended down over the last several years.

By contrast, the 'who wants to be hired' threads have been growing more popular.

As you might expect, they often move in opposite directions. In the 'hot' tech market after covid, fewer people were looking and more people were seeking.

![](https://i.ritzastatic.com/images/a311cabe015a4124850b11462d61c2d9/who-is-hiring.png)

The 'looking' line is the number of comments on 'who wants to be hired' threads; the 'hiring' line is the number of comments on 'who is hiring' threads.

If the trends continue, we might soon see the number 'looking' overtake the number 'hiring'.

Some (big) caveats:

* This data is just looking at the comment count for each thread. While these threads generally don't have much discussion, there is some, which means that not every comment is necessarily a job post or profile post.

![](https://i.ritzastatic.com/images/5968bbf01a60446484f6e4addb14427f/comment.png)

* The number of users on HN is probably growing, and most users are potential employees rather than potential hirers, so you'd expect an increase in 'looking' posts over time even if the number of jobs being offered was constant.

* HN is a pretty small bubble in the tech world, and most of the companies who post are smaller startups or scaleups (though I have seen posts from teams inside Apple and some other larger companies). This is probably not that representative of the number of job postings available

* HN tends to be pretty US-centric - although some European companies post on it too. It's rare to see companies advertising for jobs from other continents, though anecdotally I have noticed an increase in job seekers from Asia and Africa with the increase in acceptance of remote work in the last several years.

## Comparing with the FRED Indeed data

Another chart that shows an even stronger decline in tech job postings is from FRED (Federal Reserve Economic Data) which tracks job postings on Indeed. 

![](https://i.ritzastatic.com/images/6149ba30bdfd4a6783fa517bb6b65ae4/fred-software.png)
[_software job postings on indeed in the US_](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE)

I thought this might show the decline of Indeed as a place where companies advertise jobs rather than as a decline of the tech job market, but luckily they have a separate graph for "job postings on Indeed" that isn't tech specific, so we can compare.


![](https://i.ritzastatic.com/images/109e51cfddf846f9bbc795735fc043b1/fred-all-jobs.png)

[_jobpostings on indeed in the US_](https://fred.stlouisfed.org/series/IHLIDXUS)

It looks like tech jobs might be in trouble, though as always some more caveats

* Maybe **tech** companies post less on Indeed now?
* This data only goes back to 2020 and the last few years have been anything but typical 
* This is explicitly only for the US.

## How I scraped the data

HN has an API but I was too lazy to figure out how to use it and rebuild the comment trees.

Instead I asked GPT to do some webscraping for me. I've been using LLMs to help with smaller coding tasks since GPT2, and usually have been pretty disappointed with the amount of rework or iteration I have to do, but newer models are fantastic at things like this.

For anyone else living under a rock or claiming that LLMs can't code, this took me 5 minutes. As the owner of a [technical writing agency](https://ritza.co), I don't code as much as I used to, so I am not properly set up with Cursor or Sourcegraph or whatever coding assistant the cool kids are using these days. 

Instead, I have a script on my local machine called `coder.py`. It looks like this

```python
import os
import sys
import re

import requests

from datetime import datetime

from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(api_key='sk-...')

model = "gpt-4o"

def get_response(system_prompt, user_input):
    messages = [{"role": "system", "content": system_prompt}]
    messages.append(
        {"role": "user", "content": user_input},
    )

    completion = client.chat.completions.create(model=model, messages=messages)
    return completion.choices[0].message.content


if __name__ == "__main__":
    print(model)
    system_prompt = "You are a software developer. You take input code or data examples from the user as well as instructions. You output Python code as if written by an experienced software developer. You do not use OOP, but rather functions wherever possible. You output only Python code and always a single file. Your code does not have any comments. Your code does not contain any place holders. It is fully functional and runnable. You do not provide examples that the user needs to complete."

    prompt = """
    ...
    
"""

    print(get_response(system_prompt, prompt))
```

When I want to do something like this, I just describe what I want and put it into the 'prompt' string.

In this case, I spent a couple of minutes clicking 'view source' in my browser and copying a few relevant looking chunks of HTML.

I then added this as the prompt:

```
   HN posts several posts every month, namely 'who is hiring', 'who wants to be hired'. There are some others too, but I don't care about them.

    We can find these posts by starting at this URL

    https://news.ycombinator.com/submitted?id=whoishiring

    This will show the first 30 submissions.
   
    Each submission is divided into table rows. Here's an excerpt of the HTML

      <tr id="pagespace" title="whoishiring&#x27;s submissions" style="height:10px"></tr>
            <tr>
                <td>
                    <table border="0" cellpadding="0" cellspacing="0">
                        <tr class='athing' id='41425910'>
                            <td align="right" valign="top" class="title">
                                <span class="rank">1.</span>
                            </td>
                            <td valign="top" class="votelinks">
                                <center>
                                    <a id='up_41425910' class='clicky' href='vote?id=41425910&amp;how=up&amp;auth=7f0565672cd92042e3e88b848d1d85b8ce7535cf&amp;goto=submitted%3Fid%3Dwhoishiring'>
                                        <div class='votearrow' title='upvote'></div>
                                    </a>
                                </center>
                            </td>
                            <td class="title">
                                <span class="titleline">
                                    <a href="item?id=41425910">Ask HN: Who is hiring? (September 2024)</a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2"></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score" id="score_41425910">278 points</span>
                                     by
                                    <a href="user?id=whoishiring" class="hnuser">whoishiring</a>
                                    <span class="age" title="2024-09-02T15:00:06">
                                        <a href="item?id=41425910">1 day ago</a>
                                    </span>
                                    <span id="unv_41425910"></span>
                                     |
                                    <a href="flag?id=41425910&amp;auth=7f0565672cd92042e3e88b848d1d85b8ce7535cf&amp;goto=submitted%3Fid%3Dwhoishiring" rel="nofollow">flag</a>
                                     |
                                    <a href="https://hn.algolia.com/?query=Ask%20HN%3A%20Who%20is%20hiring%3F%20(September%202024)&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0" class="hnpast">past</a>
                                     |
                                    <a href="item?id=41425910">224&nbsp;comments</a>
                                </span>
                            </td>
                        </tr>
                        <tr class="spacer" style="height:5px"></tr>
                        <tr class='athing' id='41425909'>
                            <td align="right" valign="top" class="title">
                                <span class="rank">2.</span>
                            </td>
                            <td valign="top" class="votelinks">
                                <center>
                                    <a id='up_41425909' class='clicky' href='vote?id=41425909&amp;how=up&amp;auth=740ee304c00bd50ae8ad59ef54a5ea09fef2fd58&amp;goto=submitted%3Fid%3Dwhoishiring'>
                                        <div class='votearrow' title='upvote'></div>
                                    </a>
                                </center>
                            </td>
                            <td class="title">
                                <span class="titleline">
                                    <a href="item?id=41425909">Ask HN: Freelancer? Seeking freelancer? (September 2024)</a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2"></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score" id="score_41425909">20 points</span>
                                     by
                                    <a href="user?id=whoishiring" class="hnuser">whoishiring</a>
                                    <span class="age" title="2024-09-02T15:00:06">
                                        <a href="item?id=41425909">1 day ago</a>
                                    </span>
                                    <span id="unv_41425909"></span>
                                     |
                                    <a href="flag?id=41425909&amp;auth=740ee304c00bd50ae8ad59ef54a5ea09fef2fd58&amp;goto=submitted%3Fid%3Dwhoishiring" rel="nofollow">flag</a>
                                     |
                                    <a href="https://hn.algolia.com/?query=Ask%20HN%3A%20Freelancer%3F%20Seeking%20freelancer%3F%20(September%202024)&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0" class="hnpast">past</a>
                                     |
                                    <a href="item?id=41425909">96&nbsp;comments</a>
                                </span>
                            </td>
                        </tr>
                        <tr class="spacer" style="height:5px"></tr>
                        <tr class='athing' id='41425908'>
                            <td align="right" valign="top" class="title">
                                <span class="rank">3.</span>
                            </td>
                            <td valign="top" class="votelinks">
                                <center>
                                    <a id='up_41425908' class='clicky' href='vote?id=41425908&amp;how=up&amp;auth=5c4d185019bc49185ef0e4ed167e93041a0dc006&amp;goto=submitted%3Fid%3Dwhoishiring'>
                                        <div class='votearrow' title='upvote'></div>
                                    </a>
                                </center>
                            </td>
                            <td class="title">
                                <span class="titleline">
                                    <a href="item?id=41425908">Ask HN: Who wants to be hired? (September 2024)</a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2"></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score" id="score_41425908">133 points</span>
                                     by
                                    <a href="user?id=whoishiring" class="hnuser">whoishiring</a>
                                    <span class="age" title="2024-09-02T15:00:05">
                                        <a href="item?id=41425908">1 day ago</a>
                                    </span>
                                    <span id="unv_41425908"></span>
                                     |
                                    <a href="flag?id=41425908&amp;auth=5c4d185019bc49185ef0e4ed167e93041a0dc006&amp;goto=submitted%3Fid%3Dwhoishiring" rel="nofollow">flag</a>
                                     |
                                    <a href="https://hn.algolia.com/?query=Ask%20HN%3A%20Who%20wants%20to%20be%20hired%3F%20(September%202024)&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0" class="hnpast">past</a>
                                     |
                                    <a href="item?id=41425908">301&nbsp;comments</a>
                                </span>
                            </td>
                        </tr>
                        <tr class="spacer" style="height:5px"></tr>
                        <tr class='athing' id='41129813'>
                            <td align="right" valign="top" class="title">
                                <span class="rank">4.</span>
                            </td>
                            <td valign="top" class="votelinks">
                                <center>
                                    <a id='up_41129813' class='clicky' href='vote?id=41129813&amp;how=up&amp;auth=3403d9f8a3c14fce9fdaf00795c20448e251b9c7&amp;goto=submitted%3Fid%3Dwhoishiring'>
                                        <div class='votearrow' title='upvote'></div>
                                    </a>
                                </center>
                            </td>
                            <td class="title">
                                <span class="titleline">
                                    <a href="item?id=41129813">Ask HN: Who is hiring? (August 2024)</a>
                                </span>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="2"></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score" id="score_41129813">383 points</span>
                                     by
                                    <a href="user?id=whoishiring" class="hnuser">whoishiring</a>
                                    <span class="age" title="2024-08-01T15:00:34">
                                        <a href="item?id=41129813">33 days ago</a>
                                    </span>
                                    <span id="unv_41129813"></span>
                                     |
                                    <a href="https://hn.algolia.com/?query=Ask%20HN%3A%20Who%20is%20hiring%3F%20(August%202024)&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0" class="hnpast">past</a>
                                     |
                                    <a href="item?id=41129813">469&nbsp;comments</a>
                                </span>
                            </td>
                        </tr>
                        <tr class="spacer" style="height:5px"></tr>
                        <tr class='athing' id='41129812'>
                            <td align="right" valign="top" class="title">
                                <span class="rank">5.</span>
                            </td>
                            <td valign="top" class="votelinks">
                                <center>
                                    <a id='up_41129812' class='clicky' href='vote?id=41129812&amp;how=up&amp;auth=4684a3af1a023ece1d605bd77d37998762d5e2c6&amp;goto=submitted%3Fid%3Dwhoishiring'>
                                        <div class='votearrow' title='upvote'></div>
                                    </a>
                                </center>
                            </td>
                            <td class="title">
                                <span class="titleline">
                                    <a href="item?id=41129812">Ask HN: Freelancer? Seeking freelancer? (August 2024)</a>
                                </span>
                            </td>
                        </tr>
                        <tr>

            I want a CSV showing this data with columns for date (year and month), points, and comments. I want separate CSVs for the 'who is hiring' and 'who wants ot be hired' data (two csvs in total, all other posts can be ignored.

            To get to the next page, you can visit the URL at the bottom of each page called a 'morelink'. Here's an exceprt of the HTML showing the more link

                                    <tr>
                            <td colspan="2"></td>
                            <td class="subtext">
                                <span class="subline">
                                    <span class="score" id="score_38490809">180 points</span>
                                     by
                                    <a href="user?id=whoishiring" class="hnuser">whoishiring</a>
                                    <span class="age" title="2023-12-01T19:07:01">
                                        <a href="item?id=38490809">9 months ago</a>
                                    </span>
                                    <span id="unv_38490809"></span>
                                     |
                                    <a href="https://hn.algolia.com/?query=Ask%20HN%3A%20Who%20wants%20to%20be%20hired%3F%20(December%202023)&type=story&dateRange=all&sort=byDate&storyText=false&prefix&page=0" class="hnpast">past</a>
                                     |
                                    <a href="item?id=38490809">423&nbsp;comments</a>
                                </span>
                            </td>
                        </tr>
                        <tr class="spacer" style="height:5px"></tr>
                        <tr class="morespace" style="height:10px"></tr>
                        <tr>
                            <td colspan="2"></td>
                            <td class='title'>
                                <a href='submitted?id=whoishiring&amp;next=38099086&amp;n=31' class='morelink' rel='next'>More</a>
                            </td>
                        </tr>
                    </table>
                </td>

                Write me a Python script that uses requests and beautiful soup to download this data, parse it, and save it as a CSV file. Visit the first 100 pages or stop when a 'morelink' can't be found. Leave a random 0.5 to 1.5 second delay between making requests to avoid being blocked
```

Did I need the prompt to be this detailed or to have such a long example of the HTML? Probably not, but the value of LLM coding is that it doesn't matter - you can just write what you want without thinking about it too much and the LLM will probably figure it out.

Then I ran 

```
python coder.py > hnscraper.py && python hnscraper.py
```

Is it crazy to run randomly generated code without looking at it? A few years ago I'd have said absolutely. Now it seems routine.

It ran for a bit and then stopped.

I ran 

```
ls *.csv
```

and saw it had created two files for me.

```
who_is_hiring.csv		who_wants_to_be_hired.csv
```

I peeked inside them using [visidata](https://www.visidata.org):

`vd who_is_hiring.csv` 

It passed a few smell checks (dates were in order, none seemed to be missing, I spot checked a couple of comment counts against what I could see in my browser) so I uploaded those as separate tabs in a Google Sheet. I manually created a third sheet, and added formulas to pull in data from the two separate sheets. I added two columns with another formula for the three month average line, and inserted a chart.

I slightly changed the colours to match and made the three month average dotted, then I took a screenshot and pasted into this post.

Here's a link to the [Google Sheet with the raw data](https://docs.google.com/spreadsheets/d/1vrsqbHxNWsWXnGTe39vKpzfAbwzaSMGfPExPhJAc_Qo/edit?gid=432730222#gid=432730222).

Here's the code of the scraping script that GPT-4o wrote for me.

```python
import requests
import csv
import time
import random
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://news.ycombinator.com/submitted?id=whoishiring"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

def get_page(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_posts(soup, post_type):
    posts = []
    for item in soup.find_all("tr", class_='athing'):
        title_line = item.find("span", class_='titleline')
        if not title_line:
            continue
        title = title_line.text.lower()
        if post_type not in title:
            continue
        subtext = item.find_next_sibling("tr").find("td", class_='subtext')
        score_str = subtext.find("span", class_='score').text
        points = int(score_str.split()[0])
        age = subtext.find("span", class_='age').find("a").text
        comments_str = subtext.find_all("a")[-1].text
        comments = int(comments_str.split("\xa0")[0])
        date = subtext.find("span", class_='age')["title"]
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m")
        posts.append((date, points, comments))
    return posts

def scrape_post_type(post_type, output_csv):
    url = BASE_URL
    all_posts = []
    for _ in range(100):
        html = get_page(url)
        soup = BeautifulSoup(html, "html.parser")
        posts = parse_posts(soup, post_type)
        all_posts.extend(posts)
        morelink = soup.find("a", class_='morelink')
        if not morelink:
            break
        url = "https://news.ycombinator.com/" + morelink['href']
        time.sleep(random.uniform(0.5, 1.5))
    
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Points", "Comments"])
        writer.writerows(all_posts)

scrape_post_type("who is hiring", "who_is_hiring.csv")
scrape_post_type("who wants to be hired", "who_wants_to_be_hired.csv")
```

## Addendum

I've been reading these threads for nearly the whole decade covered in this data. I kind of new about the history that different people used to try to post it first to the get the karma before the `whoishiring` account became the official poster. I didn't realise that it wasn't actually an official initiative at all

Here's the [first post from that account](https://news.ycombinator.com/item?id=2391828) asking the community for buy in that the thread would be posted automatically. And [here's a post by dang](https://news.ycombinator.com/item?id=9635551) thanking the author and explaining that the account got made official and adopted by HN.

