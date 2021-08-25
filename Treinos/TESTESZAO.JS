'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'findSmallestDivisor' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. STRING t
 */

function findSmallestDivisor(s, t) {
if (s.length % t.length === 0 && s.includes(t)){
    if(t.length %new set(t).size===0) return new set(t).size
    if (s === t) return t.length
    if (t.length * 2 === s.length && t.length / (s.length / t.length) % 1 !== 0)
 rturn t.length
 else return t.length / (s.length / t.length)
}
return -1
}
    

}

function main() {