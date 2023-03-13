from rest_framework.permissions import DjangoModelPermissions


class FineGrainedPermissions(DjangoModelPermissions):
    # ovveride 'GET', and add "view" perimission to deny viewing
    # eg "GET": ["%(app_label)s.view_%(model_name)s"],
    # original = "GET" : []
    perms_map = {
        "GET": [],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }
