from db.db import UserRepository

UserRepository.set_user(name='Yari', fullname='Yari Taft', nickname='ytaft')
print(UserRepository.get_user_by_name(name='Yari'))