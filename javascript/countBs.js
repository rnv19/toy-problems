const str = "BsunBdeepB"
let count = 0

function countBs(str) {
    for (let i = 0; i < str.length; i++) {
        if (str[i] === "B") {
            count++
        }
    }
    return count
}

console.log(countBs(str));

count = 0
function countChar(str, char) {
    for (let i = 0; i < str.length; i++) {
        if (str[i] === char) {
            count++
        }
    }
    return count
}

console.log(countChar(str, "e"));
