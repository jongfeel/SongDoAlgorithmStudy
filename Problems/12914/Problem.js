function solution(n) {    
    let count = [1, 1, 2];
    
    for (let i=2; i<=n; i++) {
        count[i] = (count[i-1] + count[i-2]) % 1234567;
    }
    
    return count[n];
}

console.log(solution(4));