import pandas as pd
import numpy as np
# ------------------------------------------------------------
# ACTIVITY 1
# ------------------------------------------------------------
download_speed = pd.Series([138.24, 71.21, 125.27, 78.61, 125.38, 149.68, 148.92, 126.67, 71.96,
70.82, 82.48, 110.82, 140.40, 68.63, 126.99, 121.26, 93.67, 76.92, 80.68, 68.58])

upload_speed = pd.Series([162.73, 151.33, 152.79, 139.71, 159.14, 155.78, 153.82, 150.83, 155.71, 
131.84, 160.54, 121.53, 155.02, 159.32, 157.20, 159.01, 151.09, 160.75, 151.74, 151.23])

idle_latency = pd.Series([4, 94, 11, 7, 21, 13, 12, 6, 13, 50, 9, 12, 7, 6, 5, 48, 63, 6,
15, 5])

df = pd.DataFrame({
    'Download Speed' : download_speed,
    'Upload Speed' : upload_speed,
    'Idle Latency' : idle_latency
})

new_data = pd.DataFrame({
  "Means" : df.mean(),
  "Medians" :df.median(),
  "Mode" : df.mode().loc[0]
})

df = pd.concat([df, new_data.T])

print(df)

# df.loc[20] = [df["Download Speed"].median(),df["Upload Speed"].median(),df["Idle Latency"].median()]

# # df.loc[21] = [df["Download Speed"].mode().values[0],df["Upload Speed"].mode().values[0],df["Idle Latency"].mode().values[0]]

# df.loc[22] = [df["Download Speed"].mean(),df["Upload Speed"].mean(),df["Idle Latency"].mean()]

# print(df)

# ABOVE comments (long winded way)
# ------------------------------------------------------------
# print(df.mean(axis=0))

# print(df.mode(axis=0))

# print(df.median(axis=0))

# print(df["Download Speed"].median())

# df.loc[20] = [df["Download Speed"].median(),df["Upload Speed"].median(),df["Idle Latency"].median()]

# new_data = pd.DataFrame({"Mean": [(df.mean(axis=0))], "Mode": [(df.mode(axis=0))], "Median" :[(df.median(axis=0))]})
# df = pd.concat([df, new_data], ignore_index=True)

# print(df)

# df.loc[21] = [df.mean(axis=0)]
# print(df)
# ------------------------------------------------------------
# ACTIVITY 2
# ------------------------------------------------------------

# Sort df in order, fastest download speed 1st
print(df.sort_values(by=["Download Speed"], ascending=False))
# fastest = High to low
# to remove the Mode/median/mean I commented out the above code


# Sort to show slowest upload speed
print(df.sort_values(by=["Upload Speed"]))
# slowest= low to high


