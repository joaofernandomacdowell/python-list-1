# -*- coding: utf-8 -*-
# Calcule o valor do aluguel de um carro.
# Sabendo que o carro custa R$ 60,00 por dia
# E 0.15 por km rodado


class RentedCar(object):

    def rented_car(self, days, km):
        value = (days * 60) + (km * 0.15)
        str = "%.2f" % value
        return float(str)
