function diagonalDifference(arr) {
  // Write your code here

  let ltr = 0;
  let rtl = 0;

  for (let i = 0; i < arr.length; i++) {
    ltr += arr[i][i];
    rtl += arr[i][arr.length - 1 - i];
  }

  return Math.abs(ltr - rtl);
}

console.log(
  diagonalDifference([
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
  ])
);

//voce sempre recebera uma matriz quadrada
//pode ser 2,3,4,5...por linha.
/*
[
[1238]
[4565]
[7897]
[5647]
]
*/
//temos que somar sempre as diagonais
