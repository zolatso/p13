import pytest

from django.urls import reverse, resolve
from ..models import Letting, Address


@pytest.mark.django_db
def test_letting_url():
    address = Address.objects.create(
        number=34,
        street="Chase Avenue",
        city="Washington",
        state="WA",
        zip_code=13005,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Amazing House", address=address)
    # Reverse URL using the correct kwarg
    path = reverse("lettings:letting", kwargs={"letting_id": letting.id})

    # Assert full path including app prefix
    assert path == f"/lettings/{letting.id}/"

    # Resolve the path to check view name
    match = resolve(path)
    assert match.view_name == "lettings:letting"


@pytest.mark.django_db
def test_lettings_index_url():
    # Reverse URL for the index view (note the namespace)
    path = reverse("lettings:index")

    # Assert the path is correct
    assert path == "/lettings/"

    # Resolve the path to verify the view
    match = resolve(path)
    assert match.view_name == "lettings:index"
