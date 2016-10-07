# -*- coding: utf-8 -*-
# Sabendo que str() converte valores numéricos em string,
# calcule quantos digitos há em 2 elevado a um milhão


class LenTwoMillion(object):

    def len_string(self):
        number = 2 * (10 ** 6)
        return len(str(number))
