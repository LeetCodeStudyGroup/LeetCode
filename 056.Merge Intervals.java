/*
    Given a collection of intervals, merge all overlapping intervals.

    For example,
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].
     */

//     Definition for an interval.
     public class Interval {
         int start;
         int end;

         Interval() {
             start = 0;
             end = 0;
         }

         Interval(int s, int e) {
             start = s;
             end = e;
         }
     }

    public List<Interval> merge(List<Interval> intervals) {
        if (intervals.size() <= 1)
            return intervals;
        for (int i=0; i<intervals.size(); i++) {
            for (int j=i+1; j<intervals.size(); j++)
                if ((intervals.get(i).end >= intervals.get(j).start && intervals.get(i).start <= intervals.get(j).start)
                    || (intervals.get(j).end >= intervals.get(i).start && intervals.get(j).start <= intervals.get(i).start)) {
                    intervals.get(i).start = Math.min(intervals.get(i).start, intervals.get(j).start);
                    intervals.get(i).end = Math.max(intervals.get(i).end, intervals.get(j).end);
                    intervals.remove(j);
                    i--; break;
                }
        }

        return intervals;
    }
