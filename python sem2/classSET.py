#Create a class SET. Create member functions to perform the following SET operations:
#1. ismember: check whether an element belongs to the set or not and return value as true/false.
#2. powerset: list all the elements of the power set of a set.
#3. subset: Check whether one set is a subset of the other or not. 
#4. union and Interseection of two Sets. 
#5. complement: Assume Universal Set as per the input elements from the user. 
#6. set Difference and Symmetric Difference between two sets. 
#7 cartestian product of two sets.

#Write a menu driven program to perform the above fucntions on an instance of the SET class. 

class SET:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2
    def ismember(self, element):
        if element in self.set1:
            print("Element is in the set")
        else:
            print("Element is not in the set")
    def powerset(self):
        power_set = []
        for i in range(0, len(self.set1)+1):
            for j in range(i+1, len(self.set1)+1):
                power_set.append(self.set1[i:j])
        print(power_set)
    def subset(self):
        if self.set1.issubset(self.set2):
            print("Set 1 is a subset of set 2")
        else:
            print("Set 1 is not a subset of set 2")
    def union(self):
        print(self.set1.union(self.set2))
    def intersection(self):
        print(self.set1.intersection(self.set2))
    def complement(self):
        universal_set = set()
        for i in range(0, int(input("Enter the number of elements in the universal set: "))):
            universal_set.add(input("Enter the element: "))
        print(universal_set.difference(self.set1))
    def set_difference(self):
        print(self.set1.difference(self.set2))
    def symmetric_difference(self):
        print(self.set1.symmetric_difference(self.set2))
    def cartesian_product(self):
        cartesian_product = []
        for i in self.set1:
            for j in self.set2:
                cartesian_product.append((i, j))
        print(cartesian_product)

set1 = set()
set2 = set()
for i in range(0, int(input("Enter the number of elements in set 1: "))):
    set1.add(input("Enter the element: "))
for i in range(0, int(input("Enter the number of elements in set 2: "))):
    set2.add(input("Enter the element: "))
obj = SET(set1, set2)
while True:
    print("1. ismember")
    print("2. powerset")
    print("3. subset")
    print("4. union")
    print("5. intersection")
    print("6. complement")
    print("7. set difference")
    print("8. symmetric difference")
    print("9. cartesian product")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj.ismember(input("Enter the element to be checked: "))
    elif choice == 2:
        obj.powerset()
    elif choice == 3:
        obj.subset()
    elif choice == 4:
        obj.union()
    elif choice == 5:
        obj.intersection()
    elif choice == 6:
        obj.complement()
    elif choice == 7:
        obj.set_difference()
    elif choice == 8:
        obj.symmetric_difference()
    elif choice == 9:
        obj.cartesian_product()
    elif choice == 10:
        break
    else:
        print("Invalid choice")

#Output 

# Enter the number of elements in set 1: 3
# Enter the element: 1
# Enter the element: 2
# Enter the element: 3
# Enter the number of elements in set 2: 3
# Enter the element: 4
# Enter the element: 5
# Enter the element: 6
# 1. ismember
# 2. powerset
# 3. subset
# 4. union
# 5. intersection
# 6. complement
# 7. set difference
# 8. symmetric difference
# 9. cartesian product
# 10. Exit