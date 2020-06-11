# coding: utf-8

from faker import Faker
import pandas as pd
import time as t


def gen_faker_data():
    f = Faker('zh_CN')
    # for i in range(10):
    #     print(f.name())
    #     print(f.address())
    #     print(f.text())
    #     print(f.building_number())
    #     print(f.city())
    #     print(f.city_name())
    #     print(f.city_suffix())
    #     print(f.country())
    #     print(f.country_code(representation="alpha-2"))
    #     print(f.district())
    #     print(f.postcode())
    #     print(f.province())
    #     print(f.street_address())
    #     print(f.street_name())
    #     print(f.street_suffix())
    #     print(f.company())
    #     print(f.company_prefix())
    #     print(f.company_suffix())
    #     print(f.ipv4_private())

    p_csv = pd.DataFrame(
        data=list((f.name(), f.address(), f.building_number(), f.city(), f.city_name(),
                   f.city_suffix(), f.country(), f.country_code(representation="alpha-2"),
                   f.district(), f.postcode(), f.province(), f.street_address(),
                   f.street_name(), f.street_suffix(), f.company(), f.company_prefix(),
                   f.company_suffix(), f.ipv4_private()) for a in range(200000)),
        columns=["name", "address", "building_number", "city", "city_name", "city_suffix", "country",
                 "country_code", "district", "postcode", "province", "street_address", "street_name", "street_suffix",
                 "company", "company_prefix", "company_suffix", "ipv4_private"])
    p_csv.to_csv("C:/Users/cfa85/Desktop/dataset/data_" + t.time().__int__().__str__() + ".csv")

    pass


if __name__ == '__main__':
    gen_faker_data()
    pass
