#! /usr/bin/env ruby

############################
# The Simple AES Algorithm #
#                          #
#   by Benjamin Mestdagh   #
#                          #
############################

# Some matrices we need #

$sbox = [ [0x9, 0x4, 0xA, 0xB],
          [0xD, 0x1, 0x8, 0x5],
          [0x6, 0x2, 0x0, 0x3],
          [0xC, 0xE, 0xF, 0x7] ]

$multiplyByFour = [0x0, 0x4, 0x8, 0xC,
                   0x3, 0x7, 0xB, 0xF,
                   0x6, 0x2, 0xE, 0xA,
                   0x5, 0x1, 0xD, 0x9 ]


# The functions we need #

def putInMatrix(number, matrix)
    nibbles = ((Math.log(number)/Math.log(2)).ceil() / 4.0).ceil()
    shift = (nibbles * 4) - 4

    for i in 1..nibbles
        if i.modulo(2) == 0 then row = 1 else row = 0 end
        if i < 3 then col = 0 else col = 1 end

        matrix[row][col] = (number >> shift) & 0xF
        shift -= 4
    end
end

def printMatrix(matrix)
    for col in 0...matrix.length
        for row in 0...matrix[col].length
            result = matrix[row][col]
            puts "S%d,%d = %x - %04b" % [row, col, result, result]
        end
    end
end

def numberFromMatrix(matrix)
    result = 0
    for col in 0...matrix[0].length
        for row in 0...matrix.length
            result = result << 4
            result += matrix[row][col]
        end
    end

    return result
end

def rotateNibbles(number)
    newLeftPart = number & 0xF
    number = number >> 4
    newLeftPart = newLeftPart << 4
    number += newLeftPart
    return number
end

def addKey(matrix, key)
    for i in 0...matrix.length
        for j in 0...matrix[i].length
            matrix[i][j] = matrix[i][j] ^ key[i][j]
        end
    end
end

def shiftRow(matrix)
    matrix[1][0] = matrix[1][0] ^ matrix[1][1]
    matrix[1][1] = matrix[1][0] ^ matrix[1][1]
    matrix[1][0] = matrix[1][0] ^ matrix[1][1]
end

def substituteNibbles(matrix)
    for i in 0...matrix.length
        for j in 0...matrix[i].length
            sboxRow = (matrix[i][j] >> 2) & 0b11
            sboxCol = matrix[i][j] & 0b11
            matrix[i][j] = $sbox[sboxRow][sboxCol]
        end
    end
end

def mixColumns(matrix)
    tempState =  Array.new(2) { Array.new(2) }
    for col in 0...matrix.length
        for row in 0...matrix[col].length
            otherRow = (row + 1) % matrix.length
            tempState[row][col] = matrix[row][col] ^ ($multiplyByFour[matrix[otherRow][col]])
        end
    end
    cloneMatrix(matrix, tempState)
end

def cloneMatrix(matrix1, matrix2)
    for col in 0...matrix1.length
        for row in 0...matrix1.length
            matrix1[row][col] = matrix2[row][col]
        end
    end
end

def getNextKeys(key)
    rcon1 = 0b10000000
    rcon2 = 0b00110000
    w0    = (key & 0xFF00) >> 8
    w1    = key & 0xFF

    w1rot = rotateNibbles(w1)
    wArr  = [[(w1rot & 0xF0) >> 4],[w1rot & 0xF]]
    substituteNibbles(wArr)
    w2    = w0 ^ rcon1 ^ numberFromMatrix(wArr)
    w3    = w2 ^ w1

    w3rot = rotateNibbles(w3)
    wArr  = [[(w3rot & 0xF0) >> 4],[w3rot & 0xF]]
    substituteNibbles(wArr)
    w4    = w2 ^ rcon2 ^ numberFromMatrix(wArr)
    w5    = w4 ^ w3
    key1  = (w2 << 8) + w3
    key2  = (w4 << 8) + w5
    return [key1, key2]
end 


### Main starting point ###

message = 0b0110111101101011
key     = 0b1010011100111011 

puts "S-AES Algorithm"
puts "---------------\n"

puts "Message:\n\t%016b\n\t%04x" % [message, message]
puts "Key:\n\t%016b\n\t%04x" % [key, key]

state = Array.new(2) { Array.new(2) }
putInMatrix(message, state)

keyMatrix = Array.new(2) { Array.new(2) }
putInMatrix(key, keyMatrix)

addKey(state, keyMatrix)
substituteNibbles(state)
shiftRow(state)
mixColumns(state)

nextKeys = getNextKeys(key)
putInMatrix(nextKeys[0], keyMatrix)
addKey(state, keyMatrix)
substituteNibbles(state)
shiftRow(state)

putInMatrix(nextKeys[1], keyMatrix)
addKey(state, keyMatrix)

result = numberFromMatrix(state)
puts "Result:\n\t%016b\n\t%04x" % [result, result]
