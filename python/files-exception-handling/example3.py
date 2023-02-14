def main():
    filename = input("Enter a filename: ").strip()
    
    try:
        with open(filename, "r") as infile:
            counts = [0] * 26
            for line in infile: 
                line = line.lower()
                counts = [counts[i] + (1 if ch.isalpha() else 0) for i, ch in enumerate(line)]

            for i, count in enumerate(counts): 
                if count != 0:
                    print(f"{chr(ord('a') + i)} appears {count} time{'s' if count != 1 else ''}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

main()
