function catAndMouse(x, y, z) {
    while (x !== z && y !== z) {
      if (x > z) {
        x--;
      } else if (x < z) {
        x++;
      }
  
      if (y > z) {
        y--;
      } else if (y < z) {
        y++;
      }
    }
  
    if (x === z && y === z) {
      console.log("Mouse C");
    } else if (x === z) {
      console.log("Cat A");
    } else if (y === z) {
      console.log("Cat B");
    }
  }
  
  catAndMouse(1, 2, 3);
  
/*
fazer um programa para ver qual gato irá chegar no rato primeiro.
se os dois chegarem juntos é empate, imprime "Mouse C"
se o x chegar primeiro, imprime "Mouse A"
se o x=y chegar primeiro, imprime "Mouse B"
os gatos andam iguais, o rato nao se move.
a cada loop eles ganham uma casa em direção ao rato.
exemplo:
se o rato uma linha de 6 etapas
o gato A esta na posição 2
o gato B esta na posição 4
e o rato na posição 3
nesse caso o rato fugiria. 
mas o important é que o GA aumentaria 1 para chegar de 2 p 3
e o GB diminuiria 1.
*/
