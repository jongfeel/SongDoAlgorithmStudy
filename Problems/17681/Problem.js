function solution(n, arr1, arr2) {
    var answer = [];
    
    [...Array(n).keys()].map(i => arr1[i] | arr2[i]).forEach(bitwiseOR => {
        let mappingResult = bitwiseOR.toString(2).split('').map(bit => bit == 1 ? "#" : " ");
        [...Array(n - mappingResult.length).keys()].forEach(j => mappingResult.unshift(" "));
        answer.push(mappingResult.join(""));
    });
    
    return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]));