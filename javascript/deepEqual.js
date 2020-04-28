const obj1 = {
    val1 : "value1",
    val2 : "value2",
    obj : {
        val3 : "value3",
        val4 : "value4",
    }
}

const obj2 = {
    val1 : "value1",
    val2 : "value2",
    obj : {
        val3 : "value3",
        val4 : "value4",
    }
}

function deepEqual(obj1, obj2) {
    const obj1Keys = Object.keys(obj1)
    const obj2Keys = Object.keys(obj2)
    let equal = false

    for (let i = 0; i < obj1Keys.length; i++) {
        if((typeof obj1[obj1Keys[i]] === "object") && (typeof obj2[obj1Keys[i]] === "object" )) {
            equal = deepEqual(obj1[obj1Keys[i]], obj2[obj1Keys[i]])
        }
        else if(obj1[obj1Keys[i]] === obj2[obj1Keys[i]]) {
            equal = true
        } else {
            equal = false
            break
        }
    }
    return equal
}

console.log(deepEqual(obj1, obj2));
