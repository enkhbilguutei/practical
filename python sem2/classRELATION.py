#Create a class RELATION, use Matrix notation to represent a relation. Include member fucntions to check if the relation is Reflexive, Symmetric, Anti-Symmetric, Transitive and Equivalence relation.
#Using these functions check whether the givern relation is: Equivalnce, Partial Order relation or None of these. 

class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
    def reflexive(self):
        for i in range(0, len(self.matrix)):
            if self.matrix[i][i] == 0:
                return False
        return True

    def symmetric(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def anti_symmetric(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1 and i != j:
                    return False
        return True


#output 

# >>> from 2 import *
# >>> r = RELATION([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# >>> r.reflexive()
# True
# >>> r.symmetric()
# True
# >>> r.anti_symmetric()
# True

    



