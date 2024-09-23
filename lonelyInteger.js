function lonelyinteger(a) {
  // Write your code here
  let count = {}

  for (let num of a) {
    if (count[num]) {
      count[num]++;
    } else {
      count[num] = 1;
    }
  }


  for (let num in count) {
    if (count[num] === 1) {
      return parseInt(num);
    }
  }
}

//voce vai ter um array de numeros inteiros
//deve retornar o numero que se tem apenas uma vez, os outros se repetem.

console.log(lonelyinteger([1, 2, 3, 4, 3, 2, 1]));
