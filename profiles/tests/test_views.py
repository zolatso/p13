import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed

from ..models import Profile


@pytest.mark.django_db
def test_profile_view():
    client = Client()
    user = User.objects.create(
        username="Test_user_2000",
        first_name="Test",
        last_name="User",
    )
    profile = Profile.objects.create(user=user, favorite_city="London")
    # Reverse URL using the correct kwarg
    path = reverse("profiles:profile", kwargs={"username": profile.user.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = [
        f"<p><strong>First name :</strong> {profile.user.first_name}</p>",
        f"<p><strong>Last name :</strong> {profile.user.last_name}</p>",
        f"<p><strong>Favorite city :</strong> {profile.favorite_city}</p>",
    ]

    assert all(item in content for item in expected_content)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
def test_profile_index_view():
    client = Client()
    user_1 = User.objects.create(
        username="Test_user_2000",
        first_name="Test",
        last_name="User",
    )
    user_2 = User.objects.create(
        username="Test_user_3000",
        first_name="Tom",
        last_name="Saunders",
    )
    profile_1 = Profile.objects.create(user=user_1, favorite_city="London")
    profile_2 = Profile.objects.create(user=user_2, favorite_city="Paris")

    # Reverse URL for the index view (note the namespace)
    path = reverse("profiles:index")

    response = client.get(path)

    assert "profiles_list" in response.context
    assert response.context["profiles_list"].count() == 2
