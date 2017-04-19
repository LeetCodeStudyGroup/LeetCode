import java.util.Vector;

public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] array = str.split(" ", -1);
        int size = array.length;
        
        if (pattern.length() != size)
            return false;
        
        for (int i=0; i<size; i++) {
            for (int j=i+1; j<size; j++) {
                if (array[i].equals(array[j])) {
                    if (pattern.charAt(i)-'a' != pattern.charAt(j)-'a')
                        return false;
                } else {
                    if (pattern.charAt(i)-'a' == pattern.charAt(j)-'a')
                        return false;
                }
            }
        }
        
        return true;
    }
}
