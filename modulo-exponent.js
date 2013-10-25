function calculate(y,a,q) {
    var x = 0;
    while (true) {
        var result = Math.pow(a, x) % q;
        if((x%1000000) === 0) console.log("x is: "+ x);
        if (y === result) {
            return "het getal is: " + x;
        } else {
            x++;
        }
    }
}
