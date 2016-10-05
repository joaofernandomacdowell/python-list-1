# -*- coding: utf-8 -*-
# Faça um programa que leia a quantidade de dias, horas, minutos e
# segundos. Calcule o total em segundos


class TimeConvertion(object):

    def time_to_seconds(self, days, hour, min, sec):

        if days >= 0 and hour >= 0 and min >= 0 and sec >= 0:
            seconds = sec
            seconds += min * 60
            seconds += hour * 3600
            seconds += days * 86400

            return seconds

        else:
            raise ValueError
