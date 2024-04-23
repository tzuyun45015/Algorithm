# leetcode#215 kth largest element in an array
# MaxHeap O(n) + klogn
# Worst O(n2) nums.sort()
        #return nums[len(nums)-k]
# AVE QuickSelect O(n)
# set a pivot


def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                        # smaller than pivot swap to right index
                    nums[i], nums[p] = nums[p], nums[i] #in place partition
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]

            if p > k: return quickSelect(l, p-1)
            elif p < k: return quickSelect(p+1, r)
            else: return nums[p]
        return quickSelect(0,len(nums)-1)

## maxHeap
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)

        return nums[0]

