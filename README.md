# Probability Simulations

Short Python projects where I explore probability and game theory by simulation rather than by formula.

## El Farol Bar Problem (agent-based model)

The El Farol Bar problem is a classic model of crowd behaviour: each round, everyone decides whether to go to a bar, but the bar is only enjoyable if it isn't overcrowded. There's no "correct" choice, because the right answer depends on what everyone else does.

In my model, 2,000 agents play for 5,000 rounds. Every round there is a shared forecast of whether the bar will be crowded. Each agent has a personal value `p`: the probability that they follow the forecast (otherwise they do the opposite). An agent who keeps ending up on the wrong side replaces their `p` with a new random value. At the end, I plot how `p` is distributed across the population.

| File | Setup |
|---|---|
| `el_farol.py` | Forecast is effectively random (the memory length is too long to ever match a pattern), bar capacity 50% |
| `el_farol_small_m.py` | Forecast based on the last 2 outcomes, bar capacity 60% |

### Findings

**Random forecast:** the population splits into two extremes, agents who almost always follow the forecast and agents who almost always defy it. Cautious "in-between" strategies get weeded out.

![Distribution of p with a random forecast](p_value_histogram.png)

**Memory-based forecast:** the population shifts heavily towards following the forecast; agents learn to trust a signal that carries real information.

![Distribution of p with a memory-based forecast](p_value_histogram_2.png)

**Caveat:** the second run changes both the memory length and the bar capacity, so the shift can't yet be attributed to the forecast alone. The next step is to rerun with memory length 2 and capacity 50% to isolate the effect.

## Other simulations

| File | What it does |
|---|---|
| `monte_carlo.py` | Estimates π by dropping random points in a unit square |
| `pokemon.py` | Coupon collector problem: the expected number of packs needed to collect all 10 cards |
| `random_walks.py` | A simple one-dimensional random walk |

## Running

```
pip install matplotlib
python el_farol.py
```
