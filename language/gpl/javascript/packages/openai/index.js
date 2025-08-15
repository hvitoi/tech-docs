import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: "yourkey",
});
const openai = new OpenAIApi(configuration);

const completion = await openai.createCompletion("text-davinci-001", {
  prompt: "O que é Indústria 4.0",
  max_tokens: 200,
});

console.log(completion.data.choices[0].text);
