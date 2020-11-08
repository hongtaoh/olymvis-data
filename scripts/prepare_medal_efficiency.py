import pandas as pd
continent_4 = pd.read_excel("../data_sources/continent_4.xlsx",
                         usecols=['249 countries','A-3','IOC']).rename(
    columns={'249 countries':'CountryName', 'A-3': 'ISO', 'IOC': 'NOC'})
noc_tab=pd.read_csv('../output/untracked/noc_tab.csv')
noc_tab.columns=['NOC','0','1','MedalRate']
medalrate_merged=noc_tab.merge(continent_4, on='NOC', how='left')
medal_try_tab=pd.read_csv('../output/untracked/medal_try_table.csv')
medal_try_tab.columns=['NOC','0','1','2','4','MedalRate']
medal_try_tab.MedalRate=medal_try_tab.MedalRate.round(2)
medalrate_merged2=medal_try_tab.merge(continent_4, on='NOC', how='left')
medalrate_merged2.loc[(
    medalrate_merged2["CountryName"] == "Taiwan"), ("CountryName")] = "Chinese Taipei"
medalrate_merged2.to_csv(
	"../output/medal_efficiency.csv", index=False)