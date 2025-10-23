from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_index_view():
    client = Client()
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Orange County Lettings 2023"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_404():
    client = Client()
    path = "/made_up_path_name"
    response = client.get(path)

    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
