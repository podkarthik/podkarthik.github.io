---
title: "Characteristic Polynomial"
author: "Karthik Thiagarajan"
format: revealjs
incremental: true
fontsize: 35px
margin: 0.05
width: 1600
height: 800
---

## Characteristic Polynomial

::: {.fragment}
Consider a matrix $A$ with an eigenpair $(\lambda, v)$:
:::

::: {.fragment .fade-in-then-out .absolute top="150" left="200"}
$$
\begin{aligned}
&Av = \lambda v\\
\end{aligned}
$$
:::


::: {.fragment .fade-in-then-out .absolute top="150" left="200"}
$$
\begin{aligned}
&Av = \lambda v\\\\
&Av = (\lambda I) v\\\\
\end{aligned}
$$
:::

::: {.fragment .fade-in-then-out .absolute top="150" left="200"}
$$
\begin{aligned}
&Av = \lambda v\\\\
&Av = (\lambda I) v\\\\
&(A - \lambda I) v = 0
\end{aligned}
$$
:::

::: {.fragment .absolute top="150" left="200"}
$$
\begin{aligned}
&Av = \lambda v\\\\
&Av = (\lambda I) v\\\\
&(A - \lambda I) v = 0\\\\
&|A - \lambda I| = 0
\end{aligned}
$$
:::


::: {.fragment .absolute top="0" right="400"}
$$
A = \begin{bmatrix}
1 & 0\\
3 & 2
\end{bmatrix}
$$
:::



::: {.fragment .fade-in-then-out .absolute top="200" right="300"}
$$
\begin{aligned}
& |A - \lambda I| = \begin{vmatrix}
1 - \lambda & 0\\
3 & 2 - \lambda
\end{vmatrix}\\\\
\end{aligned}
$$
:::



::: {.fragment .absolute top="200" right="300"}
$$
\begin{aligned}
& |A - \lambda I| = \begin{vmatrix}
1 - \lambda & 0\\
3 & 2 - \lambda
\end{vmatrix}\\\\
&=(1 - \lambda)(2 - \lambda)
\end{aligned}
$$
:::



::: {.fragment .absolute top="500" right="400"}
$$
\boxed{\lambda = 1, 2}
$$
:::



