# Deep Learning

- It's a class of Machine Learning models that uses the same training algorithm technique to learn from data: `backpropagation`
- Requires large amount of input data
- Requires GPUs/NPUs for processing
- Use cases
  - Computer vision
  - Natural Language Processing (NLP)

## Tensors

- The whole input is transformed into a `multidimensional array of numbers` called `Tensors`

## Layering

- The tensor suffers several transformations on multiple `layers` and the final layer is the desired output
- On each layer the tensor is tunned by applying the weights

### Weights

- Weights are the paramters of the model
- On each layer, the parameters (`weights`) are applied (by weighted sum) to the current tensor, tunning the tensor
- The `weights` is organized as a matrix, that is used to multiply the tensors
  - E.g., GPT-3 has 175 billion weights (parameters) organized into 27 thousand matrices

## Backpropagation
