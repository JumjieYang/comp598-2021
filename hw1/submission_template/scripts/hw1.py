import pandas as pd

dataset = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/russian-troll-tweets/master/IRAhandle_tweets_1.csv")

dataset = dataset[:10000]
dataset = dataset[dataset["language"] == "English"]

columns = ['tweet_id', 'publish_date', 'content']
dataset = pd.DataFrame(dataset, columns=columns)
dataset = dataset[~dataset['content'].str.contains("?", regex=False)]

dataset['trump_mention'] = dataset['content'].str.contains("\WTrump\W")

analysis = pd.DataFrame(columns=['result', 'value'])
analysis.loc[-1] = ['frac-trump-mentions', dataset['trump_mention'].eq(True).mean() * 100]
analysis['value'] = analysis['value'].round(decimals=3)

dataset.to_csv('../dataset.tsv', sep= '\t', index=False)
analysis.to_csv('../results.tsv', sep= '\t', index=False)
