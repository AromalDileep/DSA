/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    let decrement = 10
    let aliceTurn = 1

    while (n >= decrement){
        n -= decrement
        decrement--
        aliceTurn ^= 1
    }

    return aliceTurn ? false : true
};