import pytest

from django.urls import reverse, resolve
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_letting_url():
    user = User.objects.create(
        username="Test_user_2000",
        first_name="Test",
        last_name="User",
    )
    # Reverse URL using the correct kwarg
    path = reverse("profiles:profile", kwargs={"username": user.username})

    # Assert full path including app prefix
    assert path == f"/profiles/{user.username}/"

    # Resolve the path to check view name
    match = resolve(path)
    assert match.view_name == "profiles:profile"


@pytest.mark.django_db
def test_lettings_index_url():
    # Reverse URL for the index view (note the namespace)
    path = reverse("profiles:index")

    # Assert the path is correct
    assert path == "/profiles/"

    # Resolve the path to verify the view
    match = resolve(path)
    assert match.view_name == "profiles:index"
