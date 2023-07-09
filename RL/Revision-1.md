---
title: "RL | Quiz-1 | Revision"
subtitle: "Weeks 2 and 3"
author: "Karthik Thiagarajan"
format: revealjs
incremental: true
fontsize: 35px
margin: 0.1
width: 1600
height: 800
revealjs-plugins:
  - pointer
---

## MDP

::: {.fragment}
Markov Decision Process
:::

- States: $\mathcal{S}$
- Actions: $\mathcal{A}$
- Rewards: $\mathcal{R}$
- Transition Probabilities and Reward Expectations
  - $p(s^{\prime}, r\ |\ s, a)$
  - $p(s^{\prime}\ |\ s, a), r(s, a, s^{\prime})$
- MDP $\rightarrow$ $\langle \mathcal{S}, \mathcal{A}, \mathcal{R}, \mathcal{p} \rangle$
- Finite MDP
 	- finite states
 	- finite actions

::: {.fragment .absolute left="1000" top="10"}
$$
p(s^{\prime}\ |\ s, a) = \sum \limits_{r} p(s^{\prime}, r\ |\ s, a)
$$
:::


::: {.fragment .absolute left="1000" top="230"}
$$
p(r\ |\ s^{\prime}, s, a) = \cfrac{p(s^{\prime}, r\ |\ s, a)}{p(s^{\prime}\ |\ s, a)}
$$
:::

::: {.fragment .absolute left="1000" top="500"}
$$
r(s, a, s^{\prime}) = \sum \limits_{r} r \cdot p(r\ |\ s^{\prime}, s, a)
$$
:::

## Return

::: {.fragment}
$$
G_t = R_{t + 1} + \gamma \cdot R_{t + 2} + \gamma^2 \cdot R_{t + 3} + \cdots
$$
:::

::: {.fragment .absolute left="100" top="300"}
- $\gamma$: discount rate
- $0 \leq \gamma \leq 1$
- $\gamma = 0$: myopic
- $\gamma \rightarrow 1$: farsighted
:::

::: {.fragment .absolute left="600" top="300"}
Tasks

- Episodic
	- Typically $\gamma = 1$ 
- Continuing
	- $0 \leq \gamma < 1$
:::

::: {.fragment .fade-in-then-out .absolute left="1000" top="300"}
$$
G_{t} = R_{t + 1} + \gamma \cdot [R_{t + 2} + \gamma \cdot R_{t + 3} + \cdots]
$$
:::

::: {.fragment .absolute left="1000" top="300"}
$$
G_{t} = R_{t + 1} + \gamma \cdot G_{t + 1}
$$
:::