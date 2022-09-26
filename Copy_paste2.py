import pyperclip
text1 = "代表取締役社長"
text2 = "ありがとう"
text3 = "ありがとうございました"
give_choice = int(input("Enter your choice "))
if give_choice == 1:
    pyperclip.copy(text1)
elif give_choice == 2:
    pyperclip.copy(text2)
elif give_choice == 3:
    pyperclip.copy(text3)
else:
    print("Invalid choice")