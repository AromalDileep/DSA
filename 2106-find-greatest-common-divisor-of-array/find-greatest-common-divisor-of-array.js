/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    smallest = nums[0]
    largest = nums[0]

    for (num of nums){
        if (num < smallest){
            smallest = num
        }
        else if (num > largest){
            largest = num
        }

    }

    while (largest){
        [smallest,largest] = [largest, smallest % largest]
    }

    return smallest
};