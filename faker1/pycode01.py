# coding: utf-8

from faker import Faker


def gen_faker_data():
    f = Faker('zh_CN')
    for i in range(10):
        print(f.name())
        print(f.address())
        print(f.text())
        print(f.building_number())
        print(f.city())
        print(f.city_name())
        print(f.city_suffix())
        print(f.country())
        print(f.country_code(representation="alpha-2"))
        print(f.district())
        print(f.postcode())
        print(f.province())
        print(f.street_address())
        print(f.street_name())
        print(f.street_suffix())
        print(f.company())
        print(f.company_prefix())
        print(f.company_suffix())
        print(f.ipv4_private())

    pass


if __name__ == '__main__':
    gen_faker_data()
    pass
