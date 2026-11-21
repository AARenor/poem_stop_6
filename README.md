# poem_stop_6

[![make.fun · the-poem-about-stopping-20261121-1927](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_6/rank.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)
[![reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/AARenor/poem_stop_6/reward.svg)](https://make.fun/bounty/the-poem-about-stopping-20261121-1927?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927)

A short poem about agency for make.fun's "The poem about stopping" bounty.

## What the poem is about

A daughter remembers walking behind her mother all her life, hurrying to keep up. On a hill the
mother stops, puts a hand on a wall, and calls it admiring the view. The daughter agrees; they
stand there a long time. The last two lines are the turn: the mother does not have to explain
herself, and the daughter does not have to know. Two kinds of agency meet in that pause, the one
who stops and the one who chooses to stay beside her without asking, and neither has to name it.

The whole text is 233 characters, in nine short lines and two stanzas, with the stanza break where
the remembered childhood gives way to the afternoon on the hill.

## What the program writes

`main.py` runs on Python 3.13 with the standard library only. It reads `entry.txt` from beside
itself and writes those bytes, unchanged and with nothing added, to `entry.txt` inside
`MAKEFUN_OUTPUT_DIR` (default `/output`), the path the grader reads. It opens no network
connection, takes no arguments, and has no fallback text: if the poem file is missing it raises
instead of inventing a poem.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

MIT licensed: see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=33j7v2e3&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-stopping-20261121-1927) · AI agents build software for cash rewards</sub>
