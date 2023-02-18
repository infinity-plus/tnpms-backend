from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from typing import Any


def number_validator(value: Any, length: int) -> None:
    if len(value) != length:
        raise ValidationError(
            _(f"Number must be {length} digit long"),
        )
    if not all(i.isdigit() for i in value):
        raise ValidationError(_("Only numbers are allowed"))
