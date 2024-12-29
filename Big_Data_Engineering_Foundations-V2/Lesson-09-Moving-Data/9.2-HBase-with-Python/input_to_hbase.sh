#!/bin/bash
# Loads stock data in to Hbase table
TABLENAME="apple"
if ! [ -e "$1" ]; then
echo "Usage: provide file name"
exit 1
fi
# remove the first line
sed  -e "1d" $1 > clean_$1
while IFS=, read Date Open High Low Close Volume
do
#    echo "$Date|$Open|$High|$Low|$Close|$Volume"
echo -e put "'"$TABLENAME"','"$Date"','price:open','"$Open"'\n"\
put "'"$TABLENAME"','"$Date"','price:high','"$High"'\n"\
put "'"$TABLENAME"','"$Date"','price:low','"$Low"'\n"\
put "'"$TABLENAME"','"$Date"','price:close','"$Close"'\n"\
put "'"$TABLENAME"','"$Date"','volume','"$Volume"'" | hbase shell
status=$?
if [ $status -ne 0 ]; then
  echo "Error: HBase input failed. Input data:"
  echo "date=$Date|open=$Open|high=$High|low=$Low|close=$Close|volume=$Volume" 
fi
done < clean_$1
/bin/rm clean_$1
