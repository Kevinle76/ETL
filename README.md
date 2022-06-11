# Project-2
PROJECT 2: ETL

TEAM 14: 

KHANH LE & LUKE CRABTREE

Background:
We were interested in the median income, diversity index and unemployment rate for every United States county. To learn more, we gathered three different datasets to look at. We found one for diversity index, one for median income and one for unemployment rate.

Methods for Analysis:

1.	Utilized data sets from the Kaggle and Data World. 
2.	Libraries utilized: pandas, sqlalchemy, pymysql.
3.	Sorting and cleaning data

Data sets:
1.	Unemployment from Kaggle: https://www.kaggle.com/code/alshan/mapping-us-household-income
2.	Diversity  index from Kaggle: https://www.kaggle.com/datasets/mikejohnsonjr/us-counties-diversity-index
3.	Median Income from Data World: https://data.world/tylerudite/2015-median-income-by-county

Extract: 

•	Used Pandas functions in Jupyter Notebook to load all three CSV files. Store CSV files into DataFrame.

Transformation:

•	Reviewed the files and transformed into data frames
•	Removed the column due to missing information and relevancy.
•	Identified duplicates by doing an inner merge on the incident id column across all three data sets.
•	Created queries by grouping the data by state.

Load:

The last step was to transfer our final output into a Database. We created a database and respective table to match the columns from the final Panda's Data Frame using PGadmin4 to store our final dataframe. We chose PGadmin4 because originally we wanted to reference certain values across multiple tables. We later decided to merge the data in pandas before loading it, but we still kept using PGadmin4 in case we wanted to create multiple tables instead later.

References:

•	US Unemployment Rate by County, 1990-2016 | Kaggle
•	Diversity Index of US counties | Kaggle
•	tylerudite/2015-median-income-by-county | Workspace | data.world





	
