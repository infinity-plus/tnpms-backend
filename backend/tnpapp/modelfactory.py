from random import randint
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from factory.django import DjangoModelFactory
import factory
from tnpapp.models import CustomUser


class DjangoBaseUserModelFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: "USER-%010d" % n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")

    class Meta:
        model = AbstractUser
        abstract = True


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


class CustomUserFactory(DjangoBaseUserModelFactory):
    # TODO : this executes multiple times, is single hash multiple use possible?
    password = factory.LazyFunction(lambda: make_password("password"))
    phone_number = factory.LazyFunction(lambda: random_with_N_digits(10))

    class Meta:
        model = CustomUser
        abstract = True
