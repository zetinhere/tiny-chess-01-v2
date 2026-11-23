# tiny-chess-01-v2

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/zetinhere/tiny-chess-01-v2/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/zetinhere/tiny-chess-01-v2/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in under 4 KB of Python (packed `main.py`; readable source is `engine.py` in this folder).

Second variant, built for a top-leaderboard finish: 0x88 board, node-budgeted iterative deepening (depth 1–10, PVS), working null-move pruning, late-move reductions, futility pruning, delta-pruned quiescence with check evasions, tapered middlegame/endgame piece-square evaluation with doubled-pawn terms, transposition table with mate-distance scoring, killer + history move ordering. Deterministic: fixed node budgets, no clock, no unseeded randomness — the same position always gives the same move.

Build: `node <kit>/cli/makefun.mjs compress engine.py --out main.py`

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jc69fpy6&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
