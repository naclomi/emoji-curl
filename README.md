# emoji-curl

## Introduction

Take UTF-8 emoji as input and pipe their corresponding twemoji image data to stdout. Useful for quickly getting high-resolution copies of an emoji to use in presentation slides or the SVG source of an emoji to make some edits.

## Usage

Open an emoji for editing in Inkscape

```bash
./main.py 😎 > inkscape --pipe -g
```

Or render said SVG as a 1024x1024 PNG

```bash
./main.py -r -s 1024 😎 > cool.png
```

## Dependencies and support

For core usage, requires `python3` and `requests`. For PNG conversion, requires `inkscape` to be installed and findable in the system `PATH`.

## TODO

- Find some way to render SVGs without using inkscape.
- Configure defaults through environment variables
- Support other CDNs for twemoji, including local mirror
- Support other emoji sets
- Built-in clipboard support?
