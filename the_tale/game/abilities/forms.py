# coding: utf-8

from dext.forms import forms, fields

class AbilityForm(forms.Form):

    hero_id = fields.HiddenIntegerField()
