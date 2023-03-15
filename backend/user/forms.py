from tnpapp.forms import BaseUserRegistrationForm
from user import models as m


class StudentRegistrationForm(BaseUserRegistrationForm):
    class Meta:
        model = m.Student
        fields = (
            "username",
            "password1",
            "password2",
            "enrollment_number",
        )
