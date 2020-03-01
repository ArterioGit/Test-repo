# #!/usr/local/bin/python3
import sys

import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

print(sys.executable + "")
print(sys.version)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def albert():
        pass

    def test_method(self):
        pass

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def pippo(self):
        pass


emp_1 = Employee("Alessandro", "Bigucci")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print("essential")
