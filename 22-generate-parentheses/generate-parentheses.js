/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    res = [];

    const backtrack = (s, openCount, closeCount) =>{
        if (s.length === n * 2){
            res.push(s)
            return 
        }

        if (openCount < n){
            backtrack(s+"(", openCount+1, closeCount); 
        }
        if (closeCount < openCount){
            backtrack(s+")", openCount, closeCount+1);
        }
    }
    backtrack("", 0, 0)
    return res
};