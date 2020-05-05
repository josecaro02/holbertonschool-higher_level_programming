#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.length === 3) {
  console.log('Argument Found');
} else if (myArgs.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
