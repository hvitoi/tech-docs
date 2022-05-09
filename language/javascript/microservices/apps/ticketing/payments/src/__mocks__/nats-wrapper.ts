const natsWrapper = {
  client: {
    // Mock function
    publish: jest.fn().mockImplementation(
      // This here is actual publish function that will be implemented
      (subject: string, data: string, callback: () => void) => {
        callback();
      }
    )
  }
};

export { natsWrapper };
