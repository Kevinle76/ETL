# Project-2
PROJECT 2: ETL
TEAM 14: KHANH LE & LUKE CRABTREE

Background:
We would like to know and understand about the median income and unemployment rate of each county of each state basing on data from different sources.

Methods for Analysis:

1.	Utilized data sets from the Kaggle 
2.	Libraries utilized: pandas, sqlalchemy, pymysql.
3.	Sorting and cleaning data

Data sets:
1.	Unemployment from Kaggle.
2.	Diversity  index from Kaggle.
3.	Median Income from Data World

Extract: 

•	Used Pandas functions in Jupyter Notebook to load all three CSV files. Store CSV files into DataFrame.

Transformation:

•	Reviewed the files and transformed into data frames
•	Removed the column due to missing information which was not relevant.
•	Identified duplicates by doing an inner merge on the incident id column across all three data sets.
•	Created queries by grouping the data by state.

Load:

The last step was to transfer our final output into a Database. We created a database and respective table to match the columns from the final Panda's Data Frame using PGadmin4 to store our original clean data sets. 

References:

•	US Unemployment Rate by County, 1990-2016 | Kaggle
•	Diversity Index of US counties | Kaggle
•	tylerudite/2015-median-income-by-county | Workspace | data.world





	
