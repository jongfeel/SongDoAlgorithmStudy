function solution(n, arr1, arr2) {
    var answer = [];
    let bitwiseOR = [];
    
    for (let i=0; i<n; i++) {
        bitwiseOR[i] = arr1[i] | arr2[i];
        let mappingResult = bitwiseOR[i].toString(2).split('').map(bit => bit == 1 ? "#" : " ");
        //console.log(mappingResult);
        // space fill left
        // ex) n == 6, mappingResult.length == 2 ("##")
        // space fill left 4 and make length 6 ("    ##")
        for (let j=mappingResult.length; j<n; j++) {
            mappingResult.unshift(" ");
        }
        answer[i] = mappingResult.join("");
    }
    
    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]));