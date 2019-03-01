function solution(s) {    
    let stack = [];
    
    s.split("").forEach(ch => {
        if (stack[stack.length-1] == ch) {
            stack.pop();
        }
        else {
            stack.push(ch);
        }
        //console.log(stack);
    });

    return stack.length == 0 ? 1 : 0;
}

console.log(solution("baabaa"));
console.log(solution("cdcd"));