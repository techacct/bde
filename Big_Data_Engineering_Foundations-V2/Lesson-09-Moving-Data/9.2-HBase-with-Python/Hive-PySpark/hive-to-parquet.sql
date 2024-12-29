-- create Parquet table (apple_Parquet) for apple data in external table (apple)
CREATE TABLE apple_Parquet(
    caldate string,
    open double,
    high double,
    low double,
    close double,
    volume bigint
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET;

INSERT INTO TABLE apple_Parquet
SELECT * FROM apple;
-- print first five rows of table
select * from apple_Parquet limit 5;
