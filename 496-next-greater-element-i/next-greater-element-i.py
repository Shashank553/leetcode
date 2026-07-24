class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # This stack will store elements from nums2
        # We keep it decreasing so that the top element
        # is always the next greater element candidate
        stack=[]


        # This dictionary stores:
        # number -> its next greater element
        # Example: 1 -> 3
        next_greater={}


        # We go from right to left because we need
        # elements that are to the RIGHT of current element
        for num in reversed(nums2):

            # Remove all smaller or equal elements
            # because they cannot be the answer for current num
            while stack and stack[-1]<=num:
                stack.pop()


            # If stack is not empty, the top element is
            # the first greater element on the right
            if stack:
                next_greater[num]=stack[-1]

            else:
                #No greater element exists
                next_greater[num]=-1

                 # Add current number so it can be a greater element
            # for future numbers on the left
            stack.append(num)
            
    #now nums1 only needs lookup from our dictionary
        answer=[]

        for num in nums1:
            answer.append(next_greater[num])

        return answer











        