#!usr/local/bin/python3.6
import unittest
import temperature

# unit test
class Test(unittest.TestCase):	
	def test_conv_C_k(self):
		''' test function for converting Celcius to Kelvin'''
		self.assertAlmostEqual(temperature.conv_C_k(-253.15),20 ,4)
		self.assertAlmostEqual(temperature.conv_C_k(-173.15),100 ,4)
		self.assertAlmostEqual(temperature.conv_C_k(25),298.15 ,4)	
	
	def test_conv_K_C(self):
		''' Test function for converting Kelvin to Celcius'''
		self.assertAlmostEqual(temperature.conv_K_C(20),-253.15 ,4)
		self.assertAlmostEqual(temperature.conv_K_C(100),-173.15 ,4)
		self.assertAlmostEqual(temperature.conv_K_C(298.15),25 ,4)

	def test_conv_C_F(self):
		''' Test function for converting Celcius to Farenheit'''
		self.assertAlmostEqual(temperature.conv_C_F(-12.2222),10 ,4)
		self.assertAlmostEqual(temperature.conv_C_F(10), 50,4)
		self.assertAlmostEqual(temperature.conv_C_F(37.7778), 100,4)

	def test_conv_F_C(self):
		''' Test function for converting Farenheit to Celcius'''
		self.assertAlmostEqual(temperature.conv_F_C(10), -12.2222,4)
		self.assertAlmostEqual(temperature.conv_F_C(50), 10,4)
		self.assertAlmostEqual(temperature.conv_F_C(100), 37.7778,4)

	
	def test_conv_K_F(self):
		''' Test function for converting Kelvin to Farenheit'''
		self.assertAlmostEqual(temperature.conv_K_F(0), -459.67,4)
		self.assertAlmostEqual(temperature.conv_K_F(260), 8.33,4)

	def test_conv_F_K(self):
		''' Test function for converting Farenheit to Kelvin'''
		self.assertAlmostEqual(temperature.conv_F_K(-459.67), 0,4)
		self.assertAlmostEqual(temperature.conv_F_K(8.33), 260,4)

unittest.main()
