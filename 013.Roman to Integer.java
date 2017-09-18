/*
Given a roman numeral, convert it to an integer.

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

    public int romanToInt(String s) {
        int sum = 0;
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        for (int i=0; i<s.length(); i++) {
            if (i+1 < s.length() && map.get(s.charAt(i)) < map.get(s.charAt(i+1)))
                sum -= map.get(s.charAt(i));
            else
                sum += map.get(s.charAt(i));
        }

        return sum;
    }
