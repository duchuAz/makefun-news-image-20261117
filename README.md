# news-image-20261117

An entry for the make.fun [news-image-20261117](https://make.fun/bounty/news-image-20261117) bounty: a 1024x1024 front page of world news reported on 17 November 2026.

## What it does

`main.ts` (Node 22, standard library only) reads `entry.png` from the repository root, checks it is a well-formed 1024x1024 PNG of at most 1 MiB, and writes the same bytes to `${MAKEFUN_OUTPUT_DIR:-/output}/entry.png`.

The image is never redrawn, resampled or re-encoded: the output is a byte-for-byte copy, so two runs of the program always write identical bytes.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
sha256sum out/entry.png entry.png
```

## Layout

- `entry.png` — the finished image (1024x1024, 216,951 bytes)
- `main.ts` — the validating copy program
- `build.py` — the script that rendered the front page from the day's headlines
- `world.geojson` — Natural Earth 110m country outlines used by the map
- `.makefun/owner.json` — the claim file naming the entry's wallet
- `LICENSE` — MIT

## License

MIT, see [LICENSE](LICENSE).
