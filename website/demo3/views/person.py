from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from vanilla import ListView, DetailView, CreateView, UpdateView

from demo3.models import Person


def index(request):
    return render(request, "demo3/index.html")


class PersonListView(ListView):
    model = Person
    template_name = 'demo3/person_list.html'

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class PersonProxy(Person):
    class Meta:
        proxy = True

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in self.__class__._meta.fields
        ]


# doing as much as I can through configuration
class PersonDetailView(DetailView):
    model = PersonProxy
    template_name = 'demo3/person_detail.html'
    lookup_field = "uuid"
    lookup_url_kwarg = 'person_uuid'


# an example of LoginRequiredMixin
class PersonCreateView(LoginRequiredMixin, CreateView):
    model = PersonProxy
    fields = [
        'first_name',
        'last_name',
        'email',
    ]

    template_name = 'demo3/person_create.html'
    success_url = reverse_lazy("demo3:person-list")

    def form_valid(self, *args, **kwargs):
        ret = super().form_valid(*args, **kwargs)

        messages.success(self.request, f"{self.object} has been created")

        return ret


# Doing a lot of custom work (the hard way)
class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'company',
            'address',
            'city',
            'state',
            'postal_code',
        ]


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonUpdateForm
    template_name = "demo3/person_update.html"
    success_url = reverse_lazy("demo3:person-list")

    def get_object(request):
        # replaces lookup_field and lookup_url_kwarg
        return Person.objects.get(uuid=request.kwargs['person_uuid'])

    def form_valid(self, *args, **kwargs):
        ret = super().form_valid(*args, **kwargs)

        messages.success(self.request, f"{self.object} has been updated")

        return ret
