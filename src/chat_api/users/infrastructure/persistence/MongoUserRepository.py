from src.shared.infrastructure.MongoRepository import MongoRepository
from src.chat_api.users.infrastructure.persistence.UserRepository import UserRepository
from src.chat_api.users.domain.valueobjects.UserPassword import UserPassword


class MongoUserRepository(MongoRepository, UserRepository):

    def search_by_username_and_password(self, username: str, password: UserPassword):
        return self.db.user.find_one({
            'email': username,
            'password': password.encrypted()
        })
