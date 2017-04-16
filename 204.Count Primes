/*
*         First LeeCode Practice 
*         2017/04/16
*         C#
*/

public class Solution {
    
        public int CountPrimes(int n)
        {
            List<int> nonPrimeList = new List<int>();
            bool[] primtable = new bool[n];

            for (int i = 0; i < n; ++i) 
            {
                primtable[i] = false;
            }

            int CountResult = 0;
            
            for (int p = 2; p < n; ++p )
            {
                if (primtable[p])
                    continue;

                CountResult++;

                int num = n / p;
                for (int i = 2; i <= num; ++i)
                {
                    int inp = i * p;
                    
                    if (inp == n) break;

                    primtable[inp] = true;
                }
            }
            return CountResult;
        }
}
