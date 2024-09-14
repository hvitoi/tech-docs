# Training a Model

- To train our model we must have good data
- `Garbage in` => `Garbage out`

## Labeled vs. Unlabeled Data

- **Labeled data** has input features and the corresponding output labels
  - It gives a clue on what the data is about
  - With labeled data you can apply `supervised learning` where the model is trained to map inputs to known outputs

- **Unlabeled data** is just raw data
  - With unlabeled data you can apply `unsupervised learning`, the algorithm itself tries by itself to find pattern in the data and group them together

## Structured vs. Unstructured Data

- **Structured Data** is structured in a predefined format
  - E.g., csv file, time series data

- **Unstructured Data** doesn't follow a specific structure
  - It's usually text-heavy or multimedia content
  - Text data: articles, social media posts, customer reviews
  - Image data: just pixels

## Training Data

- **Training Set**
  - Typically 80% of the dataset
  - Used to the train the model

- **Validation Set**
  - Typically 10% of the dataset
  - Used to tune model hyperparameters and validate performance
  - Tune the settings of the algorithm to make it more efficient

- **Test Set**
  - Typically 10% of the dataset
  - Used the evaluate the final model performance

## Feature Engineering

- It's a preprocessing of the training data to better fit the domain knowledge of the model
- It's also called `ETL` (create, transform, extract) variables from data
- Enhances the performance of the model
- It's applied over structured data or ever unstructured data

- Techniques
  - `Feature extraction`: e.g., derive age from birth date
  - `Feature selection`: e.g., pick only the fields relevant to the model
  - `Feature transform`: e.g., normalize numerical data
  - `TF-IDF`: convert text into numerical features or word embeddings

## Hyperparameter Tuning

- Settings that define the model structure and learning algorithm and process
- Examples
  - `Learning rate`
  - `Batch size`
  - `Number of epochs`
  - `Regularization`

- Tuning it is finding the best hyperparameters values to optimize the model performance
  - Improving it reduces overfitting and enhances generalization

- How?
  - Grid search, random search
  - Amazon SageMaker Automatic Model Tuning (AMT)

## Supervised Learning

- Based on labeled data
- Sometimes difficult to implement because labeled data is not easily available
- Examples
  - Linear regression uses labeled data points (x -> y)
  - Classification of images with labeled animals (cats, dogs, etc)
  - Binary classification: email spams

## Unsupervised Learning

- Discover "automatically" inherent patterns, structure or relationships within the input data
- The machine must uncover and create the groups itself

- Techniques
  - `Clustering`
    - Customer segmentation
    - Targeted Marketing
    - Recommender systems
  - `Association Rule Learning`
    - Market basket analysis (products that are bought together)
  - `Anomaly Detection`
    - Fraud (spot outlier transactions)
  - `Dimensionality Reduction`

## Semi-supervised Learning

![Semi-supervised Learning](.images/semi-supervised-learning.png)

## Reinforcement Learning (RL)

- An agent learns to make decisions by trying to maximize a "reward"
- E.g., the shortest way out of a maze

- `Agent`: learner or decision-maker
- `Environment`: the external system the agent interacts with
- `Action`: choices made by the agent
- `Reward`: the feedback from the environment based on the agent's actions
- `State`: the current situation of the environment
- `Policy`: the strategy the agent uses to determine actions based on the state

- It is simulated many times to get the optimal strategy
- Goal: maximize the cumulative reward over time

### Reinforcement Learning From Human Feedback (RLHF)

- Use human feedback to help ML models to self-learn more efficiently
- Incorporates human feedback in the reward function

1. Data collection
1. Supervised fine-tuning of a language model
1. Build a separate reward model
1. Optimize the language model with the reward-based model
