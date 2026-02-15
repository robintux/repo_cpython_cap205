import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/refs/heads/master/Ames_Housing_Data.tsv")

df = df.dropna()
df.to_csv("data_limpia.csv")