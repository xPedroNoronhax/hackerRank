function migratoryBirds(arr) {
  // Write your code here
  arr.sort((a, b) => a - b);
  let types = [];
  // crie um chave e valor baseado no arr
  for (let i = 0; i < arr[arr.length - 1]; i++) {
    types.push({ id: i + 1, value: 0 });
  }
  // percorra todo types e adicione valores ao value.
  for (let i = 0; i < types.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] == types[i].id) {
        types[i].value++;
      }
    }
  }

  //percorrer o arr types, identificar qual possui o maior value
  let popular = types[0];

  for (let i = 1; i < types.length; i++) {
    if (types[i].value > popular.value) {
      popular = types[i];
    }
  }
  console.log(popular.id);
}

/*
voce vai receber um array de numeros inteiros
[1,4,4,4,5,3]
nesse caso há 3 tipos de passaros
id 1 - 1
id 2 - 0
id 3 - 1
id 4 - 3
id 5 -1

vai ser necessário, trabalhar com objetos.
entao primeiro, fazemos um loop for, para percorrer do menor id até o maior, para gerar um array de objetos assim:
let types = [
"1":1
"2":0
"3":1

"4":3
"5":1
]

primeiro criamos a o array types, depois colocamos as chaves
*/

console.log(migratoryBirds([1, 4, 4, 4, 5, 3]));
