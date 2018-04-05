import re
def ask():
    global S
    global d
    S = input("What is your word?\n")
    d = []
    def ask_words():
        try:
            global num
            num = int(input("How many words would you like to input?\n"))
        except ValueError:
            print("Please, put the integer")
            ask_words()
    ask_words()
    for i in range(0,num):
        d.append(str(input("Enter the word number " + str(i) + "\n")))
    print("We are looking for the word " + str(S) +
          " and the longest occurences of anything in "
        + str(d) + "\n")
def subseq(S,d):
    try:
        # every word in D is made into a regex pattern interspersed with .* and looked up in S
        in_dict = {word:len(word)
                   for word in d
                   if bool(re.search(pattern=".*".join(word),string=S))}
        print(max(in_dict, key=in_dict.get))
    except:
        print("There is no such subsequence")
ask()
subseq(S,d)
