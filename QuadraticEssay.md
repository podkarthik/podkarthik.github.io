# Quadratic Functions

This is an unconventional essay on quadratic functions. The content is not new and the ideas contained will be found in any standard mathematics textbook. What is new is the medium in which it is presented. This essay is an example of what is called a [mnemonic medium](https://numinous.productions/ttft/). This is an experimental concept introduced by Andy Matuschak and Michael Nielsen.

[toc]

## Parabola

Consider the following function:
$$
f(x) = x^2 - 3x + 2
$$
One way to get a concrete understanding of a function is to tabulate the values of $f(x)$ for different values of $x$:

| $x$  | $f(x)$ |
| ---- | ------ |
| $1$  | 0      |
| $2$  | 0      |
| $3$  | $2$    |
| $4$  | $6$    |
| $5$  | $12$   |

We have some data available with us. How do we analyze it? Recall that a function is just a technical term for a well defined relationship between two quantities. A good place to start is to see what happens to this relationship when we change one of these two quantities.

More concretely, as $f(x)$ has been defined in terms of $x$, it depends on $x$. In some sense, $x$ is free to assume whatever value it wants and is hence termed the independent variable. Now the question: what happens to $f(x)$ as $x$ changes? In particular, if we keep increasing $x$ by one unit, what happens to $f(x)$?

<orbit-reviewarea color="blue">
  	<orbit-prompt
    	question="What happens to $f(x) = x^2 - 3x + 2$ as $x$ increases?"
    	answer="$f(x)$ appears to increase"
	></orbit-prompt>
</orbit-reviewarea>

$f(x)$ *appears* to increase as $x$ increases. But is this the complete picture? What happens if $x$ is negative?

| $x$  | $f(x)$ |
| ---- | ------ |
| $-5$ | $42$   |
| $-4$ | $30$   |
| $-3$ | $20$   |
| $-2$ | $12$   |
| $-1$ | $6$    |

A different picture emerges. $f(x)$ seems to decrease for this range of values. Look at the two tables. Do you see any negative numbers in the second column? Can we conclude that $f(x)$ is always non-negative?



<orbit-reviewarea color="blue">
  	<orbit-prompt
    	question="Is $f(x) = x^2 - 3x + 2$ is greater than or equal to $0$ for all values of $x$?"
    	answer="No! What if $x = \cfrac{1}{2}$?"
	></orbit-prompt>
</orbit-reviewarea>

We must be wary of hasty generalizations in mathematics! We see that $f(x)$ decreases for a while and then starts increasing. Though the tabular approach has yielded some interesting insights, it is time to move to something more visual. What does the function look like? Let us plot the points $(x, f(x))$ on a graph and join them by a smooth curve. This is what we get:

<video controls loop autoplay muted>
    <source src="assets/PointsQuadratic.mp4" type="video/mp4" zoom=50%>
</video>


This beautiful curve is called a **parabola**. 

