def main():
    txt = input("Please enter some text:")
    output(txt, count(txt))
def count(k):
    num = len(k)
    return num
def output(txt,num):
    if num != 0:
        print(txt, "has", num, "characters.")
    else:
        print("You have to enter some text!")
main()