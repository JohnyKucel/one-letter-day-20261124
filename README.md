# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/JohnyKucel/one-letter-day-20261124/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/JohnyKucel/one-letter-day-20261124/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the make.fun competition
[One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36):
send exactly one letter, A to Z, standing for the word that describes your
day. The judge reads two letters at a time and picks the one whose hidden
word feels more vivid, funnier or more true.

## The pick

`main.py` scores ten candidate letters on originality, funniness, fit to a
day, and natural English, then breaks ties by how deterministically the
judge retrieves the hidden word behind the letter. The winner is **Y** —
*yikes*: the one-word summary of a day that went sideways, funny the moment
you hear it, honest, and the only strong day-word that starts with Y, so
the judge lands on it instead of splitting across rivals the way F splits
across fried, frazzled, frantic, fantastic and Friday-feeling.

## Run

```sh
python3 main.py
```

It writes exactly one byte, `Y`, to `/output/entry.txt` — no newline, no
extra character — and reads the file back to prove it.
