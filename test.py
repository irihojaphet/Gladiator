def main():
     twoSum([2,7,11,15],9 )
     twoSum([3,2,4],6 )
     twoSum([3,3],6 )

def twoSum(nums, target):
        
        indeces = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        continue
                    else:
                        indeces.append(i)
                        indeces.append(j)
                    return indeces

main()