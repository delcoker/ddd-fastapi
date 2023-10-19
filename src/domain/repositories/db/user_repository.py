from abc import abstractmethod, ABC


class UserRepository(ABC):

    @abstractmethod
    def get_users(self):
        pass
