from bs4 import BeautifulSoup
import codecs

clearflg_dict={
    "clflg7": "FC",
    "clflg6": "EXH",
    "clflg5": "H",
    "clflg4": "N",
    "clflg3": "E",
    "clflg2": "A",
    "clflg1": "F",
    "clflg0": "---"
    }
clearflg_list = ["FC", "EXH", "H", "N", "E", "A", "F", "---"]
djlevel_list = ["AAA", "AA", "A", "B", "C", "D", "E", "F", "---"]


def parse_summary(html):
    soup = BeautifulSoup(codecs.open(html, "r", "shift_jis").read(),
                         "html5lib")
    clears = soup.find("div", class_="music-diff").find("table")

    clear_musics = {k: 0 for k in clearflg_list}
    djlevels = {k: 0 for k in set(djlevel_list) - set(["---"])}

    for row in clears.find_all("tr"):
        items = row.find_all("td")
        for i, item in enumerate(items):
            if not item.find_all("img"):
                continue
                
            filename = item.find("img")["src"].split("/")[-1]
            filename = filename.replace(".gif","")

            if filename in clearflg_dict:
                flag = clearflg_dict[filename]
                clear_musics[flag] = int(items[i+1].string[:-1])
            else:
                djlevels[filename] = int(items[i+1].string[:-1])
    return clear_musics, djlevels


def parse_detail(html):
    soup = BeautifulSoup(codecs.open(html, "r", "shift_jis").read(),
                         "html5lib")    
    detail = soup.find("div", class_="series-difficulty").find("table")
    musics = {}
    for row in detail.find_all("tr"):
        tds = row.find_all("td")
        if len(tds) < 5:
            continue
        music = tds[0].a.string
        level = tds[1].string
        djl = tds[2].find("img")["src"].split("/")[-1].replace(".gif","")
        score = tds[3].text.split("(")[0]
        clf = clearflg_dict[
            tds[4].find("img")["src"].split("/")[-1].replace(".gif","")]
        musics[(music, level)] = (djl, score, clf)
    return musics


def main(argvs):
    htmls = argvs[1:]
    clear_musics, djlevels = parse_summary(htmls[0])
    musics = {}
    for h in htmls:
        musics.update(parse_detail(h))
    print(clear_musics, djlevels)
    print(musics)

if __name__=="__main__":
    import sys
    main(sys.argv)
