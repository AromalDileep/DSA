/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    let decrement = 10
    let aliceTurn = true

    while (n >= decrement){
        n -= decrement
        decrement--
        aliceTurn = !aliceTurn
    }

    return !aliceTurn 
};