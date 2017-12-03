'''
Program that uses temperature module for the actual calculations
Accept multiple conversion like below, by using argparse
-c2f 100 -f2c 90 -c2k -100
'''
#!usr/local/bin/python3.6
import argparse
import temperature

parser = argparse.ArgumentParser(description = 'convert temperature in differents units')

parser.add_argument('-c2f','--c2f', type = int, help='Convert from Celcius to Farenheit')
parser.add_argument('-f2c','--f2c', type = int, help='Convert from Farenheit to Celcius')
parser.add_argument('-c2k','--c2k', type = int, help='Convert from Celcius to Kelvin')

args = parser.parse_args()

print(args.c2f, '°C', '=', temperature.conv_C_F(args.c2f), '°F')
print(args.f2c, '°F', '=',temperature.conv_F_C(args.f2c), '°C')
print(args.c2k, '°C', '=',temperature.conv_C_k(args.c2k),'K')

