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
collaboration  requirement so he has to be possible to do asynchronous collaboration and this is something that software DevOps has got sorted and MLOps doesn't 
yet mostly and this means that I need to be able to if for example if if my colleague Chris is working on a model I need to be able to make a fork of that model 
and I need to be able to make changes to it without treading on Chris's toes so we both need to be able to collaborate asynchronously and and get useful work done 
now this has kind of influenced the design of what we're building to a large extent because because we believe very much in the sort of github pull request style 
of collaboration that the data scientists are familiar with and and there are some challenges in in making that possible for for ml and then finally the 
model development process has to be continuous and so there are a couple of things that I mean by this the first one is that the development process must 
be automatic the deployment process or it must be automatic so it must be possible to automatically deploy a model into a staging environment or 
production environment without manually emailing Jupiters and notebooks or or tensorflow files serialized test flow models 
around because as soon as you start doing things manually then it introduces this possibility for the human error and the other piece is that you have to be able 
to statistically monitor your models and this is interesting because monitoring models is specifically is quite different to monitoring regular software that 
you might deploy it as micro services and the reason for that is that when you monitor software you can monitor things like Layton sees an error 

rate but when you monitor Mike Rosario when you monitor models machine learning models they can be giving you perfectly normal latencies and perfectly normal error rates and the model can have gone 

completely haywire and the reason for that is basically if you already knew the right answer for what the model was predicting then you wouldn't need the 

model in other words the production data is unlabeled and so this means that it's challenging to understand the behavior room of your model once it's running in production so an example might be that I 

might have deployed a model for four autonomous vehicles that classify road signs and so you might have a bunch of cars driving around with models running on hardware in the cars and sensors 

cameras basically on the cars that are looking around for the road signs and if you already knew what road sign the sensor was looking at then you wouldn't need the model right but at the same time it means that it's hard to understand the behavior of the model of 

production and there are some solutions to this including looking at the statistical distribution of the classifications the model is making if it's a classifier and then you can say well if the actual distribution of classifications drifts very 

significantly from my expected distribution like the distribution that I used in training in the training set then maybe Paige a human like fire and alert and get a human to look at what's 

going on because either you deployed a bad model in which case well you need to know about it so that so that you can roll back and so that you can figure out what went wrong with the new deployed model or the world changed and 

especially with things like computer vision it's it's often surprising like how the models actually distinguish features in the data and and you can get stupid things like I 

the computer vision model might never have classified any or never it never be trained on any stop signs in the snow and for some reason it can't classify stop signs in the snow so suddenly it snows over a large part of the country and then your stop sign classifier stops 

working and obviously you're in trouble so you need to have that statistical monitoring so those are the requirements and and so I'm going to talk about how 

how we can try and address those requirements using ml ops tools 
