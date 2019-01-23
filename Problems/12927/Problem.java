import java.util.PriorityQueue;
import java.util.Collections;
import java.util.Arrays;
import java.util.stream.IntStream;

class Problem {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(works.length, Collections.reverseOrder());
        Arrays.stream(works).forEach(work -> pq.offer(work));
        
        IntStream.range(0, n).forEach(hour -> pq.offer(pq.peek() == 0 ? 0 : pq.poll() - 1));
        //pq.stream().forEach(System.out::println);
        
        answer = (long)pq.stream().filter(work -> work != 0).mapToDouble(work -> Math.pow(work.intValue(), 2)).sum();
        
        return answer;
    }

    public static void main(String[] args) {
        System.out.println( new Problem().solution(4, new int[] { 4,3,3 }) );
        System.out.println( new Problem().solution(1, new int[] { 2,1,2 }) );
        System.out.println( new Problem().solution(3, new int[] { 1,1 }) );
    }
}