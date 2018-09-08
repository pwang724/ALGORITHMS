class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            #find biggest prefix that is also a suffix of p[i-1], with condition that the next char after prefix is also p[i]
            #has two conditions, either fail, in which case j = 0, or succeed, in which case j > 0
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]

            #if success, then p[j] == p[i] always. if fail, then j=0, and not guaranteed that p[j] == p[i]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]

            #j == 0, match, else do nothing
            if T[i] == P[j]: j += 1


            if j == len(P):
                ret.append(i - (j - 1))
                j = 0
        return ret

    def search1(self, T, P):
        partial, ret, j, i = self.partial(P), [], 0, 0

        while (i < len(T)):
            if j == 0:
                if T[i] == P[j]:
                    j+=1
                i+=1
            else:
                if T[i] == P[j]:
                    j+=1
                    i+=1
                else:
                    j = partial[j-1]



if __name__ == '__main__':
    a = KMP()
    print(a.partial('ababcabaz'))
    