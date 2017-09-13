import java.util.Vector;

/*

Determine whether an integer is a palindrome. Do this without extra space.

*/

    public boolean isPalindrome(int x) {
        Vector<Integer> vector = new Vector<>();
        if (x < 0)
            return false;

        x = Math.abs(x);
        while (x > 0) {
            vector.add(x % 10);
            x = x / 10;
        }

        int vectorSize = vector.size();
        for (int i=0; i<vectorSize/2; i++) {
            if (vector.get(i) != vector.get(vectorSize-i-1))
                return false;
        }

        return true;
    }
