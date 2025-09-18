from django.urls import reverse, resolve


def test_root_url():
    path = reverse("index")

    assert path == "/"
    # Resolve the path to check view name
    match = resolve(path)
    assert match.view_name == "index"
