# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Person
from .models import Profile


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'first_name',
        'last_name',
        'email',
        'company',
        'address',
        'city',
        'state',
        'postal_code',
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
