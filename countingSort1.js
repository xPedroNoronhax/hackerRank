function countingSort(arr) {
  // Write your code here
  let maxValue = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > maxValue) {
      maxValue = arr[i];
    }
  }

  let counterArr = [];
  for (let i = 0; i <= maxValue; i++) {
    counterArr[i] = 0;
  }

  for (let i = 0; i < arr.length; i++) {
    counterArr[arr[i]]++;
  }

  return counterArr;
}

// voce recebe um arr de numeros inteiros
// voce faz o sorte e deixa eles em ordem
// voce cria um outro array, composto de varios "0", baseado na quantidade de elementos que o arr principal possui, deve contar de 0 ate arr.length
//

console.log(countingSort([1, 1, 3, 2, 1]));
