
def main():
    # Your code goes here
    # s=input()
    # for i in s:
    #     print(i)
    cnt=0
    b=0
    TwoD
    while(True):
        
        s = input()
        
        if not s:
            break;
        else: 
            #TwoD.append(s);
            b=len(s)
            cnt+=1
            print('[',end='')
            for i in range(len(s)):
                if i == len(s)-1:
                    print(s[i],'],',sep='')
                else:
                    print(s[i],',',sep='',end='')
            #print(']')
    print(cnt,b)

if __name__ == "__main__":
    main()
