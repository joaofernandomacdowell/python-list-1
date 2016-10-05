# -*- coding: utf-8 -*-
# Faça um programa que receba o percentual de desconto
# e calcule o preço a pagar

from __future__ import division


class Discount(object):

    def salary_raise(self, price, discount):
        new_value = price * (discount / 100.0)
        return price - new_value
