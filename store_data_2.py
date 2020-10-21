import requests
import re
import math
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

today = datetime.now()

DATA_URL = (
    "C:/Users/Rohit/Documents/Self Learning/ipl_2020/result.csv"
    )
pattern = r"\(([0-9\\.]+)\)"
df = []

data = pd.read_csv(DATA_URL)
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by=['Date'])
data = data.iloc[-1:]
dt = datetime.utcfromtimestamp((data['Date'].values[0]).tolist()/1e9)

delta = timedelta(days=1)

while dt <= today:
    dt += delta
    date = dt.strftime("%d+%B+%Y").lower()

    if (dt.weekday() == 5 or dt.weekday() == 6):
        print (date)

        try:
            url = f"https://www.google.com/search?q=ipl+match+on+"+date

            req = requests.get(url)

            soup = BeautifulSoup(req.text, "html.parser")

            divs = soup.find_all('div',class_='kCrYT')

            part1 = divs[2].find_all('span')
            match_no = part1[0].div.contents[0].split(" ")[1]
            date = part1[2].contents[0]
            date = date + ", 2020"

            superover1 = math.nan
            superover2 = math.nan
            superover_runs1 = math.nan
            superover_runs2 = math.nan

            try:
                team1 = part1[4].contents[0].contents[0]
                score1 = str(part1[5].contents[0].contents[0]).strip()
                runs1 = score1.split("/")[0]
            except:
                team1 = part1[5].contents[0]
                score1 = str(part1[6].contents[0].contents[0]).strip()
                runs1 = score1.split("/")[0]

            try:
                overs1 = part1[6].contents[0]
                result = re.search(pattern, overs1)
                overs1 = result.group(1)
            except:
                try:
                    overs1 = part1[7].contents[0]
                    result = re.search(pattern, overs1)
                    overs1 = result.group(1)
                except:
                    superover1 = part1[6].contents[0].contents[2]
                    result = re.search(r"([0-9/]+)", superover1)
                    superover1 = result.group()
                    superover_runs1 = superover1.split("/")[0]
                    overs1 = 20

            try:
                team2 = part1[8].contents[0].contents[0]
                score2 = str(part1[9].contents[0].contents[0]).strip()
                runs2 = score2.split("/")[0]
            except:
                try:
                    team2 = part1[8].contents[0]
                    score2 = str(part1[9].contents[0].contents[0]).strip()
                    runs2 = score2.split("/")[0]
                except:
                    team2 = part1[9].contents[0].contents[0]
                    score2 = str(part1[10].contents[0].contents[0]).strip()
                    runs2 = score2.split("/")[0]

            try:
                overs2 = part1[10].contents[0]
                result = re.search(pattern, overs2)
                overs2 = result.group(1)
            except:
                superover2 = part1[10].contents[0].contents[2]
                result = re.search(r"([0-9/]+)", superover2)
                superover2 = result.group()
                superover_runs2 = superover2.split("/")[0]
                overs2 = 20

            new_df = {
                    "Match" : match_no,
                    "Date" : date,
                    "Team1" : team1,
                    "Score1" : score1,
                    "Runs1" : runs1,
                    "Overs1" : overs1,
                    "SuperOver1" : superover1,
                    "SuperOver_Runs1" : superover_runs1,
                    "Team2" : team2,
                    "Score2" : score2,
                    "Runs2" : runs2,
                    "Overs2" : overs2,
                    "SuperOver2" : superover2,
                    "SuperOver_Runs2" : superover_runs2
                    }
            df.append(new_df)

            part2 = divs[1].find_all('span')

            match_no = part2[0].div.contents[0].split(" ")[1]
            date = part2[2].contents[0]
            date = date + ", 2020"

            superover1 = math.nan
            superover2 = math.nan
            superover_runs1 = math.nan
            superover_runs2 = math.nan

            # for part in part2:
            #     print (part)
            try:
                team1 = part2[4].contents[0].contents[0].contents[0]
                score1 = str(part2[6].contents[0].contents[0]).strip()
                runs1 = score1.split("/")[0]
            except:
                team1 = part2[4].contents[0].contents[0]
                score1 = str(part2[5].contents[0].contents[0]).strip()
                runs1 = score1.split("/")[0]

            try:
                overs1 = part2[7].contents[0]
                result = re.search(pattern, overs1)
                overs1 = result.group(1)
            except:
                try:
                    overs1 = part2[6].contents[0]
                    result = re.search(pattern, overs1)
                    overs1 = result.group(1)
                except:
                    superover1 = part2[5].contents[0].contents[2]
                    result = re.search(r"([0-9/]+)", superover1)
                    superover1 = result.group()
                    superover_runs1 = superover1.split("/")[0]
                    overs1 = 20

            try:
                team2 = part2[8].contents[0].contents[0]
                score2 = str(part2[9].contents[0].contents[0]).strip()
                runs2 = score2.split("/")[0]
            except:
                try:
                    team2 = part2[8].contents[0]
                    score2 = str(part2[9].contents[0].contents[0]).strip()
                    runs2 = score2.split("/")[0]
                except:
                    team2 = part2[9].contents[0]
                    score2 = str(part2[10].contents[0].contents[0]).strip()
                    runs2 = score2.split("/")[0]

            try:
                overs2 = part2[10].contents[0]
                result = re.search(pattern, overs2)
                overs2 = result.group(1)
            except:
                superover2 = part2[10].contents[0].contents[2]
                result = re.search(r"([0-9/]+)", superover2)
                superover2 = result.group()
                superover_runs2 = superover2.split("/")[0]
                overs2 = 20

            new_df = {
                    "Match" : match_no,
                    "Date" : date,
                    "Team1" : team1,
                    "Score1" : score1,
                    "Runs1" : runs1,
                    "Overs1" : overs1,
                    "SuperOver1" : superover1,
                    "SuperOver_Runs1" : superover_runs1,
                    "Team2" : team2,
                    "Score2" : score2,
                    "Runs2" : runs2,
                    "Overs2" : overs2,
                    "SuperOver2" : superover2,
                    "SuperOver_Runs2" : superover_runs2
                    }
            df.append(new_df)
            print ("Done")
            print ()
        except:
            break

df = pd.DataFrame(df)
df.to_csv(DATA_URL, mode='a', header=False, index=False)
print ("Transferred to CSV")
