/*
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.


 */

    public int reverse(int x) {
        long result = 0;

        while (x != 0) {
            result = result*10 + x % 10;
            x /= 10;

            if( result > Integer.MAX_VALUE || result < Integer.MIN_VALUE)
                return 0;
        }

        return (int) result;
    }
