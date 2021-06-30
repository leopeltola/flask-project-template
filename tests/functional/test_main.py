def test_index(client):
    rv = client.get("/")
    assert b"Index page" in rv.data


def test_about(client):
    rv = client.get("/about")
    assert b"About page" in rv.data


def test_404(client):
    rv = client.get("/this-page-doesnt-exist")
    assert b"404" in rv.data
