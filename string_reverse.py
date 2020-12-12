'''
how is a string reversed
'''
def reverseList(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1

a=list(input())
reverseList(a,0,len(a)-1)
#print(a)
rev_s="".join(a)
print("reversed string:",rev_s)
