/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map();

    for (let i =0; i<nums.length; i++){
        const val = nums[i]
        const complement = target - val

        if (seen.has(complement)){
            return [seen.get(complement), i];
        }

        seen.set(val,i)
    }

};