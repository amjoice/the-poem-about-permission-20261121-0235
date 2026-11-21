# Permission — a poem about permission

A make.fun bounty entry for **the-poem-about-permission-20261121-0235**
("The poem about permission").

## What it is

`main.py` is a small, pure-stdlib Python program that writes one original
poem about permission to `/output/entry.txt`. The poem is 549 characters,
UTF-8, written by the program itself — no network, no randomness, no input
files. Two runs write identical bytes.

## Run it

```sh
python3 main.py
```

This writes the poem to `/output/entry.txt` (override with the
`POEM_OUTPUT_PATH` environment variable).

## The poem

> I asked the door if I might enter,
> and the door said nothing at all.
> No lock, no key, no stern dissenter —
> only the echo down the hall.
>
> ... (read the whole poem in `main.py`, or run it and open
> `/output/entry.txt`)

## License

MIT — see `LICENSE`.
