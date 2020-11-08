import pandas as pd
summer = pd.read_csv("../output/summer.csv")
unique_year = summer.Year.unique()
unique_year.sort()

sex_list=[]
year_list=[]
frequency_list = []
for year in unique_year:
    a = summer[summer.Year == year]
    frequency_list.extend([len(a[a.Sex=="M"]), len(a[a.Sex=="F"])])
    sex_list.extend(("M", "F"))
    year_list.extend([year, year])
year_sex_frequency_list = list(zip(year_list, sex_list,frequency_list)) 
year_sex_frequency = pd.DataFrame(year_sex_frequency_list, columns = ['Year', 'Sex','Frequency'])

percentage_list = []
participation_list = []
for year in unique_year:
    a = year_sex_frequency[year_sex_frequency.Year == year]
    frequency_total = sum(a["Frequency"])
    for row in a["Frequency"]:
        percentage_list.append(row/frequency_total)
        participation_list.append(row/frequency_total * 100)
year_sex_frequency["Percentage_decimal"] = percentage_list
year_sex_frequency["Percentage"] = (year_sex_frequency.Percentage_decimal*100).round(1).astype(str) + '%'
year_sex_percentage = year_sex_frequency
year_sex_percentage.Percentage_decimal = year_sex_percentage.Percentage_decimal.round(3)
year_sex_percentage.to_csv("../output/year_sex_percentage.csv")