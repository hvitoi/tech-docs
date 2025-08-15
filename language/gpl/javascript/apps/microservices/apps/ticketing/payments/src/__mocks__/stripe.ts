const stripe = {
  charges: {
    // Callback that resolves with an empty object
    // It's necessary to be used on functions that use AWAIT
    create: jest.fn().mockResolvedValue({
      id: 'abcd' // Provide any ID for testing purposes
    })
  }
};

export { stripe };
