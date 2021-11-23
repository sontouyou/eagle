
def test(arr: list[int]) -> int:
    result = 0
    lenarr = len(arr)
    if lenarr <= 2:
        return result
    maxitem1 = max(enumerate(arr), key=lambda x: x[1])
    rearr = list(reversed(arr))
    maxidx2 = rearr.index(maxitem1[1])
    remaxidx2 = lenarr - 1 - maxidx2
    if remaxidx2 - maxitem1[0] > 1:
        result = result + sum(arr[maxitem1[0] + 1 : remaxidx2]) * (-1) + (remaxidx2 - maxitem1[0] - 1) * maxitem1[1]
    for i in [1,2]:
        lst = []
        endindex = 0
        if i == 1:
            lst = arr
            endindex = maxitem1[0]
        else:
            lst = rearr
            endindex = maxidx2
        if endindex < 2:
            continue
        while 0 < endindex:
            arr1 = lst[0:endindex]
            maxitm = max(enumerate(arr1), key=lambda x: x[1])
            p1e = maxitm[0]
            minv1 = maxitm[1]
            if endindex - p1e == 1:
                endindex = p1e
                continue
            result = result + sum(lst[p1e+1:endindex]) * (-1) + (endindex - p1e - 1) * minv1
            endindex = p1e
    return result


#tt=[7,10,13,10,3,6,2,8,3,5,2,2,2,2,1,1,4,1,1,1,1]
tt=[]
for i in range(1000000):
    tt.append(2)

print(test(tt))
