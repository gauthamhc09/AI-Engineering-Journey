"""AI Command Router
chat

translate

summarize

code

image """

command = input("Please enter the command: ")

match command:
    case "chat":
        print("It is a chat command")
    case "translate":
        print("It is a translate command")
    case "summarize":
        print("It is a summarize command")
    case "code":
        print("It is a code command")
    case "image":
        print("It is a image command")
    case _:
        print("Invalid command")
        
score = 7000

if(score>=8000):
    print("Great score")
else:
    print("Average score")