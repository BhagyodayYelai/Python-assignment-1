import string

with open("sample.txt", "r") as input_file:
    text = input_file.read()

translator = str.maketrans('', '', string.punctuation)
text_no_punct = text.translate(translator)
text_lower = text_no_punct.lower()

words = text_lower.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

with open("word_report.txt", "w") as output_file:
    for word, count in sorted_words:
        output_file.write(f"{word}: {count}\n")

print("Report saved to word_report.txt")