---
title: Writings
excerpt:
---

As a science educator for Christians, the majority of questions I receive are about two topics: climate change and evolution. I've written a guide to climate change intended for people of any background, and am in the process of writing several more guides to evolution, the Big Bang, vaccines, and Genesis. I’m also exploring a series of devotionals based on science.
<p style="text-align: center;"> <h3>Climate Change: A Guide for the Perplexed</h3></p>
After receiving many questions about the topic, I wrote an introductory-level guide to climate change. It assumes no scientific background, and it’s ordered by topic so you can easily find what you’re looking for. If you don't believe in climate change, want to know more, or are just confused, this is for you.

{% include button.html text="Read the Climate Guide" link="/guide" color="#3366ff" align="center"%}


| ***Opinion Pieces*** | | ***The Coronavirus*** |
| :----------:         | | :-----:             |
| I wrote an Opinion piece in *the Tennesseean* arguing against the Trump administration’s attacks on clear air standards. [The Tennesseean, 2020](https://www.tennessean.com/story/opinion/2020/03/09/california-clean-car-standard-deserves-support/4980634002/) ![The Tennesseean](assets/images/Tennesseean.png) | | I wrote a scientific primer on the coronavirus in the early days of the pandemic. [Part 1 - The Science](/PartOneScience) ![matthewdgroves.com](assets/images/Logos/logo.jpeg) |
|  ||  |
| I argue that all Christians should take part in the Global Climate Strike as a duty to both God and neighbor. [The Christian Post, 2019](https://www.christianpost.com/voice/were-young-evangelicals-and-were-striking-for-the-climate-will-you-join-us.html) <br/> ![TheChristianPost](assets/images/Orgs/The Christian Post.png) | | A deeper exploration and explanation of the public health solutions being recommended during the lockdowns. [Part 2 - The Solutions](/PartTwoSolutions) ![matthewdgroves.com](assets/images/Logos/logo.jpeg) |
|  ||  |
| I wrote a Letter to the Editor critiquing the Trump administration’s attacks on the Endangered Species Act. [The Tennesseean, 2019](assets/LTETennessean.pdf) ![The Tennesseean](assets/images/Tennesseean.png)| | Reflections on the spiritual and theological nature of pandemics, suffering, community, and reading scripture in trying times . [Part 3 - The Spirituality](/PartThreeSpirituality) ![matthewdgroves.com](assets/images/Logos/logo.jpeg) |
|  ||  |
| "Jesus didn’t say anything about climate change, but he said plenty about how we should care for those whom society would prefer to forget.” [Baptist News Global, 2017](https://baptistnews.com/article/climate-change-gospel-issue-time-christians-acknowledged/) ![Baptist News Global](assets/images/BNG.png) || Climate, the Coronavirus, and Justice [Justice Unbound, 2020](https://justiceunbound.org/climate-the-coronavirus-and-justice/) ![Justice Unbound](assets/images/JusticeUnboundLogoBlack.png)|
|  ||  |
| When informed Christians ponder devastation from climate change that will affect millions of people for generations to come, it’s easy to lose hope for the future. But our actions still matter. We must not give up. [Baptist News Global, 2018](https://baptistnews.com/article/climate-nihilism-is-right-to-recognize-the-dire-situation-were-in-but-wrong-to-lose-hope/) ![Baptist News Global](assets/images/BNG.png) ||  |
|  ||  |

---
layout: base
---

# Responsive, Two Column Documentation Layout With Markdown and CSS

Markdown makes it easy to write and maintain documentation, but is normally limited to single column layouts. For documenting code, and on larger screens particularly, single column layouts do not utilize space well and separate explanatory text too much from code samples:

This page documents how to use plain old Markdown and CSS to achieve a responsive, two column layout, with code examples their explanations appear next to each other. It targets code documentation, but can easily be adapted to other contexts as well.

For maximum metaness, the page itself uses the two column layout it documents. More complete examples are demonstrated on the [Bennu][bennu] and [Nu][nu] project sites.

Checkout the complete code on [github][src]. It uses [Jekyll](http://jekyllrb.com). Simply run: `$ jekyll build` to build it.

<div class="begin-examples"></div>

## The Markdown
We'll abuse some Markdown elements to get the layout we want. You can choose to style your page differently, but here we'll have code examples on the right, and code explanations on the left.

### First, we need to tell Markdown where the two column layout begins.
Anything before this element will be rendered normally.

```
<div class="begin-examples"></div>
```

And we should also tell it where the two column layout ends.

```
<div class="end-examples"></div>
```

### `h2` will be an example section header.

```
## Section title
```

And any text directly after the section title will not be split into two columns.

```
## Section title
This text, along with the title, remains in a single column
```

### Each point in a section starts with an `h3`.

```
### Main you want to make point here
```

### Normal text elements (`p`) are used for more detailed explanations. 
You can put them after the main point.

``` 
### Main point
Some explanatory text.
```

### Code is interleaved with explanatory text.

The main point or explanation for a piece of code should come directly before it.

    ### Main point about code block 1

    ```
    code block 1
    ```

    More text explaining code block 2

    ```
    code block 2
    ```

## Styling
We can use CSS to style the Markdown output to create a two column layout when readers view our page on a larger screen.

### The main section and subsection headings both take up the entire width of the page.

```
article .begin-examples ~ h2,
article .begin-examples ~ h2 + p {
    width: 100%;
    clear: both;
}
```

### Each column element is 50% width

```
article .begin-examples ~ h3,
article .begin-examples ~ p,
article .begin-examples ~ .highlight {
    width: 50%;
}
```

### The left column has the main point and explanation text (`h3` and `p`).
We'll add some padding here too for good measure.

```
article .begin-examples ~ h3,
article .begin-examples ~ p {
    float: left;
    box-sizing: border-box;
    padding-right: 1rem;
    clear: both;
}
```

### While the right column has only the code examples `.highlight`.
And some spacing between the sections.

```
article .begin-examples ~ .highlight {
    float: right;
    clear: right;
    margin-bottom: 1rem;
}
```

### That's it!
But we have to ensure that nothing goes past the end of content.

```
.end-examples {
    clear: both;
}
```

### But we should clean up after ourselves.
Reset the styles to stop the two column layout. This must come after all the other styles in the CSS file.

```
article .end-examples ~ p,
article .end-examples ~ h3,
article .end-examples ~ .highlight {
    width: auto;
    float: none;
    clear: none;
}
```


## Style For Small Screens
Using a media query on screens less that 580px in width, we'll create a single column layout again. 

### All you have to do is reset the styling on the main elements of the two column layout

```
article .begin-examples ~ h3,
article .begin-examples ~ p,
article .begin-examples ~ .highlight {
    width: 100%;
    float: none;
    clear: none;
}
```

<div class="end-examples"></div>

# Conclusion
This example and the [source][src] intentionally keep any other fancy styling to a minimum, but it is very easy to style the two column layout. For styles that only apply inside the layout, add styles for `.begin-examples ~ * { }` and then reset them with `.end-examples ~ * { }`.



[Nu]: http://mattbierner.github.io/nu/
[bennu]: http://bennu-js.com

[src]: https://github.com/mattbierner/markdown-two-column-documentation-example






#+BEGIN_columns
#+ATTR_HTML: :width 60%
#+BEGIN_column
- My notes based on my partial understanding
#+END_column
#+ATTR_HTML: :width 40%
#+BEGIN_column
- Joined late in the project
#+END_column
#+END_columns