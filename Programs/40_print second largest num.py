#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		srt_list = sorted(arr)
		ans = []
		for i in srt_list:
		    if i not in srt_list:
		        srt_list.append(i)
    return srt_list[1]
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1
