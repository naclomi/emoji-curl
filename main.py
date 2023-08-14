#!/usr/bin/env python3
import argparse
import sys
import requests
import subprocess

def urljoin(*strs):
    return "/".join(str.rstrip("/") for str in strs)

def inkscapeSvgToPng(svg_bytes, size):
    cmd = ["inkscape",
            "--pipe",
            "--export-width={:d}".format(size),
            "--export-type=png",
            "--export-filename=-"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p_out, p_err = p.communicate(input=svg_bytes)
    return p_out

class Source(object):
    def __init__(self):
        pass

    def getPng(self, emoji, size):
        return b""

    def getSvg(self, emoji):
        return b""


class TwemojiSource(Source):
    def __init__(self, cdn):
        self.cdn = cdn

    @staticmethod
    def _getTwemojiCanonical(emoji):
        return "-".join(emoji.codepoints_hex)

    def getPng(self, emoji, size):
        svg = self.getSvg(emoji)
        return inkscapeSvgToPng(svg, size)

    def getSvg(self, emoji):
        filename = "{:}.svg".format(self._getTwemojiCanonical(emoji))
        url = urljoin(self.cdn, "svg", filename)
        response = requests.get(url)
        return response.content

class Emoji(object):
    def __init__(self, string):
        self.string = string
        self.codepoints = tuple(ord(x) for x in self.string)
        self.codepoints_hex = tuple("{:x}".format(c) for c in self.codepoints)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("emoji", nargs="+")
    parser.add_argument("--size", "-s", type=int, default=512)
    parser.add_argument("--png", "-r", action="store_true")

    args = parser.parse_args()
    source = TwemojiSource("https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/")
    for string in args.emoji:
        emoji = Emoji(string)
        if args.png:
            sys.stdout.buffer.write(source.getPng(emoji, args.size))
        else:
            sys.stdout.buffer.write(source.getSvg(emoji))
