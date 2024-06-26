from sqlalchemy import Select

from fastapi_zero.models import User


def test_create_user(session):
    user = User(
        username='igorcruz',
        email='igor@email.com',
        password='teste1234',
    )
    session.add(user)
    session.commit()

    result = session.scalar(Select(User).where(User.username == 'igorcruz'))

    assert result.id == 1
    assert result.username == 'igorcruz'
