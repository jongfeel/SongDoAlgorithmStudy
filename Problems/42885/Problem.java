import java.util.Deque;
import java.util.Arrays;
import java.util.ArrayDeque;

class Problem {
    public long solution(int[] people, int limit) {
        int answer = 0;
        
        Deque<Integer> deque = new ArrayDeque<>(people.length);
        Arrays.stream(people).sorted().forEach(person -> deque.offer(person));
        
        while (deque.size() != 0) {
            if (deque.peekLast() + deque.peekFirst() <= limit) {
                deque.pollFirst();
                deque.pollLast();
            } else {
                deque.pollLast();
            }
            answer++;
        }
        
        return answer;
    }

    public static void main(String[] args) {
        System.out.println( new Problem().solution(new int[] { 70, 50, 80, 50 }, 100) );
        System.out.println( new Problem().solution(new int[] { 70, 50, 80 }, 100) );
    }
}