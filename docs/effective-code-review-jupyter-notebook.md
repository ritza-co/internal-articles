---
hide:
  - navigation
---

# Effective code reviews for Jupyter Notebooks

A recent large-scale study comparing Python code in Notebooks to scripts found that there were [more problems with best practices in Notebooks than in scripts](https://www.researchgate.net/publication/359646711_A_Large-Scale_Comparison_of_Python_Code_in_Jupyter_Notebooks_and_Scripts). 

Code reviews are one way to remedy this.

Through the practice of reviewing one another's work, you can increase the overall quality of the code, spot mistakes before they cause problems, and learn from one another.

When you review code, you are reviewing the content for high-level appropriateness (is this code broadly doing what it should be doing?), technical correctness and quality, and for style. Let's take a look at each of these aspects.

## Reviewing content

When reviewing notebook content, we aim to establish whether it achieves its overall intended purpose.

Some things to think about for high-level content review are:

* Does the notebook effectively meet the business or product requirements? <br>
Perhaps the notebook was written to do some analysis or build a model. How well has the code in the notebook met that goal? As a reviewer, do you have questions about your colleague's approach or suggestions for improvement?

* Is the choice of technical solution appropriate? <br>
Do the data processing, analysis, and modeling steps make sense? Consider this both on an algorithmic level and in the implementation details. For example, perhaps you think the notebook author should have dealt with NaNs differently or tried a different clustering algorithm or you know some caveats about the data quality. 

---
**TIP: Be humble**

Remember that your colleague is the one that did the work and you are looking in from the outside. It's good to ask questions or make suggestions with some humility - your colleague may have chosen their approach for a reason you haven't understood. 

---

* Is the notebook understandable? <br>
Unlike other forms of code, notebook code is often used as a form of lab book, a recording of an experiment or model development process. This makes the record of the process almost as important as the correctness of the code. You can also review for this, and ask your colleague to add explanations or visualizations or display data as needed. If a notebook is unmanageably long, you can suggest breaking it up into multiple notebooks. 

## Reviewing code correctness and quality

Once you've reviewed the content of the notebook, you'll want to review the code itself for correctness and quality.

Usually, the first step here would be to run the notebook yourself.

When you have ensured the notebook runs without error and produces the expected results, you can move on to reviewing the code in more detail. Some things to look out for are:

* Correctness <br>
Are there any glaring errors? 
Even if there are no glaring errors, read through the code carefully for more subtle errors. Also look out for edge cases, to check if the code will handle them without errors or incorrect results.

* Efficiency <br>
You may notice code that isn't strictly incorrect but it's inefficient. For example, inefficient code might iterate through the same large dataset twice or fail to use available vectorized operations.

* Security <br>
Check that there aren't any passwords or secrets in the notebook. Depending on your context, you may also check that no private customer data is exposed in a notebook. 

* Best practice <br>
Check that the code follows coding best practice. For Python code, this could include following the guidelines set out in the Python Style Guide, [PEP 8](https://peps.python.org/pep-0008/). Some best practice approaches include using descriptive variable naming, writing modular code, avoiding code duplication, not having unused variables, reusing variable names, not having unused imports, and keeping imports at the top of the notebook. Best practice is a big topic and overlaps with our next aspect of reviewing: style.

## Reviewing style 

Low stylistic quality is actually a predictor of code with low reproducibility and more errors. Code is written a few times, but read many times - so readability is vital. 

Style can differ from team to team, but the important thing is that there is consistency within your team.

Some possible team standards may include naming conventions, repository folder structure, how to use headings and explanatory sections in your notebooks, whether you are going to adopt style conventions such as [PEP 8](https://peps.python.org/pep-0008/), how to do [dependency management](https://blog.reviewnb.com/jupyter-notebook-reproducibility-managing-dependencies-data-secrets), visualization standards (for example, requiring axis labels), and how you do documentation.

Some style and best practice standards can be automated using tooling like [nbqa](https://nbqa.readthedocs.io/en/latest/). The best approach is to automate, but not everything can be automated - we still need to be actively reviewing each other's code.

---
**TIP: Starting out reviewing code**

Giving your first code review can be intimidating. If you can't find anything to comment on, a good option is to ask a clarifying question. Find some aspect of the code and ask about it, for example, "Why did you normalize the data before plotting it?" This is an opportunity for you to learn and for the code author to reflect on their approach.

---

## Practical tips

Let's finish off with some practical tips. Usually, you will do code reviews on an online version-control platform like [GitHub](https://github.com/) or [Gitlab](https://about.gitlab.com/). These platforms allow you to comment on each other's code, as a back-and-forth conversation, at any point in the code. 

Unfortunately, this isn't as easy for notebooks, because you can't comment on individual lines of the rendered notebook. There are some [workarounds](https://blog.reviewnb.com/how-to-add-comments-to-notebook-diffs-github/) for this, but the most streamlined way to do notebook reviews is using [ReviewNB](https://www.reviewnb.com/?utm_source=reviewnb_blog). ReviewNB integrates with your version-control platform and allows you to [comment inline on rendered notebooks](https://blog.reviewnb.com/commenting-and-discussion-on-jupyter-notebook/) so you can have code-review conversations directly in the notebook. 

The awkwardness of notebook code reviews on current version-control platforms is a real hurdle to meaningful code reviews. If you and your team are wanting to up your code reviewing game, ReviewNB is a great way to make it easier.
