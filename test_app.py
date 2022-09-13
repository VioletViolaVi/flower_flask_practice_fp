# GOOD TO KNOW &n about needing it's file!!!
from urllib import response


def test_index_route(api):
    response = api.get("/")

    assert response.status == "200 OK"

    assert b"Welcome to the Flower Factory!" in response.data


def test_flowers_post_route(api):
    response = api.post("/flowers")

    assert response.status == "405 METHOD NOT ALLOWED"
    assert response.status_code == 405


def test_new_flower_route(api):
    response = api.post("/flower/new")

    assert response.status_code == 400

    data = {
        "colour": "green"
    }

    response = api.post("/flower/new", json=data)

    assert response.status_code == 200
