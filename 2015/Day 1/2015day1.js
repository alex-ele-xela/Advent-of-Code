const fs = require('fs');

// PART 1
fs.readFile('./santa.txt', (err, data) => {
    if (err) { console.log(err) }

    const directions = data.toString();

    // let floor = 0;
    // for (let char of directions) {
    //     if (char === '(') { floor += 1 }
    //     else if (char === ')') { floor -= 1 }
    // }
    // console.timeEnd('For Loop')

    const directionsArray = directions.split('')
    const answer = directionsArray.reduce((acc, currentValue) => {
        if (currentValue === '(') { return acc += 1 }
        else if (currentValue === ')') { return acc -= 1 }
    }, 0)
    console.log('Final Answer =', answer);
})


// PART 2
fs.readFile('./santa.txt', (err, data) => {
    if (err) { console.log(err) }

    const directions = data.toString();

    const directionsArray = directions.split('');
    let accumulator = 0;
    let counter = 0;
    const answer = directionsArray.some((currentValue) => {
        counter += 1;
        if (currentValue === '(') { accumulator += 1 }
        else if (currentValue === ')') { accumulator -= 1 }

        return accumulator < 0 ;
    })
    console.log('Basement entered at', counter)
})
