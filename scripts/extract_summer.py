import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/rgriff23/Olympic_history/master/data/athlete_events.csv')
summer = data[data.Season == "Summer"].to_csv("../output/summer.csv", index=False)
