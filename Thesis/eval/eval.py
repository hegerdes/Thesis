import sys
import pandas as pd

df = pd.read_csv("eval/stats_win_raw.csv")
# df = df.groupby("PID")
df = df[(df["Abbildname"] == "node.exe")]
for pid,df_pid in df.groupby("PID"):
    print(pid, df_pid)


if __name__ == '__main__':
    print("test")
    print(len( df.groupby("PID")))
    # print(df)