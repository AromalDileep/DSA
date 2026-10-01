/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];

    const closeToOpen = {
        "]": "[",
        "}": "{",
        ")": "("
    };

    for (const para of s){
        if (Object.hasOwn(closeToOpen, para)){
            if (stack.length == 0 || stack.pop() != closeToOpen[para]){
                return false
            }
        }else {
            stack.push(para)
            }
    }
    return stack.length === 0;
};