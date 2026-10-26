sentence = input("enter a sentence: ")

words = len(sentence.split())

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special_characters += 1

total_characters = len(sentence)
total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("\n========== sentence analysis ==========")
print(f"input sentence      : {sentence}")
print(f"total characters    : {total_characters}")

print("\n---------- character details ----------")
print(f"number of words     : {words}")
print(f"vowels              : {vowels}")
print(f"consonants          : {consonants}")
print(f"digits              : {digits}")
print(f"spaces              : {spaces}")
print(f"special characters  : {special_characters}")

print("\n----------- analysis summary -----------")
print(f"total letters       : {total_letters}")
print(f"vowel percentage    : {vowel_percentage:.1f}%")
print("========================================")
print("sentence analysis completed!")