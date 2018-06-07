class Solution {
    public int numJewelsInStones(String J, String S) {
        char[] jewel = J.toCharArray();
        char[] stones = S.toCharArray();
        boolean[] jewelMask = new boolean[256];
        int result = 0;

        for (int i = 0; i < jewel.length; i++) {
            jewelMask[jewel[i]] = true;
        }

        for (int i = 0; i < stones.length; i++) {
            if (jewelMask[stones[i]]) {
                result++;
            }
        }
        return result;
    }
}
