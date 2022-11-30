#!/usr/bin/node
const arg = process.argv[2];
const number = Number.parseInt(arg);
if (number) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
