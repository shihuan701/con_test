
class Forwork():
    def sumdigist(self,num):
        num = str(num)
        if num.isdigit():
            num = int(num)
            if num < 10 :
                return num
            else:
                return self.sumdigist(num%10 + self.sumdigist(num//10))
        else:
            print('你输入的不是数字')

    def twoSum(self, nums, target: int) :
        '''
        Python的字典数据类型是基于hash散列算法实现的，采用键值对(key:value)的形式，根据key的值计算value的地址，具有非常快的查取和插入速度。
        '''
        mapping = {}
        result = []
        for i in range(len(nums)):
            mapping[nums[i]] = i
        for j in range(len(nums)):
            diff = target - nums[j]
            if (diff in mapping and mapping[diff] != j):
                print('11111')
                result.append(j)
                result.append(mapping[diff])
                return result
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         mysum = nums[i] + nums[j]
        #         if mysum == target:
        #             return [i, j]

    def findMaxConsecutiveOnes(self, nums) -> int:
        result = 0
        count = 0
        if nums == None or len(nums) == 0:
            return result

        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0
        return result

    def moveZeroes(self, nums) -> None:
        # m = []
        # for i in nums:
        #     if i !=0:
        #         m.append(i)
        # for j in nums:
        #     if j == 0 :
        #         m.append(j)
        # return m
        index = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[index] = nums[i]
                index +=1
        for i in range(index,len(nums)):
            nums[i] = 0
        return nums

    def removeElement(self, nums, val) -> int:
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[index] = nums[i]
        #         index += 1
        # for i in range(index, len(nums)):
        #     nums.pop()
        # return len(nums)
        if nums == None or len(nums) == 0:
            return 0
        i=0
        j=len(nums)-1
        while i<j:
            while i<j and nums[i] !=val:
                print('i---',i)
                i+=1
            while i<j and nums[j] == val:
                print('j---', j)
                j = j-1
            nums[i],nums[j] = nums[j],nums[i]
        if nums[i] == val:
            return i
        else:
            return i+1

    def binarySearch(self,nums,target):
        '''
        二分搜索是一种在有序数组中查找某一特定元素的搜索算法
        1.首先需要对列表进行重排序
        2.找到列表中间的索引
        '''
        nums.sort()
        nums_len = len(nums)
        left,right=0,nums_len - 1
        if nums_len == 0 or nums == None:
            print('您要找的数字不在列表中')
            return -1
        while (left <= right):
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target :
                right = mid - 1
            else:
                left = mid +1
        print('您要找的数字不在列表中')
        return -1

    def search(self,nums,target):
        nums_len = len(nums)
        if nums_len == 0 or nums == None:
            print('您要找的数字不在列表中')
            return -1
        for i in range(0, nums_len):
            if nums[i] == target:
                return i
        return -1

    def insertionSort(self,nums):
        for i in range(1,len(nums)):
            key = nums[i]
            j = i -1
            while j >=0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

    def quick_sort(self,li, start, end):
        # 分治 一分为二
        # start=end ,证明要处理的数据只有一个
        # start>end ,证明右边没有数据
        if start >= end:
            return
        # 定义两个游标，分别指向0和末尾位置
        left = start
        right = end
        # 把0位置的数据，认为是中间值
        mid = li[left]
        while left < right:
            # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
            while left < right and li[right] >= mid:
                right -= 1
            li[left] = li[right]
            # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
            while left < right and li[left] < mid:
                left += 1
            li[right] = li[left]
        # while结束后，把mid放到中间位置，left=right
        li[left] = mid
        # 递归处理左边的数据
        self.quick_sort(li, start, left - 1)
        # 递归处理右边的数据
        self.quick_sort(li, left + 1, end)

    def bubble_sort(self, nums):
        l = len(nums)
        for i in range(l):
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]


    def partition(self,nums, low, high):
            i = low - 1
            pivot = nums[high]
            for j in range(low,high):
                if nums[j] <= pivot:
                    i = i +1
                    nums[i] , nums[j] = nums[j] , nums[i]
            nums[i+1],nums[high] = nums[high],nums[i+1]
            return (i+1)

if __name__ == '__main__':
    # num = input('please input a number:')
    # print(Forwork().sumdigist(num))
    # print(Forwork().twoSum(nums=[2, 7, 11, 15], target=9))
    # print(Forwork().removeElement(nums=[0,1,2,2,3,0,4,2],val = 2))
    # print(Forwork().binarySearch(nums=[2,7,9,10,11,13,14,15,20,21], target=8))
    # print(Forwork().search(nums=[2,7,9,10,11,13,14,15,20,21], target=13))
    # print(Forwork().insertionSort(nums=[13, 14, 15, 20, 2, 7, 9, 10, 11, 21]))
    nums = [10, 7, 8, 9, 1, 5]
    n = len(nums)
    Forwork().bubble_sort(nums)
    print("排序后的数组:",nums)