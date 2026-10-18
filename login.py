#program stores a correct username and a correct password
#program asks user to enter username
#program asks user to enter the password
#program checks whether entered info is mathced with the stored info
# if info is correct, program allows access
# #otherwise program denies access 


correct_username = "android"
correct_password = "windows"

username = input("enter your user name ")
password = input("enter your password ")

#if username == correct_username or password == correct_password:
#  print(f"welcome to valgeklaar, Android!")

#else: git
#  print(f"access denied, {username}")


if username != correct_username or password != correct_password:
  print("access denied")
else: 
  print(f"hello again, {correct_username}") 



