text = input("Matn kiriting: ")
length = int(input("Matn uzunligini kiriting: "))
text = text.rjust(length, "0")
print(text)
