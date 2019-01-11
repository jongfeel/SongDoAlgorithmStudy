class Problem {
    public static int solution(int n) {
        int answer = 0;
        int isNotPrimes[] = new int[1000000];

        for (int index = 2; index <= Math.sqrt(n); index++) {
            if (isNotPrimes[index] == 0) {
                for (int innerIndex = index * 2; innerIndex <= n; innerIndex += index) {
                    isNotPrimes[innerIndex] = 1;
                }
            }
        }

        for (int i=2; i<=n; i++) {
            if (isNotPrimes[i] == 0) {
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        System.out.println( Problem.solution(10) );
    }
}