from collections import UserList


class user_list(UserList):
    def append(self, s=None):
        raise RuntimeError("Authority denied for new insertion")


# trying to insert new element
my_list = user_list([10, 11, 12])
my_list.append(13)
