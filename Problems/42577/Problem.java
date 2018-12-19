class Problem {
    public static boolean solution(String[] phone_book) {
        boolean answer = true;
        
        for (int i=0; i<phone_book.length; i++) {
            String prefix = phone_book[i];
            for (int j=0; j<phone_book.length; j++) {
                if (i == j) {
                    continue;
                }
                 
                if (phone_book[j].startsWith(prefix)) {
                    return false;
                }
            }   
        }
        
        return answer;
    }

    public static void main(String[] args) {
        System.out.println( Problem.solution(new String[] {"119", "97674223", "1195524421"}) );
    }
}