import pickle 

def main():

    outfile = open("pick.dat", "wb")
    pickle.dump(45, outfile)
    pickle.dump(56.6, outfile)
    pickle.dump("Programming is fun", outfile)
    pickle.dump([1, 2, 3, 4], outfile)
    outfile.close()

    infile = open("pick.dat", "rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
main()