/*
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

var map = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000,
    }
*/

    public String intToRoman(int num) {
        int[] values = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] strs = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        String sum = "";


        if (num < 1 || num > 3999)
            return sum;

        for (int i=0; i<values.length; i++) {
            int count = num / values[i];
            if (count > 0) {
                for (; count>0; count--)
                    sum += strs[i];

                num = num % values[i];
            }
        }

        return sum;
    }
