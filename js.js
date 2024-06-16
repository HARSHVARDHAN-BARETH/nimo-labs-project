let sum = 0;

 function calc(n) {
    for (let i = 0; i < n; i++) {
        sum += i;
    }
    return sum;
}

const memorize = (fun)=>{
    let cache = {};
    return function(...args){
        let n = args[0];
        if(n in cache)
            {
                console.log("cache...");
                return cache[n];
            }else
            {
                console.log("Calculating first time...");
                let result = fun(n);
                cache[n] = result;
                return result;
            }
    }
}

console.time();
const efficent = memorize(calc);
console.log(efficent(5));
console.timeEnd();

