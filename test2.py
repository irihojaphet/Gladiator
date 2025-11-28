def main():
    print(intersection([1,2,2,1],[2,2]))
def intersection(nums1, nums2):
    nums = []
    test = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if i != j:
                if nums1[i] == nums2[j]:
                    test.append(nums1[i])
                    
    for k in test:
        if k not in nums:
            nums.append(k)
    return nums

main()

