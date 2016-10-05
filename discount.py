# -*- coding: utf-8 -*-
# Faça um programa que calcule o aumento de um salário.
# Deve solicitar o valor do salário e a porcentagem de aumento


class Discount(object):

    def calculate_discount(self, percent):
        return 1.0 + (percent / 100.0)

    def salary_raise(self, price, discount):
        porcentagem = percent / 100.0
        porcentagem = 1.0 + porcentagem
        new_salary = salary * porcentagem
        return int(new_salary)
