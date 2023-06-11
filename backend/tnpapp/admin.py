from django.contrib import admin
from typing import Tuple, Any
from copy import deepcopy
from django.http import HttpResponse
import csv


def append_primary_fields(
    data: Tuple[Any, ...],
    # data: Tuple[Any, ...],
    new_fields=Tuple[str, ...],
):
    tmp_data = deepcopy(data)
    tmp_data[0][1]["fields"] = (*tmp_data[0][1]["fields"], *new_fields)
    return tmp_data


# https://docs.djangoproject.com/en/4.1/ref/contrib/admin/actions/#actions-that-provide-intermediate-pages
# https://docs.djangoproject.com/en/4.1/howto/outputting-csv/
# TODO : add custom permission for exports
def export_as_csv(modeladmin, request, queryset) -> HttpResponse:
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta}.csv"
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response


admin.site.add_action(export_as_csv, "export_selected")

# def append_primary_fields(
#     data: Tuple[Any, ...],
#     new_fields=Set[str],
# ):
#     tmp_data = copy(data)
#     tupleset = set(tmp_data[0][1]["fields"]).union(new_fields)
#     tmp_data[0][1]["fields"] = tuple(tupleset)
#     return tmp_data
