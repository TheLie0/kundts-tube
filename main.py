#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sin,cos,pi

class Tube(object):

	def __init__(self, length, left_open = False, right_open = True ):
		"""Takes length in Meters of the tube and the state of either end"""

		self.length = length
		self.kind = ""

		if left_open:
			self.kind += "O"
		else:
			self.kind += "C"

		if right_open:
			self.kind += "O"
		else:
			self.kind += "C"

	@property
	def __str__(self):

		if self.kind == "OC" or self.kind == "CO":
			return "Kundt's tube with one open end"
		elif self.kind == "OO":
			return "Kundt's tube with two open ends"
		else:
			return "Kundt's tube with two closed ends"

	def get_wavelength(self, n):

		if self.kind == "OC" or self.kind == "CO":
			return (4 * self.length) / (2 * n + 1)
		else:
			return (2 * self.length) / (n + 1)

	def get_frequency(self, n):

		return 343/self.get_wavelength(n)

	def wave_function(self, n, x):

		if self.kind == "OC":
			return cos((0.5 + n) * pi * x / self.length)
		elif self.kind == "CO":
			return sin((0.5 + n) * pi * x / self.length)
		elif self.kind == "OO":
			return cos((1 + n) * pi * x / self.length)
		else:
			return sin((1 + n) * pi * x / self.length)

	def get_wave_points(self, n , steps):

		step, point = self.length/(steps -1), 0
		while point <= self.length:
			yield self.wave_function(n, point)
			point += step

	def get_visual_wave_points(self, n, steps):

		outStr = ""

		for val in self.get_wave_points(n, steps):
			if abs(val) < 1/3:
				outStr += chr(9617)
			elif abs(val) < 2/3:
				outStr += chr(9618)
			else:
				outStr += chr(9619)


		if self.kind == "OC":
			outStr = "0" + outStr + "|"
		elif self.kind == "CO":
			outStr = "|" + outStr + "0"
		elif self.kind == "OO":
			outStr = "0" + outStr + "0"
		else:
			outStr = "|" + outStr + "|"

		return outStr

if __name__ == "__main__":

	test_tube = Tube(1.5, False, False)
	for num in range(20):
		print(test_tube.get_visual_wave_points(num,70) + " " + str(test_tube.get_frequency(num)) + "Hz")