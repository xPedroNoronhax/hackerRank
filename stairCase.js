function staircase(n) {
  for (let i = 0; i < n; i++) {
    let line = "";
    for (let j = 1; j < n - i; j++) {
      line += " ";
    }

    for (let k = 0; k <= i; k++) {
      line += "#";
    }
    console.log(line);
  }
}

staircase(5);
