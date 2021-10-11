# -*- coding:utf-8 -*-
from faker import Faker

faker=Faker("zh_CN")
name=faker.name()
aa=faker.numerify()
print(name)
print(aa)