import os
if __name__ == '__main__':
    print("Welcome to personal Speaker")
    while(True):
        x=input("Enter what you want me to speak")
        if(x=="q"):
            break
        else:
            command=f"say {x}"
            os.system(command)


