function plusMinus(arr) {
  let pos = 0;
  let neg = 0;
  let neut = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      pos++;
    } else if (arr[i] < 0) {
      neg++;
    } else {
      neut++;
    }
  }

  let resPos = (pos / arr.length).toFixed(6);
  let resNeg = (neg / arr.length).toFixed(6);
  let resNeut = (neut / arr.length).toFixed(6);

  console.log(resPos);
  console.log(resNeg);
  console.log(resNeut);
}

console.log(plusMinus([-4, 3, -9, 0, 4, 1]));

//voce possui um array de numeros positivos e negativos
// conte quantos items tem no array
// crie tres variaveis, pos,neg,neut
// percorra o array
//  se o i for positivo, coloque o i em pos
//  se o i for negativo, coloque o i em neg
//  senao coloque o i em neut
// retorne tres respostas (pos/arr.length ; neg/arr.length ; neut/arr.length) todas com 6 casas decimais apos a virgula
