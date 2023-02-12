for (let i = 1; i <= 10; i++) {
  for (let j = 4; j <= 40; j + 4) {
    console.log(k + "x" + i + "="(j * i));
  }
  console.log("\n");
}

let data = [];
for (let i = 1; i <= 10; i++) {
  let row = [];
  for (let j = 4; j <= 40; j += 4) {
    row.push(j * i);
  }
  data.push(row);
}
console.table(data);
