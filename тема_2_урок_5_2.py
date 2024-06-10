word = input("Введите слово из маленьких латинских букв: ")
vow = {'a', 'e', 'i', 'o', 'u'}

count_vowels = sum(1 for let in word if let in vow)
count_cons = len(word) - count_vowels

print("Количество гласных букв:", count_vowels)
print("Количество согласных букв:", count_cons)