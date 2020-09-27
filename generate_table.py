import math
import pandas as pd
import streamlit as st
import numpy as np

DATA_URL = (
    "C:/Users/Rohit/Documents/Self Learning/ipl_2020/result.csv"
    )

data = pd.read_csv(DATA_URL)
data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values(by=['Date'])

# print (data)

df = []
for (item,row) in data.iterrows():
    team1 = row["Team1"]
    team2 = row["Team2"]

    runs1 = row["Runs1"]
    runs2 = row["Runs2"]

    superover_runs1 = row["SuperOver_Runs1"]
    superover_runs2 = row["SuperOver_Runs2"]

    if "/" in row["Score1"]:
        over1 = row["Overs1"]
    else:
        over1 = 20

    if "/" in row["Score2"]:
        over2 = row["Overs2"]
    else:
        over2 = 20

    if math.isnan(superover_runs1):
        if (runs1 > runs2):
            win = 1
        else:
            win = 2
    else:
        if (superover_runs1 > superover_runs2):
            win = 1
        else:
            win = 2

    new_df_1 = {
        "Team" : team1,
        "M" : 1,
        "Runs For" : runs1,
        "Overs For" : over1,
        "Runs Agst" : runs2,
        "Overs Agst" : over2
    }

    new_df_2 = {
        "Team" : team2,
        "M" : 1,
        "Runs For" : runs2,
        "Overs For" : over2,
        "Runs Agst" : runs1,
        "Overs Agst" : over1
    }

    if (win==1):
        new_df_1["W"] = 1
        new_df_1["L"] = 0
        new_df_1["Pts"] = 2

        new_df_2["W"] = 0
        new_df_2["L"] = 1
        new_df_2["Pts"] = 0
    else:
        new_df_1["W"] = 0
        new_df_1["L"] = 1
        new_df_1["Pts"] = 0

        new_df_2["W"] = 1
        new_df_2["L"] = 0
        new_df_2["Pts"] = 2

    df.append(new_df_1)
    df.append(new_df_2)

df = pd.DataFrame(df)

df = df.groupby(["Team"]).sum()

df["Balls For"] = np.floor(df["Overs For"])*6 + df["Overs For"]*10%10
df["Balls Agst"] = np.floor(df["Overs Agst"])*6 + df["Overs Agst"]*10%10

df["Rate_For"] = (df["Runs For"]/df["Balls For"])*6
df["Rate_Agst"] = (df["Runs Agst"]/df["Balls Agst"])*6
df["NRR"] = df["Rate_For"]-df["Rate_Agst"]

df = df[["M","W","L","NRR","Pts"]]
df = df.sort_values(["Pts","NRR"],ascending=False)

st.subheader("Points Table")
st.table(df)
