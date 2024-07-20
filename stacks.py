def web_navigation():

    stack = []
    cont = 0

    while True:
        action  = input("add a url or interact with the words forward/backward/exit ")
        print(len(stack))
        if action == "add":
            url = input("what is the url?")
            stack.append(url)
        elif action == "exit":
            print("leaving the navigator")
            break
        elif len(stack)>=1:
            if action == "backward":
                stack.pop()
            else:
                print("invalid")
        else:
            print("you only have one url")

        if len(stack)>0:
            print(f"you have navigated to the web {stack[-1]}")
        else:
            print("add a url, you don't have any")
web_navigation()