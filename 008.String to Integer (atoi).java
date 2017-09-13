package com.square;

import java.util.HashMap;

import static java.lang.Math.max;

/**
 * Created by cynthia.pan on 2017/8/24.
 */

public class Solution {
/*
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

 */

    public int myAtoi(String str) {
        int sign = 1;
        int index = 0;
        int result = 0;

        if (str.length() == 0) return 0;

        while (str.charAt(index) == ' ' && index < str.length())
            index++;

        if (index < str.length() && str.charAt(index) == '+') {
            index++;
        } else if (index < str.length() && str.charAt(index) == '-') {
            sign = -1;
            index++;
        }

        while(index < str.length()) {
            int digit = str.charAt(index) - '0';
            if (digit < 0 || digit > 9) break;

            if (result > Integer.MAX_VALUE/10 || (result == Integer.MAX_VALUE/10 && digit > Integer.MAX_VALUE%10))
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            result = result * 10 + digit;
            index++;
        }

        return result * sign;
    }
}
