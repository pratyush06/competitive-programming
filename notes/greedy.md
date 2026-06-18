# Greedy

## Recognition Cues

- Need optimize with local choices.
- Sorting by start, end, cost, profit, or deadline simplifies the decision.
- Once a choice is made, it never needs to be revisited.

## Core Ideas

- State the greedy rule in one sentence.
- Prove why choosing the local best does not block the global best.
- Sort to expose the next safe choice.

## Common Traps

- Greedy rule feels intuitive but lacks an exchange argument.
- Sorting by the wrong key.
- Missing tie-breaking.
- Applying greedy to a DP problem.

## Review Problems

- `greedy_problems/uva-11264-coin-collector.py`
- `greedy_problems/uva-11389-the-bus-driver-problem.py`
- `greedy_problems/uva-12321-gas-station.py`
- `dynamic_programming/55_jump_game.py`

