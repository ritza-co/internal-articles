---
hide:
  - navigation
---

# Rewrite git commits for vercel

If you use Vercel for tests and previews then you have to authorize everyone who commits to your git repo on Vercel separately. I assume this is also because of how Vercel pricing works on a per-user basis, but I haven't looked into it too much. This is the error you get if you open a PR containing commits from a non-approved user.

> Bob is attempting to deploy a commit to the Acme Team on Vercel.
> To accomplish this, Bob needs to request access to the Team.
> Afterwards, an owner of the Team is required to accept their membership request.
> If you're already a member of the respective Vercel Team, make sure that your Personal Vercel Account is connected to your GitHub account.

In some cases (for example, if you want to accept contributions from [Ritza](https://ritza.co) to your documentation, blog, or other developer-focused materials), you might want to add commits without approving the committer. Especially if there are many committers, and they don't all want to sign up for Vercel and/or you don't want to pay for that many new Vercel users.

One workaround for this problem is to rewrite the commit history of the branch and pretend that an authorized committer actually made all the commits. In this case, you might want to keep a history of the actual committers as git comments.

You can do this with the following script. Change `main` to whatever branch you usually open PRs to.

```bash
#!/bin/sh

# Switch to your branch

# Get the logging details from all commits that are in the current branch but not in main
log=$(git log `git merge-base HEAD main`..HEAD)

# Reset your branch to the state of main
git reset $(git merge-base HEAD main)

# Commit all changes as a new commit with the current user
git add .
git commit -m "Squashed Commit

$log"
```

This will create a single commit from all the commits that are in the active branch but not in main. It will recreate all the changes as one commit, authored as your (an authorized Vercel user) git user. 

I keep this script one level higher than the repo I need it to work on as `rewrite.sh`.

Also run

```
chmod +x rewrite.sh
```

to give it execute permissions.

If you have a file structure like this

```
/Users/g/git/my-repo-that-uses-vercel
/Users/g/rewrite.sh
```

Then from a terminal window in

```
/Users/g/git/my-repo-that-uses-vercel
```

You can run

```
git fetch origin
git checkout branch-with-third-party-commits
../rewrite.sh
```

This will rewrite all the commits as a single 'squashed commit' with your user, but preserve the history of the original commits (dates and real author) as part of the git commit message.

![demo](https://i.ritzastatic.com/images/f108eda312c24cc3a4041900cc946bcc/git-rewrite.png)

Of course there are downsides to this approach in that you a) rewrite git history (a big no-no in many people's eyes) and b) you can't actually interact with those commits as they aren't real commits any more - just a log of what it should have looked like.

But if your main goal is to accept third-party contributions and get past Vercel's bot, then this is an effective workaround.
