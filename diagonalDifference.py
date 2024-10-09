def diagonalDifference(arr):
    ltr = []
    rtl = []

    for i in range(0,len(arr)):
            ltr.append(arr[i][i])
            rtl.append(arr[i][len(arr)-i-1])
    print(ltr)
    print(rtl)


    


diagonalDifference([[11,2,4],
                    [4,5,6],
                    [10,8,-12]
                    ])


