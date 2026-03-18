username = input("GitHub username kiriting: ")
username = username.replace("-", "")
if username.isalnum():
    print("GitHub username to'g'ri formatda.")
else:
    print("GitHub username noto'g'ri formatda.")
