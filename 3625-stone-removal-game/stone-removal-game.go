func canAliceWin(n int) bool {
    
    decrement := 10
    aliceTurn := true

    for n >= decrement{
        n -= decrement
        decrement--
        aliceTurn = !aliceTurn
    }

    return !aliceTurn
}