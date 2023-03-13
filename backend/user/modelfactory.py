from tnpapp.modelfactory import CustomUserFactory
from user.models import Student
from user import roles as r
import factory
import factory.fuzzy
import datetime


class StudentFactory(CustomUserFactory):
    class Meta:
        model = Student

    marks = factory.fuzzy.FuzzyInteger(10, 100)
    institute = "GECM"
    department = factory.Iterator(r.Department.choices, getter=lambda c: c[0])
    semester = factory.fuzzy.FuzzyInteger(1, 8)
    batch_year = factory.fuzzy.FuzzyDateTime(
        datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc)
    )  # 4 character field possible
    is_profile_complete = False
    is_blocked = factory.Faker("boolean", chance_of_getting_true=30)
