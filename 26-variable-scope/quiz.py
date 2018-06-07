def main():
    funcs = []
    for i in range(4):
        funcs.append(lambda: print(i))

    funcs[0]()

main()
