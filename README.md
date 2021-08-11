## About

This is the repository detailing the data work flow of [Olymvis](), a visualization project by by [Zihui (Chris) Fang](https://github.com/zihfang/) and [Hongtao Hao](https://hongtaoh.com/), with **Equal Contribution**, as the term paper for Professor [Yong-Yeol Ahn](http://yongyeol.com/)'s [Data Visualization](https://yyahn.com/dviz-course/) course in 2019 Fall. 

## Data Source
The main data set used in this project is [Olympic_history](https://github.com/rgriff23/Olympic_history) by [rgriff23](https://github.com/rgriff23).

Other complementary data sets:

- [continent.csv](https://github.com/hongtaoh/olymvis-data/blob/master/data_sources/continent.csv) is used for extracting the ISO-3166 three letter country code and the corresponding continent name.

- [host_countries.csv](https://github.com/hongtaoh/olymvis-data/blob/master/data_sources/host_countries.csv) is used in [vis 3](https://olymvis.netlify.app/vis3/).

- [continent_4.xlsx](https://github.com/hongtaoh/olymvis-data/blob/master/data_sources/continent_4.xlsx) is used to extract the IOC (International Olympic Committee) country codes and the ISO-3166 three letter country codes. We merge `continent_4` with `continent` to get the corresponding continent name of each IOC code. We then merge this with [summer.csv](https://github.com/hongtaoh/olymvis-data/blob/master/output/summer.csv) to produce [continent_percentage_tidy](https://github.com/hongtaoh/olymvis-data/blob/master/output/continent_percentage_tidy.csv) and [continent_percentage_untidy](https://github.com/hongtaoh/olymvis-data/blob/master/output/continent_percentage_untidy.csv), two of which we used to visualize [changes in female particiation in the Olympics in different continents](https://olymvis.netlify.app/vis2/).

## Scripts

We used [these scripts](https://github.com/hongtaoh/olymvis-data/tree/master/scripts) to produce the results in [output](https://github.com/hongtaoh/olymvis-data/tree/master/output) from [data sources](https://github.com/hongtaoh/olymvis-data/tree/master/data_sources).

## Output

- [`summer.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/summer.csv) was produced by filtering only the Summer Olympics in [`athelet_events.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/data_sources/Olympic_history/data/athlete_events.csv). It was processed by [extract_summer.py](https://github.com/hongtaoh/olymvis-data/blob/master/scripts/extract_summer.py).

- [`year_sex_percentage.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/year_sex_percentage.csv) listed the percentages of both male and female in each Summer Olympic Game. It was produced by [prepare_year_sex_percentage.py](https://github.com/hongtaoh/olymvis-data/blob/master/scripts/prepare_year_sex_percentage.py).

- [`continent_percentage_tidy.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/continent_percentage_tidy.csv) & [`continent_percentage_untidy.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/continent_percentage_untidy.csv) were to visualize [changes in female particiation in the Olympics in different continents](https://olymvis.netlify.app/vis2/). They were produced by [prepare_continent_percentage.py](https://github.com/hongtaoh/olymvis-data/blob/master/scripts/prepare_continent_percentage.py).

- [`medal_summary.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/medal_summary.csv) was used to visualize home-field advantage. It was produced by [prepare_medal_summary.py](https://github.com/hongtaoh/olymvis-data/blob/master/scripts/prepare_medal_summary.py).

- [`medal_efficiency.csv`](https://github.com/hongtaoh/olymvis-data/blob/master/output/medal_efficiency.csv) was used to visualize medal efficiency for each participating country or region. It was produced by [prepare_medal_efficiency.py](https://github.com/hongtaoh/olymvis-data/blob/master/scripts/prepare_medal_efficiency.py).

## Noteobooks

We used [these notebooks](https://github.com/hongtaoh/olymvis-data/tree/master/notebooks) to produce our visulizations. 

## License

MIT

## Contribute 

Contact [Hongtao](https://hongtaoh.com/en/en-vitae/) or [Chris](https://github.com/zihfang/) if you have any suggestions or questions!

