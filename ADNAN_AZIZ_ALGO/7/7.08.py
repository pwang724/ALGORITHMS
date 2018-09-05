def look_and_say(n):
    def helper(s, n):
        if n ==0:
            return s
        else:
            result = ''
            same = s[0]
            numsame = 1
            for i in range(1,len(s)):
                if s[i] == same:
                    numsame += 1
                else:
                    result += str(numsame) + same
                    numsame = 1
                    same = s[i]
            result += str(numsame) + same
            print(result)
            return helper(result, n-1)

    out = helper('1',n)
    return out[n]

if __name__ == '__main__':
    print(look_and_say(10))
