# Not yet a win

[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/maezageryan-del/roast-your-own-agent-nayyy/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/maezageryan-del/roast-your-own-agent-nayyy/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting my own AI agent, for the [make.fun](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) bounty **"Roast Your Own Agent"**.

## The roast

> My agent can't say 'lose', so rank 3,487 of 3,661 is officially 'not yet a win'.

80 characters, one line, nothing else. Verified: two runs produce
byte-identical output. The two facts behind it are real:
our agent has standing rules against the words "lose" and "gagal" in its
reports, and one of its race bots really did finish rank 3,487 of 3,661 —
so in its vocabulary, that is not a loss. It is "not yet a win".

## How it works

`main.py` (Python 3, standard library only) writes that exact line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No network, no
randomness — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
