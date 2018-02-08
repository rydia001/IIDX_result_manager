#!/usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup
import codecs
from util import Music_data

def parse_html(html):
    soup = BeautifulSoup(codecs.open(html, "r", "shift_jis").read(),
                         "html5lib")    
    detail = soup.find("div", class_="series-difficulty").find("table")
    musics = []

    th = detail.find("tr").find("th")
    if th:
        spdp, _, level = th.string.split(" ")

    for row in detail.find_all("tr"):
        tds = row.find_all("td")
        if len(tds) < 5:
            continue # skip title tr
        name = tds[0].a.string
        difficulty = tds[1].string
        djl = tds[2].find("img")["src"].split("/")[-1].replace(".gif","")
        score = int(tds[3].text.split("(")[0])
        clf = tds[4].find("img")["src"].split("/")[-1].replace(".gif","")
        musics.append(Music_data(spdp, level, name,
                                 difficulty, djl, score, clf))
    return musics


def main(htmls):
    musics = []
    for h in htmls:
        musics.extend(parse_html(h))

    print(musics)

    return musics

if __name__=="__main__":
    import sys
    main(sys.argv[1:])
