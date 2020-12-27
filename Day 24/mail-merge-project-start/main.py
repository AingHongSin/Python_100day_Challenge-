#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode ='r') as name_file:
    names = name_file.read().split('\n')

# print(invited_name)
print("NameList:", names)

for name in names:
    print("Name:", name)
    with open("./Input/Letters/starting_letter.docx", mode='r') as letter_file:
        text = letter_file.read()
        after = text.replace("[name]", f"{name}")
        print(after)

    with open(f"./Output/ReadyToSend/Send_to_{name}.txt", mode = 'w') as output_file:
        output_file.write(f"{after}")



print("Sucessfully...")