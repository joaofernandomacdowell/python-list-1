# -*- coding: utf-8 -*-
# Calcular tempo de vida em minutos que um fumante perde


class SmokingTimeLine(object):

    def smoking_time_line(self, cigarretes_per_day, years):
        min_lost_in_one_day = cigarretes_per_day * 10
        return min_lost_in_one_day * (years * 365)
