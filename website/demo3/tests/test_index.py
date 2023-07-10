import pytest
from django.test import Client
from django.shortcuts import reverse

import pytest

from .factories import PersonFactory


def test_index():
    client = Client()
    response = client.get(reverse("demo3:index"))
    assert "Hello from demo3" in str(response.content)


@pytest.mark.django_db
def test_make_person():
    person = PersonFactory.create()

    assert person.first_name is not None


#####################################################################################
## monkeypatching
import requests


class MockResponse(requests.Response):
    """build the response that behaves as you want it"""

    def content(self):
        return "Hello World"


def mock_get_response(*args, **kwargs):
    """build a function that returns the mock response"""
    return MockResponse()


@pytest.fixture
def requests_get_shield(monkeypatch):
    """set up a fixture to override requests.get with your function"""
    monkeypatch.setattr(requests, 'get', mock_get_response)


def test_monkey(requests_get_shield):
    """inject the shield fixture into your test"""
    response = requests.get("https://www.google.com")

    assert response.content() == 'Hello World'
