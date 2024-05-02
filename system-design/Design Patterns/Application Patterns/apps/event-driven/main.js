class Event {
  constructor() {
    this.events = {};
  }

  // Register an event handler
  on(eventName, callback) {
    if (this.events[eventName]) {
      this.events[eventName].push(callback);
    } else {
      this.events[eventName] = [callback];
    }
  }

  // Trigger all callbacks associated with a given eventName
  trigger(eventName) {
    if (this.events[eventName]) {
      for (let cb of this.events[eventName]) {
        cb();
      }
    }
  }

  // Remove all event handlers associated with the given eventName
  off(eventName) {
    delete this.events[eventName];
  }
}

// Testing

const test = require('node:test');
const assert = require('node:assert');

test('Events can be registered then triggered', () => {
  const events = new Event();

  const myFn = test.mock.fn(() => null);

  events.on('click', myFn);
  events.trigger('click');

  assert.strictEqual(myFn.mock.calls.length, 1);

});

test('Multiple events can be registered then triggered', () => {
  const events = new Event();

  const myFn1 = test.mock.fn(() => null);
  const myFn2 = test.mock.fn(() => null);

  events.on('click', myFn1);
  events.on('click', myFn2);
  events.trigger('click');

  assert.strictEqual(myFn1.mock.calls.length, 1);
  assert.strictEqual(myFn2.mock.calls.length, 1);

});

test('Events can be triggered multiple times', () => {
  const events = new Event();

  const myFn1 = test.mock.fn(() => null);
  const myFn2 = test.mock.fn(() => null);

  events.on('click', myFn1);
  events.trigger('click');
  events.on('click', myFn2);
  events.trigger('click');
  events.trigger('click');

  assert.strictEqual(myFn1.mock.calls.length, 3);
  assert.strictEqual(myFn2.mock.calls.length, 2);
});

test('Events can have different names', () => {
  const events = new Event();

  const myFn1 = test.mock.fn(() => null);
  const myFn2 = test.mock.fn(() => null);

  events.on('click', myFn1);
  events.trigger('click');
  events.on('hover', myFn2);
  events.trigger('click');
  events.trigger('hover');

  assert.strictEqual(myFn1.mock.calls.length, 2);
  assert.strictEqual(myFn2.mock.calls.length, 1);
});

test('Events can be toggled off', () => {
  const events = new Event();

  const myFn1 = test.mock.fn(() => null);
  const myFn2 = test.mock.fn(() => null);

  events.on('hover', myFn2);

  events.on('click', myFn1);
  events.trigger('click');
  events.off('click');
  events.trigger('click');

  events.trigger('hover');

  assert.strictEqual(myFn1.mock.calls.length, 1);
  assert.strictEqual(myFn2.mock.calls.length, 1);
});
