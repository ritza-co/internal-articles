---
hide:
  - navigation
---

# The MLOps Manifesto

*Based on a transcription of [https://www.youtube.com/watch?v=hqxQO7MoQIE](https://www.youtube.com/watch?v=hqxQO7MoQIE)*

We have a manifesto for MLOps. This is what we care about and why we get out of bed in the morning.

It consists of four tests:

* ♻️ **Reproducible:** Other people and teams should be able to reproduce your work months or years later without talking to you directly.
* 👩‍🏫 **Accountable:** We (and others) can trust the results of our model by recording exactly what data was used and how a decision was reached
* 👥 **Collaborative:** People can asynchronously fork and work on different models without creating a mess.
* 👉 **Continuous:** 

![The four tests for MLOps](https://cln.sh/YOsDpQ+)

You can kind of apply these tests to your own MLOps pipelines and you can form an opinion about how *mature* you are compared to the different the different 
requirements.


## Reproducible

The first requirement is that your model training and deployment pipelines have to be reproducible.Can someone else come along nine months later and retrain a model 
without talking to the original creator of that model?

Let's say an old version of TensorFlow on an old data set with on a hardware that is sufficiently equivalent that they can retrain the models within 
a few percentage points - then you've got a reproducible MLOps pipeline.

Nine months later you can't because you upgraded the version of TensorFlow on your development machines and the data has gone somewhere and you don't know where 
the data is gone the date has  changed in your production database then you've failed the reproducibility test.

If you fail the reproducibility test and you're in trouble from a governance and compliance perspective in some industries.

## Accountable

The second test is that an MLOps pipeline should be *accountable*. We think about accountability from the same perspective that we hold humans accountable for 
their decision-making process and one of the ways in which you do that is you to specify
* on what basis did you make your decision
* on what basis question with machine learning as a minimum requirement

not even going into the whole area of explain ability but as a minimum requirement you have to be able to say what version of the data was the model 
trained on so you need to be able to track the model back to the program where that model came from what data was trained on by whom and and so on the 
next point and it's especially pertinent at the moment is this 

## Collaboration
We want to do asynchronous collaboration. This is something that software DevOps has got sorted and MLOps doesn't yet.

For example, my colleague Chris is working on a model I need to be able to make a fork of that model and I make changes to it without treading on Chris's toes.

We need to collaborate asynchronously and and get useful work done. DevOps does this with a GitHub pull request style 
of collaboration that the data scientists are familiar with, but there are some challenges in making that possible for ML. 


## Continuous 
* Development should lead to **automatic deployment**: we should automatically deploy a model into a staging environment or 
production environment without manually emailing Jupiters and notebooks or TensorFlow files, or serialized test flow models, 
around because as soon as you start doing things manually then it introduces this possibility for human error.

* You have to be able to **statistically monitor** your models, and this is interesting because monitoring models is specifically is quite different to 
monitoring regular software. With regular software, you can monitor things like error-rates and know immediately if something is wrong. With machine learning 
models, they might give you perfectly normal latencies and error rates but the model itself has gone haywire. You can't verify a models **predictions** because 
if you could, you wouldn't need the model in the first place. That is, productdion data is **unlabeled**, so it's challenging to understand the behaviour 
of your model once it's running in production. You need to look statistically at e.g. the number of predictions it makes in certain classes, and if then 
page a human if the distribution varies from an expected distribution to make a call on if the world has chnaged or if the model has broken.

This is especially a problem in computer vision where you get stupid things like suddenly it starts snowing and now your self-driving car can't recognise stop
signs any more because it was never trained on identifying stop signs with snow in the background.
