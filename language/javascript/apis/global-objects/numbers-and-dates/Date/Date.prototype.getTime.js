var birthday = new Date(1994, 12, 17); // 11 -> december. 12 -> january

console.log(birthday); // 1995-01-17T02:00:00.000Z
console.log(birthday.getTime()); // 790308000000 -> milliseconds passed since linux epoch (1970)
console.log(birthday.valueOf()); // same result

console.log(birthday.getTime() / 1000 / 60 / 60 / 24 / 365); //  time since linux epoch in years
