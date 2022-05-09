const bro = () => {
  const el = document.createElement('h3');
  el.innerHTML = 'Call from imported module';
  return el;
};

export { bro };
