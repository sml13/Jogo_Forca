function consecutive(num) {
    let count = 0;
    for (let L = 1; L * (L + 1) < 2 * num; L++) {
        let a = ((1.0 * mum - (L * (L + 1)) / 2) / (L + 1));

        if (a - parseInt(a, 10) == 0.0)
            count++;
    }

    return count;
}

console.log(num)