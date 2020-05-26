import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from db.db import UserRepository
from httpReq.user_http import send_user

def set_and_print_user(name, fullname):
    nickname = "".join([name[0], fullname.split(" ")[1]])
    UserRepository.set_user(name, fullname, nickname)
    user_saved = (UserRepository.get_user_by_name(name=name))
    send_user(user_saved)

set_and_print_user("yari", "yari taft")