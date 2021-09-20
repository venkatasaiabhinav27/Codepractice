class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        arr1 = 0
        arr2 = 0
        temp1 = 0
        temp2 = 0
        m = (l1+l2)//2
        for i in range(1,m+2):
            if(len(nums1) > arr1 and len(nums2) > arr2):
                if(nums1[arr1]<nums2[arr2]):
                    temp1 = temp2
                    temp2 = nums1[arr1]
                    arr1+=1
                else:
                    temp1 = temp2
                    temp2 = nums2[arr2]
                    arr2+=1
            elif(len(nums1) > arr1):
                temp1 = temp2
                temp2 = nums1[arr1]
                arr1+=1
            elif(len(nums2) > arr2):
                temp1 = temp2
                temp2 = nums2[arr2]
                arr2+=1
        if((l1+l2)%2!=0):
            return temp2
        else:
            return (temp1+temp2)/2