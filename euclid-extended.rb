#!/usr/bin/env ruby

# Extended Euclidean Algorithm
# Written by Benjamin Mestdagh
#
# Usage: ./euclid-extended.rb a b
# a and b being integer values.

begin
    a = Integer(ARGV[0])
    b = Integer(ARGV[1])

    x0 = xn = 1
    y0 = yn = 0
    x1 = 0
    y1 = 1
    r = a.modulo(b)

    while r > 0
        q = a/b
        xn = x0 - q*x1
        yn = y0 - q*y1

        x0 = x1
        y0 = y1
        x1 = xn
        y1 = yn
        a = b
        b = r
        r = a.modulo(b)
    end

    puts "d = " + b.to_s()
    puts "x = " + xn.to_s()
    puts "y = " + yn.to_s()

rescue
    puts "Usage: ./euclid-extended.rb number1 number2"
    puts "Make sure you enter your numbers as integers."

end
