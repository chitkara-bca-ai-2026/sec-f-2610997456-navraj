
sentence = input("enter a sentence: ")

position = int(input("enter position for indexing: "))
character = sentence[position]

start_index = int(input("enter start index for slicing: "))
end_index = int(input("enter end index for slicing: "))
sliced_string = sentence[start_index:end_index]

uppercase = sentence.upper()
lowercase = sentence.lower()

word_to_replace = input("enter word to replace: ")
replacement_word = input("enter replacement word: ")
after_replace = sentence.replace(word_to_replace, replacement_word)

length = len(sentence)

print("\n========== string analysis report ==========")
print(f"original sentence : {sentence}")
print("--------------------------------------------")
print(f"indexed character : {character}")
print(f"sliced string     : {sliced_string}")
print(f"uppercase         : {uppercase}")
print(f"lowercase         : {lowercase}")
print(f"after replacement : {after_replace}")
print("--------------------------------------------")
print(f"total characters  : {length}")
print("============================================")
print("string analysis completed successfully!")