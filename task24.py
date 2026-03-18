email = input("Email manzilingizni kiriting: ")
if not email.startswith("@") and email.endswith(".com"):
    print("Email manzili tog'ri formatda.")
else:
    print("Email manzili noto'g'ri formatda.")
