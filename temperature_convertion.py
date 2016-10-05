# -*- coding: utf-8 -*-
# Converta uma temperatura em Celsius para Fahrenheit

from __future__ import division


class TemperatureConvertion(object):

    def convert_celsius_to_fahrenheit(self, celsius):
        fahrenheit = 9 * (celsius / 5) + 32
        return fahrenheit

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) / 1.8
        return celsius
