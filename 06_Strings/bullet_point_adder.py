import pyperclip

text = pyperclip.paste()

#Separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = f"* {lines[i]}"  # add star to each string in "lines" list


text = "\n".join(lines)

pyperclip.copy(text)

#output on terminal since pyperclip.copy(text) paste the output on clipboard and we cannot see it running
print(text)