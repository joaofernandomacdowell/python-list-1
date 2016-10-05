# -*- coding: utf-8 -*-
# Faça um programa que calcule o aumento de um salário.
# Deve solicitar o valor do salário e a porcentagem de aumento

from __future__ import division


class SalaryRaise(object):

    def calculate_raise(self, percent):
        return 1.0 + (percent / 100.0)

    def salary_raise(self, salary, percent):
        new_raise = 1.0 + (percent / 100.0)
        new_salary = salary * new_raise
        return int(new_salary)
