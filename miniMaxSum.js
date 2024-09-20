function miniMaxSum(arr) {
  // Write your code here
  let orderedArray = arr.sort((a, b) => a - b);
  let totalSum = orderedArray.reduce((acc, curr) => acc + curr, 0);
  let maxSum = totalSum - orderedArray[0];
  let minSum = totalSum - orderedArray[(orderedArray.length - 1)];

  console.log(minSum, maxSum);
}

//voce recebe um array de numeros inteiros
// colocar eles em ordem
// precisa realizar a soma de todos eles
// retornar a somaMax = somaTotal - arr[0]
// retornar a somaMin = somaTotal - arr[arr.length-1]


