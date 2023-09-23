import instaloader
import getpass

username = input("please enter your username: ")
password = getpass.getpass("enter your password: ")

f = open("followers.txt", "r")
old_followers.append(line)

f.close()

l = instaloader.instaloader()

l.login(username, password)
print("ok,✅🎉")

