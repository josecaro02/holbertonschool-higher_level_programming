#!/usr/bin/node
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}
if (parseInt(process.argv[2])) {
  const result = factorial(parseInt(process.argv[2]));
  console.log(result);
} else {
  console.log(1);
}
