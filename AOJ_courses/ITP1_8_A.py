sent = input()

for i in sent:
    if i.isalnum():
        if i.isupper():
            if i == sent[len(sent) - 1]:
                print(i.lower()) 
            else:
                 print(i.lower(), end="")  

        elif i.islower():
            if i == sent[len(sent) - 1]:
                print(i.upper())
            else:
                print(i.upper(), end="")
        else:
            if i == sent[len(sent) - 1]:
                print(i)
            else:
                print(i, end="")
    else:
        if i == sent[len(sent) - 1]:
            print(i)
        else:
            print(i, end="")
    