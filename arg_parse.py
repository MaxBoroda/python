#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser(description='Process summ of range')
parser.add_argument('a', type=int, help='a_start of the range')
parser.add_argument('b', type=int, help='b_end of the range')

args = parser.parse_args()

if args.a >= args.b:
    parser.error('"a" number must be less then "b"')

numbers = range(args.a, args.b)
sum = reduce(lambda x, y: x + y, numbers)

print("Result of summing numbers in range[{:n}, {:n}] is {:n}".format(args.a,
                                                                args.b, sum))
