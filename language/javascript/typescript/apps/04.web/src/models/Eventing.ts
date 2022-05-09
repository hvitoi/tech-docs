type Callback = () => void;

export class Eventing {
  events: { [key: string]: Callback[] } = {};
  // events = { 'click': [cb1, cb2], 'hover': [cb1, cb2, cb3] }

  on = (eventName: string, callback: Callback): void => {
    const handlers = this.events[eventName] || [];
    handlers.push(callback);
    this.events[eventName] = handlers;
  };

  trigger = (eventName: string): void => {
    const handlers = this.events[eventName] || [];
    for (let callback of handlers) callback();
  };
}
