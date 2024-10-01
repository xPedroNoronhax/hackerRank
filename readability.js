function readability(sentence) {
  let letters = definingLetters(sentence);
  let sentences = definingSentence(sentence);
  let words = definingWord(sentence);

  let L = (letters / words) * 100;
  let S = (sentences / words) * 100;

  let index = 0.0588 * L - 0.296 * S - 15.8;

  index = Math.round(index);

  let output;
  if (index < 1) {
    output = "Before Grade 1";
  } else if (index >= 16) {
    output = "Grade 16+";
  } else {
    output = "Grade " + index;
  }

  return output;
}

function definingWord(sentence) {
  sentence = sentence.split(" ");
  for (let i = 0; i < sentence.length; i++) {
    // Usando regex para remover pontuações da palavra
    sentence[i] = sentence[i].replace(/[!?,.;:]/g, "");
  }
  return sentence.length;
}

function definingLetters(sentence) {
  // Dividindo a frase em caracteres
  sentence = sentence.split("");

  // Iterando por cada caractere
  for (let i = 0; i < sentence.length; i++) {
    // Usando regex para remover o que não for letra ou número
    sentence[i] = sentence[i].replace(/[^a-zA-Z0-9]/g, "");
  }

  // Retornando apenas letras e números
  sentence = sentence.filter((char) => char !== ""); // Remove os elementos vazios

  return sentence.length;
}

function definingSentence(text) {
  // Usando regex para encontrar todas as frases (separadas por '.', '!', '?')
  let sentences = text.match(/[^.!?]+[.!?]/g);

  // Retorna o número de frases
  return sentences ? sentences.length : 0;
}

console.log(
  readability(
    "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."
  )
);
