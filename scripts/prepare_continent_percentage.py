import pandas as pd
summer = pd.read_csv("../output/summer.csv")
continent=pd.read_csv('../data_sources/continent.csv', 
                     usecols=['Continent_Name','Three_Letter_Country_Code']).rename(
    columns={'Three_Letter_Country_Code':'code_3'})
continent_4 = pd.read_excel("../data_sources/continent_4.xlsx",
                         usecols=['249 countries','A-3','IOC']).rename(
    columns={'A-3':'code_3'})
continent_merged=continent_4.merge(continent, on='code_3', how='left').rename(
    columns={'IOC':'NOC'})
summer_con=summer.merge(continent_merged,on='NOC',how='left')
summer_con_simple = summer_con[['Sex', 'Team','Year','Continent_Name']]
summer_con_classified2=pd.crosstab(summer_con_simple.Year, [summer_con_simple.Sex,summer_con_simple.Continent_Name])
summer_con_classified2['M', 'total'] = summer_con_classified2.iloc[:,0:12].sum(axis=1)
summer_con_classified2['M', 'female_percent']=summer_con_classified2.iloc[:,0:6].sum(axis=1)/summer_con_classified2['M', 'total'] 
summer_con_classified2['M','Africa_percent']=summer_con_classified2.iloc[:,0]/(
	summer_con_classified2.iloc[:,0]+summer_con_classified2.iloc[:,6])
summer_con_classified2['M','Asia_percent']=summer_con_classified2.iloc[:,1]/(
	summer_con_classified2.iloc[:,1]+summer_con_classified2.iloc[:,7])
summer_con_classified2['M','Europe_percent']=summer_con_classified2.iloc[:,2]/(
	summer_con_classified2.iloc[:,2]+summer_con_classified2.iloc[:,8])
summer_con_classified2['M','North America_percent']=summer_con_classified2.iloc[:,3]/(
	summer_con_classified2.iloc[:,3]+summer_con_classified2.iloc[:,9])
summer_con_classified2['M','Oceania_percent']=summer_con_classified2.iloc[:,4]/(
	summer_con_classified2.iloc[:,4]+summer_con_classified2.iloc[:,10])
summer_con_classified2['M','South America_percent']=summer_con_classified2.iloc[:,5]/(
	summer_con_classified2.iloc[:,5]+summer_con_classified2.iloc[:,11])
df=summer_con_classified2.drop(summer_con_classified2.iloc[:,0:12],axis=1,inplace=False)
df_new = df.xs('M', axis=1, drop_level=True)
df2=df_new.drop(df_new.iloc[:,0:1],axis=1,inplace=False)
df3=df2.reset_index(inplace=False)
df3.columns = ['Year', 'Global', 'Africa', 'Asia', 'Europe','North America','Oceania','South America']
df3.to_csv(
	"../output/continent_percentage_untidy.csv", index=False)
df3_tidy=pd.melt(df3,id_vars=['Year'],var_name='Continent',value_name='Female_Percentage')
df3_tidy["Female Percentage"] = (
   df3_tidy.Female_Percentage*100).round(1).astype(str) + '%'
df3_tidy.to_csv(
	"../output/continent_percentage_tidy.csv", index=False)


