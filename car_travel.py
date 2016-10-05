# -*- coding: utf-8 -*-
# Calcule o tempo de uma viagem de carro. Receba a
# distância e a velocidade média e retorne o tempo esperado

from __future__ import division


class CarTravel(object):

    def car_travel(self, distance, average_speed):
        time = distance / average_speed

        if distance % average_speed == 0:
            return int(round(time))

        else:
            return "%.2f" % time

