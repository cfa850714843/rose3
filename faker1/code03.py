# coding: utf-8

from faker import Faker
import pandas as pd
import time as t


def fun1():
    f = Faker('zh_CN')

    p_csv = pd.DataFrame(
        data=list((f.name(), f.text().replace('\n', '')) for a in range(20000)),
        columns=["name", "text"])
    p_csv.to_csv("C:/Users/cfa85/Desktop/dataset/data_" + t.time().__int__().__str__() + ".csv")
    pass


if __name__ == '__main__':
    fun1()
    pass
