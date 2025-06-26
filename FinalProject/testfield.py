import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", type=int, default=2, help="number of decimal places")  # default to 2 places maybe~

args = parser.parse_args()
flo = args.f

some_number = 3.1415926535

# use flo in format string
formatted = "{:.{}f}".format(some_number, flo)

print("formatted number: {formatted}")
