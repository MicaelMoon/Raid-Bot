import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", type=str, required=True, help="Enter a message")
args = parser.parse_args()

print (f"Mesage: {args.m}")