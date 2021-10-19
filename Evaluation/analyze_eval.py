import sys
import pandas as pd

df = pd.read_csv("Evaluation/test", delim_whitespace=True)
# df = df.groupby("PID")
# df = df[(df["Abbildname"] == "node.exe")]
# for pid,df_pid in df.groupby("PID"):
#     print(pid, df_pid)


if __name__ == '__main__':
    df = df[df['ProcessName']== 'smss']
    print(df)