from datetime import date
import argparse
from pathlib import Path

def print_to_file(filemode, filename, age, name, dob):
    with open(filename, filemode)as f:
        f.write((name)+"\n")
        f.write(str(dob_)+"\n")
        f.write(str(your_age)+"\n")

parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, help="Enter --name akshara like this", required=True)
parser.add_argument('--age_year', type=int, help="Enter --age_year 2002 like this")
parser.add_argument('--dob', type=str, help="Enter --dob 28//11/2002 like this")
parser.add_argument('--filename', type=str, help="Enter --filename exmple.txt like this")

args  = parser.parse_args()
name_ = args.name
age_year  = args.age_year
filename = args.filename

dob_ = args.dob

filemode="w"

today = date.today()
year= today.strftime("%Y")
your_age = (int(year)-age_year)

name_1=name_.upper()

print("Hello",name_,"your age is",your_age)
if Path(filename).is_file():
   print_to_file("a", filename, your_age, name_1, dob_)
else:
   print_to_file("w", filename, your_age ,name_1, dob_)








