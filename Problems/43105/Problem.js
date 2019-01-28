function solution(triangle) {
    var answer = 0;
    
    answer = triangle.reduceRight((acc, cur) => {
        let arr = [];
        acc.reduce( (a, c) => {
            arr.push( Math.max(a, c) );
            return c;
        });
        //console.log(arr);
        var sumArr = arr.map( (num, idx) => num + cur[idx] );
        //console.log(sumArr);
        return sumArr;
    });
    
    return answer[0];
}

console.log(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));