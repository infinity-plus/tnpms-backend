from tnpapp.modelfactory import CustomUserFactory
from user.models import Student
import factory
import factory.fuzzy
from user.serializers import calculate_semester




class StudentFactory(CustomUserFactory):

    class Meta:
        model = Student

    enrollment_number = factory.Sequence(lambda n: '200160107%03d' % n)
    marks = factory.fuzzy.FuzzyInteger(10, 100)
    batch_year = factory.LazyAttribute(
        lambda o: 2000 + int(o.enrollment_number[:2])
    )
    institute = factory.LazyAttribute(lambda o: o.enrollment_number[2:5])
    department = factory.LazyAttribute(lambda o :int(o.enrollment_number[7:9]))
    semester = factory.LazyAttribute(lambda o:calculate_semester(o.batch_year))
    is_profile_complete = False
    is_blocked = factory.Faker("boolean", chance_of_getting_true=30)
