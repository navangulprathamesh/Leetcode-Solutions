class Solution:
    
            
    def search(self, nums: List[int], target: int) -> int:
        def solve(low,high,arr,k):
            if(low<=high):
                mid=low+((high-low)//2)
                if(k==arr[mid]):
                    return mid
                elif(k>arr[mid]):
                    return solve(mid+1,high,arr,k)
                else:
                    return solve(low,mid-1,arr,k)
                
            else:
                return -1
        return solve(0,len(nums)-1,nums,target)
