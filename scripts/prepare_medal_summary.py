# Data manipulated by Chris

import pandas as pd
summer = pd.read_csv("../output/summer.csv")
host_countries = pd.read_csv("../data_sources/host_countries.csv",skipinitialspace=True)
#Find unique year
unique_NOC = summer.NOC.unique()
unique_Year = summer.Year.unique()
unique_Year.sort()
unique_NOC.sort()
#Create medal summary list
Year_list=[]
NOC_list=[]
MedalPercentage_list=[]
for year in unique_Year:
    for noc in unique_NOC:
        total_medals = summer[(summer["Year"]==year)]
        medals_gained = total_medals[(total_medals["Medal"].notnull()) & (total_medals["NOC"] == noc)]
        medals_percentage = len(medals_gained)/len(total_medals)
        Year_list.append(year)
        NOC_list.append(noc)
        MedalPercentage_list.append(medals_percentage)
        
#Make panda dataframe with the medal summary list
MedalSummary_list = list(zip(Year_list, NOC_list,MedalPercentage_list)) 
MedalSummary = pd.DataFrame(MedalSummary_list, columns = ['Year', 'NOC','Percentage_of_Medals'])  
MedalSummary['compressed']=MedalSummary.apply(lambda x:'%s%s' % (x['Year'],x['NOC']),axis=1)
host_countries['compressed']=host_countries.apply(lambda x:'%s%s' % (x['Year'],x['NOC']),axis=1)
MedalSummary['Host_Country'] = MedalSummary['compressed'].isin(host_countries['compressed']).astype(int)
MedalSummary.drop(columns=["compressed"]).to_csv(
	"../output/medal_summary.csv", index=False)


