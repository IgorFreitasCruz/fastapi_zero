from http import HTTPStatus


def test_read_root_return_OK_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Igor',
            'email': 'igor@test.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Igor',
        'email': 'igor@test.com',
    }


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Igor',
                'email': 'igor@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Igor Cruz',
            'email': 'test@test.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Igor Cruz',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user_not_found_error(client):
    response = client.put(
        '/users/5',
        json={
            'username': 'Igor Cruz',
            'email': 'test@test.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found_error(client):
    response = client.delete('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND
