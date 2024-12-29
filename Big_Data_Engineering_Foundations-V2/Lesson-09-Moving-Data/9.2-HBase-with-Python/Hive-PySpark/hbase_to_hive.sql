-- Copy apple stock table to Hive
 
CREATE EXTERNAL TABLE IF NOT EXISTS apple (
    caldate string,
    open double,
    high double,
    low double,
    close double,
    volume bigint 
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.hbase.HBaseSerDe'
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES (
    'hbase.columns.mapping'=':key,price:open,price:high,price:low,price:close,volume:amount'
)
TBLPROPERTIES (
    'hbase.mapred.output.outputtable'='apple',
    'hbase.table.name'='apple'
);
-- Provide information on the table
describe apple;
select * from apple limit 5;
