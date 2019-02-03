import string
def remove_pattern(word):
    punc = string.punctuation
    stri = ""
    for p in punc:
        stri = word.strip()
        stri = word.replace(p,'')
    return stri
def sed(filename1,filename2):
     try:
        master = open(filename1,"r")
        slave = open(filename2,"w")
        for m in master:
            new = remove_pattern(m)
            slave.write(m)
        print("File write operation completed")
     except:
        print("Something went wrong!!!")
x = input("Enter master file for copy operation:")
y = input("Enter slave file:")
sed(x,y)
