from sqlalchemy.orm.scoping import scoped_session
from project.dao.models import User
from project import config


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def get_all(self, data_filter):
        users = self._db_session.query(User)

        # Обрабатываем пагинацию
        page = data_filter.get('page')

        if page is not None:
            page_int = int(data_filter.get('page'))
            users = users.paginate(page_int, config.BaseConfig.ITEMS_PER_PAGE, False)

            return users.items
        else:
            return users.all()

    def create(self, user_d):
        self._db_session.add(User(**user_d))
        self._db_session.commit()

    def delete(self, pk):
        user = self.get_by_id(pk)
        self._db_session.delete(user)
        self._db_session.commit()

    def update(self, user_d):
        user = self.get_by_id(user_d.get("id"))

        email = user_d.get("email")
        if email is not None:
            user.email = user_d.get("email")

        password = user_d.get("password")
        if password is not None:
            user.password = user_d.get("password")

        name = user_d.get("name")
        if name is not None:
            user.name = user_d.get("name")

        surname = user_d.get("surname")
        if surname is not None:
            user.surname = user_d.get("surname")

        favorite_genre = user_d.get("favorite_genre")
        if favorite_genre is not None:
            user.favorite_genre = user_d.get("favorite_genre")

        role = user_d.get("role")
        if role is not None:
            user.role = user_d.get("role")

        self._db_session.add(user)
        self._db_session.commit()
