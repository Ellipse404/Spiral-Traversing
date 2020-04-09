def spiral(m,n,a) :
    k = l = 0                                                                   # m = number  of  rows 
    while(k<m and l<n) :
#  printing  the  first  row from the remaining rows       # n = number  of  column
        for i in range(l,  n) :
            print(a[k][i], end = " ")                                           #  k = index  of  starting  row
        k+=1
# printing the last column from the remaining column      #  l = index  of  starting  column
        for i in range(k,m) :
            print(a[i][n-1], end = " ")
        n-=1
        
        if(k<m) :
# printing the last row from remaining rows
            for i in range(n-1,l-1,-1) :
                print(a[m-1][i], end = " ")
            m-=1
        if(l<n) :
# printing the first column from the remaining columns
            for i in range(m-1,k-1,-1) :
                print(a[i][l], end = " ")
            l+=1

a = []
count = 1
for i in range(5) :
    p = []
    for j in range(5) :
        p.append(count)
        count+=1
    a.append(p)

spiral(5,5,a)

