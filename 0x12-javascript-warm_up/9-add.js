#!/usr/bin/node

function add (a, b) {
  /**
   * Prints the addition of two integers
   * Args:
   *  a(integer): the first argument is the first integer
   *  a(integer): the first argument is the first integer
   */
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);
  const result = a + b;
  console.log(result);
}

add(10, 30);
