class Solution {
public:
    int longestValidParentheses(string s) {
        int count = 0;
        stack<int> save;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                save.push(i);
            }
            if (s[i] == ')') {
                if (!save.empty() && s[save.top()] == '(') {
                    save.pop();
                    count += 2;
                } else {
                    save.push(i);
                }
            }
        }
        
        if (save.empty())
            return count;
        
        int last = s.length() - 1;
        count = 0;
        while (!save.empty()) {
            int tmp = last - save.top();
            last = save.top();
            save.pop();
            if (count < tmp)
                count = tmp - tmp%2;
        }
        
        if (last > count)
            count = last;
        
        return count;
    }
};
