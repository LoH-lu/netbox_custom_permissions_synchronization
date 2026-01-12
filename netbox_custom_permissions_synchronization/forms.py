from django import forms


class PermissionsSyncForm(forms.Form):
    sync_all = forms.BooleanField(required=False)
