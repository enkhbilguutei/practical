from random import randint 

def main():
    outfile = open("input.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9))+ " ")
        outfile.close()

        infile = open("input.txt", "r")
        s = infile.read()
        numbers = [eval(x) for x in s.split()]
        for number in numbers: 
            print(number, end = " ")
        infile.close()
main()


