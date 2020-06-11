# coding: utf-8

import pandas as pd
import time as t
import random


def fun1():
    p_csv = pd.DataFrame(
        data=list((list(random.randint(0, 100) for a in range(15))) for a in range(200000)),
        columns=list(('c' + str(a)) for a in range(15)), index=None)
    p_csv.to_csv("C:/Users/cfa85/Desktop/dataset/data_" + t.strftime("%H%M%S").__str__() + ".csv")
    pass


if __name__ == '__main__':
    fun1()
    pass
