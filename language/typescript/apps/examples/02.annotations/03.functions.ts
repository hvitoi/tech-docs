// Inferred return value
const add = (a: number, b: number) => {
  return a + b;
};

// number
const subtract = (a: number, b: number): number => {
  return a - b;
};

// void
const logger = (message: string): void => {
  console.log(message);
};

// throw -> never
// 100% never reaches the end of the function! Never execute the function completely
const throwError = (message: string): never => {
  throw new Error(message);
};

// throw + string
// Return string even though it can return error
const showMessage = (message: string): string => {
  if (!message) throw new Error(message);
  return message;
};

// throw + void
// Return void even though it can return error
const checkError = (message: string): void => {
  if (!message) throw new Error(message);
};

// Destructuring with annotations
const todaysWeather = {
  date: new Date(),
  weather: 'sunny'
};
const logWeather = ({
  date,
  weather
}: {
  date: Date;
  weather: string;
}): void => {
  console.log(date);
  console.log(weather);
};
logWeather(todaysWeather);
