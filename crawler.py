'''
Python script to act as a web crawler.

Used with Twint.
'''
# imports
import argparse  # makes sure the user gives a username
import subprocess  # the modern version of os
import json  # twint uses json

# handle arguments
parser = argparse.ArgumentParser(description='Filter Tweets.')
parser.add_argument("-u", required=True)
args = parser.parse_args()


# run Twint
retcode = subprocess.call(
        ['twint', '-u', args.u, '-o', f'{args.u}_tweets.json', '--json'],
        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

with (open(f"{args.u}_tweets.json", "r") as input_file,
        open(f"readable_{args.u}_tweets.txt", "w") as out_file):
    for line in input_file:
        tweet = json.loads(line)
        out_file.write(tweet['created_at'] + " " + tweet['tweet'] + "\n")
