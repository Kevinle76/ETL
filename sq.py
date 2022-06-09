CREATE TABLE DIVERS (
	
	State VARCHAR(255),
	County VARCHAR(255), 
	FOREIGN KEY (County) REFERENCES unemp(County),
  	Diver_index FLOAT,
 	Black FLOAT,
 	American FLOAT,
	Asian FLOAT,
	Hawaian FLOAT,
	Two_more_races FLOAT,
	Hispanic FLOAT,
 	White FLOAT
 );

	
-- CREATE TABLE unemp (
-- 	State VARCHAR(255) , 
-- 	County	VARCHAR(255) PRIMARY KEY,
-- 	Rate FLOAT 
-- 	);
-- CREATE TABLE inco (
-- 		State VARCHAR(255) ,
-- 		County VARCHAR(255), 
-- 		FOREIGN KEY (County) REFERENCES unemp(County),
-- 		Population INT,
-- 		Median_household_income	FLOAT
-- );
