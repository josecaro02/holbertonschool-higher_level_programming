#!/usr/bin/node
if (process.argv[2] && process.argv[3]) {
  const numbers = process.argv.slice(2);
  for (let i = 0; i < numbers.length; i++) {
    numbers[i] = parseInt(numbers[i]);
  }
  numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
} else {
  console.log(0);
}
