string = "You can have data without information, but you cannot have information without data."
dict = {}
new_str=''
for ch in string:
    if ch.lower() not in [' ', ',', '.']:
        new_str+=ch.lower()
for letter in new_str:
    if letter not in dict.keys():
        dict[letter]=0
    else:
        dict[letter]=new_str.count(letter)

for key, value in dict.items():
    print(f'{key}:{value}')