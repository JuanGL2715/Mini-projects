def shared_printed():
    queue = []

    while True:
        action = input("add a document or select print/exit: ")
        if action == "print":
            if len(queue)>0:
                print(f"the document {queue[0]} was printed ")
                queue.pop(0)
            else:
                print("you don't have any documents to print")
        if action == "add":
            queue.append(input("what's the document: "))
        if action == "exit":
            break

        print(f"print queue {queue}")
shared_printed()