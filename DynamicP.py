import numpy
from pprint import pprint


class DynamicP():

    class MatrixSolution():
        D = [0]
        backtrack = [""]
        def __init__(self, sequencelen1,sequencelen2 ):
            self.D = [[0 for x in range(sequencelen1 + 1)] for y in range(sequencelen2 + 1)]
            self.backtrack = [[0 for x in range(sequencelen1 + 1)] for y in range(sequencelen2 + 1)]


    def NeedlemanWunsch(self, sequence1, sequence2, g):
        #D(i,j) = max(D(i-1, j-1) + S(i=>j), D(i-1, j) + G, D(i, j-1) + g)
        M = self.MatrixSolution(len(sequence1), len(sequence2))

        M.D[0][0] = 0
        #substitution matrix is just an arbitiary number but should use BLOSSUM62
        S = 2

        for rqScore in range(1, len(sequence1) + 1):
            M.D[0][rqScore] = M.D[0][rqScore -1] + g
            M.backtrack[0][rqScore] = "left"


        for cqScore in range(1, len(sequence2) + 1):
            M.D[cqScore][0] = M.D[cqScore -1][0] + g
            M.backtrack[cqScore][0] = "up"

        for i in range(1, len(sequence1) + 1):
            for j in range(1, len(sequence2) + 1):
                direction = ""
                maxR = -99999999
                ntMax = M.D[i - 1][j - 1] + S
                if (ntMax > maxR):
                    maxR = ntMax
                    M.backtrack[i][j] = "diag"
                ntMax = M.D[i - 1][j] + g
                if (ntMax > maxR):
                    maxR = ntMax
                    M.backtrack[i][j] = "up"
                ntMax = M.D[i][j - 1] + g
                if (ntMax > maxR):
                    maxR = ntMax
                    M.backtrack[i][j] = "left"

                M.D[i][j] = maxR

        return M
