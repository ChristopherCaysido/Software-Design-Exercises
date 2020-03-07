from doctor import Doctor
def main():
    d = Doctor()
    print(d.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(d.farewell())
            break
        print(d.reply(sentence))

if __name__ == "__main__":
    main()