import requests
import re
from bs4 import BeautifulSoup

# URL
url = f"https://www.google.com/search?rlz=1C1RLNS_enIN782IN783&ei=2FBvX8bRJcKc4-EP_YiqwAk&q=ipl+match+on+25+september+2020"
pattern = r"\(([0-9\\.]+)\)"

req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

divs = soup.find_all('div',class_='kCrYT')
divs = divs[1]

part1 = divs.contents[0].find_all('span')
match_no = part1[0].div.contents[0].split(" ")[1]
date = part1[2].contents[0]

try:
    team1 = divs.contents[2].contents[1].span.div.contents[0].contents[0]
except:
    team1 = divs.contents[2].contents[1].span.div.contents[0]

score1 = str(divs.contents[2].contents[2].contents[0].contents[0]).strip()
runs1 = score1.split("/")[0]

try:
    overs1 = divs.contents[2].contents[2].contents[0].contents[1].contents[0]
    result = re.search(pattern, overs1)
    overs1 = result.group(1)
except:
    overs1 = 20
    superover1 = divs.contents[2].contents[2].contents[0].contents[2]
    result = re.search(r"([0-9/]+)", superover1)
    superover1 = result.group()

try:
    team2 = divs.contents[3].contents[1].span.div.contents[0].contents[0]
except:
    team2 = divs.contents[3].contents[1].span.div.contents[0]

score2 = str(divs.contents[3].contents[2].contents[0].contents[0]).strip()
runs2 = score2.split("/")[0]

try:
    overs2 = divs.contents[3].contents[2].contents[0].contents[1].contents[0]
    result = re.search(pattern, overs2)
    overs2 = result.group(1)
except:
    overs2 = 20
    superover2 = divs.contents[3].contents[2].contents[0].contents[2]
    result = re.search(r"([0-9/]+)", superover2)
    superover2 = result.group()

# for i in divs.contents[3:]:
#     print (i.prettify())
#     print ()

try:
    df = {
        "Match" : match_no,
        "Date" : date,
        "Team1" : team1,
        "Score1" : score1,
        "Runs1" : runs1,
        "Overs1" : overs1,
        "SuperOver1" : superover1,
        "Team2" : team2,
        "Score2" : score2,
        "Runs2" : runs2,
        "Overs2" : overs2,
        "SuperOver2" : superover2
        }
    print (df)
except:
    df = {
        "Match" : match_no,
        "Date" : date,
        "Team1" : team1,
        "Score1" : score1,
        "Runs1" : runs1,
        "Overs1" : overs1,
        "Team2" : team2,
        "Score2" : score2,
        "Runs2" : runs2,
        "Overs2" : overs2
        }
    print (df)
