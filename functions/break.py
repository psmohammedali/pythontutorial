
try:
    i = 1
    while i < 9:
        print(i)
        break
        i += 1
except IndentationError:
    print("identation error")