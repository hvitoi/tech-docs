import { bro } from './bro';

const textComponent = () => {
  const el = document.createElement('h2');
  el.innerHTML = 'Call from JS';
  return el;
};

document.body.appendChild(textComponent());
document.body.appendChild(bro());
