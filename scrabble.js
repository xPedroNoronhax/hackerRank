function scrabble(word1, word2) {
  const player1Score = score(word1);
  const player2Score = score(word2);

  if (player1Score > player2Score) {
    return "player 1 Wins!";
  } else if (player1Score < player2Score) {
    return "player 2 Wins";
  } else {
    return "Tie!";
  }
}

function score(word) {
  //faz o array de objetos "letra":ponto
  const lettersScores = [
    { letra: "A", pontos: 1 },
    { letra: "B", pontos: 3 },
    { letra: "C", pontos: 3 },
    { letra: "D", pontos: 2 },
    { letra: "E", pontos: 1 },
    { letra: "F", pontos: 4 },
    { letra: "G", pontos: 2 },
    { letra: "H", pontos: 4 },
    { letra: "I", pontos: 1 },
    { letra: "J", pontos: 8 },
    { letra: "K", pontos: 5 },
    { letra: "L", pontos: 1 },
    { letra: "M", pontos: 3 },
    { letra: "N", pontos: 1 },
    { letra: "O", pontos: 1 },
    { letra: "P", pontos: 3 },
    { letra: "Q", pontos: 10 },
    { letra: "R", pontos: 1 },
    { letra: "S", pontos: 1 },
    { letra: "T", pontos: 1 },
    { letra: "U", pontos: 1 },
    { letra: "V", pontos: 4 },
    { letra: "W", pontos: 4 },
    { letra: "X", pontos: 8 },
    { letra: "Y", pontos: 4 },
    { letra: "Z", pontos: 10 },
  ];
  word = word.toUpperCase();
  //cria a variavel que ira armazenar o total de pontos
  let total = 0;
  //com base na letra, verifica se na palavra há determinada letra e se tiver, credita a quantidade de pontos
  for (let i = 0; i < word.length; i++) {
    for (let j = 0; j < lettersScores.length; j++) {
      if (lettersScores[j].letra === word[i]) {
        total += lettersScores[j].pontos;
      }
    }
  }
  return total;
}


console.log(scrabble("computer","Science!"));