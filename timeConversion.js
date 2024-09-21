function timeConversion(s) {
    // Remover os ':' da string
    const newString = s.replace(/:/g, "");
    
    // Transformar em array de caracteres
    let arr = newString.split("");
    
    // Agrupar elementos em pares
    let groupedArr = [
      [arr[0], arr[1]], // Hora
      [arr[2], arr[3]], // Minuto
      [arr[4], arr[5]], // Segundo
      [arr[6], arr[7]], // Período (AM/PM)
    ];
  
    // Converter hora para número
    let hours = Number(groupedArr[0].join(""));
  
    // Obter o período (AM ou PM)
    let period = groupedArr[3].join("");
    
    let result;
  
    // Se for PM e a hora for menor que 12, adicionar 12 (ex: 07PM -> 19:00:00)
    if (period === "PM" && hours < 12) {
      hours += 12;
    }
    
    // Se for AM e a hora for 12, transformar em 00 (ex: 12AM -> 00:00:00)
    if (period === "AM" && hours === 12) {
      hours = 0;
    }
  
    // Formatando as horas com dois dígitos
    let formattedHours = hours.toString().padStart(2, "0");
  
    // Construir o resultado final no formato militar
    result = `${formattedHours}:${groupedArr[1].join("")}:${groupedArr[2].join("")}`;
    
    console.log(result);
  }
// converter um horario de AM/PM para horario militar
// se for 12:01:00 AM se transforma em 00:01:00
// se for 07:21:00PM se transforma em 19:21:00
// o que se transforma? a hora SE for PM e menorIgual a 12 e o periodo se for
// de qualquer jeito, nao vai ter o AM/PM na resposta
// transforma o s em um arr, dividido em [[0,1]:[2,3]:[4,5][6,7]]

console.log(timeConversion("12:21:00AM"));
