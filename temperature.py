#!usr/local/bin/python3.6
'''Module "temperature which converts from Celcius to Farenheit and Kelvin an vice versa
Celcius = (Farenheit -32)* 5/9
Farenheit = Celcius * 9/5 +32
Kelvin = Celcius + 273.15
Celcius = Kelvin - 273.15
'''

def conv_C_k(tempC):
	''' Conversion Celcius-Kelvin '''
	tempK = tempC + 273.15
	return tempK

def conv_K_C(tempK):
	''' Conversion Kelvin-Celcius'''
	tempC = tempK - 273.15
	return tempC

def conv_C_F(tempC):
	'''Conversion Celcius Farenheit'''
	tempF = tempC *9/5 + 32
	return tempF


def conv_F_C(tempF):
	'''Conversion Farenheit-Celcius'''
	tempC = (tempF - 32)*5/9
	return tempC

def conv_K_F(tempK):
	''' Conversion Kelvin-Farenheit'''
	tempF = tempK * 9/5 -459.67
	return tempF

def conv_F_K(tempF):
	''' Conversion Farenheit-Kelvin'''
	tempK = (tempF + 459.67)*5/9
	return tempK


