/*
    Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

    You may assume the integer do not contain any leading zero, except the number 0 itself.

    The digits are stored such that the most significant digit is at the head of the list.
     */

    public int[] plusOne(int[] digits) {
        int sum;
        sum = digits[digits.length-1] + 1;
        digits[digits.length-1] = sum % 10;
        int carry = sum / 10;
        for (int i=digits.length-2; i>=0; i--) {
            sum = digits[i] + carry;
            digits[i] = sum % 10;
            carry = sum / 10;
        }

        if (carry > 0) {
            int size = digits.length + 1;
            int[] results = new int[size];
            results[0] = carry;
            for (int i=0; i<digits.length; i++) {
                results[i+1] = digits[i];
            }

            return results;
        }

        return digits;
    }
