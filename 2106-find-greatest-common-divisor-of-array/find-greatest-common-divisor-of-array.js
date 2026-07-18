/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    const smallest = Math.min(...nums)
    const largest = Math.max(...nums)

    return gcd(smallest, largest)
};

function gcd(a,b){
    while (b){
        [a,b] = [b, a%b]
    }
    return a
}