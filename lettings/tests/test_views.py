import pytest

from django.urls import reverse
from django.test import Client
from ..models import Letting, Address
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db  
def test_letting_view():
    client = Client()
    address = Address.objects.create(
        number = 34,
        street = "Chase Avenue",
        city = "Washington",
        state = "WA",
        zip_code = 13005,
        country_iso_code = "USA",
    )
    letting = Letting.objects.create(
        title = "Amazing House",
        address = address
    )
    # Reverse URL using the correct kwarg
    path = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<p>34 Chase Avenue</p>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")



@pytest.mark.django_db  
def test_letting_index_view():
    client = Client()
    address1 = Address.objects.create(
        number=34,
        street="Chase Avenue",
        city="Washington",
        state="WA",
        zip_code=13005,
        country_iso_code="USA",
    )
    address2 = Address.objects.create(
        number=12,
        street="Main Street",
        city="Seattle",
        state="WA",
        zip_code=98101,
        country_iso_code="USA",
    )

    Letting.objects.create(title="Amazing House", address=address1)
    Letting.objects.create(title="Cozy Apartment", address=address2)

    # Reverse URL for the index view (note the namespace)
    path = reverse('lettings:index')

    response = client.get(path)

    assert "lettings_list" in response.context
    assert response.context["lettings_list"].count() == 2
