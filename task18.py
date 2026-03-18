text = input("Matn kiriting: ")
length = int(input("Matn uzunligini kiriting: "))
text = text.ljust(length, "0")
print(text)
