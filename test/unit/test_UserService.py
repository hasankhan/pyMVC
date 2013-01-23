from TestCase import TestCase
from services.UserService import UserService, DuplicateUserException
from services.data_access.UserRepository import UserRepository
from services.entities.User import User
from mock import create_autospec

class UserServiceTest(TestCase):

    def __get_service_with_mock_repository(self):
        MockRepository = create_autospec(UserRepository)
        repository = MockRepository()
        service = UserService(repository)
        return service, repository
        
    def test_rejects_duplicate_user(self):
        service, repository = self.__get_service_with_mock_repository()
        repository.get_user_by_username.return_value = User()
        
        with self.assertRaises(DuplicateUserException):
            service.create_user(User())
        
    def test_creates_non_existing_user(self):
        service, repository = self.__get_service_with_mock_repository()        
        repository.get_user_by_username.return_value=None
        
        user = User()
        
        service.create_user(user)
        repository.add_user.assert_called_with(user)
