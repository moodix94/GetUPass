import getpass
import pwd

print("     GetUPass  \n Twitter: @imohafa \n Github: @imohafa \n")


def UserName():
    User = getpass.getuser()
    return User


print(f' User: {UserName()}')


def UserPass():
    # you can change it to (0) for 'root', (501) for 'user'.
    Pass = pwd.getpwuid(501)
    return Pass


print(f' Pwd Inf: {UserPass()}')
