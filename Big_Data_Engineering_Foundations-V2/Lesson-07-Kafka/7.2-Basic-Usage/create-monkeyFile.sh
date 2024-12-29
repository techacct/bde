#!/bin/bash
# A simple nonsense script to generate 100 messages at random times 
# between 2 and 10 seconds
for I in `seq 1 100`; do
SLEEPTIME=$(shuf -i2-10 -n1)
echo "Message: $I Monkeys jumping on the bed, $SLEEPTIME fell off and bumped their head. Then the Monkey said: " >>monkeyFile.txt
fortune >>monkeyFile.txt
sleep $SLEEPTIME 
done
