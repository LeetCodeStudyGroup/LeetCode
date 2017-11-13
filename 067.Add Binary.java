/*
    Given two binary strings, return their sum (also a binary string).

    For example,
    a = "11"
    b = "1"
    Return "100".
     */

    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int aLength = a.length() - 1;
        int bLength = b.length() - 1;
        int carry = 0;
        while (aLength >= 0 || bLength >= 0) {
            int sum = carry;
            if (aLength >= 0)
                sum += a.charAt(aLength--) - '0';
            if (bLength >= 0)
                sum += b.charAt(bLength--) - '0';
            carry = sum / 2;
            sb.append(sum % 2);
        }
        if (carry != 0)
            sb.append(carry);
        return sb.reverse().toString();
    }
