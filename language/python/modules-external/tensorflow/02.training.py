# %% [markdown]
# # MNIST Data Set - Basic Approach

# %% [markdown]
# ### Get the MNIST Data

# %%
import tensorflow as tf
import tensorflow_datasets as tfds


# %%
mnist = tfds.load("mnist:1.*.*")

# %%
mnist

# %%
#mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# %% [markdown]
# ** Alternative sources of the data just in case: **
#
# * http://yann.lecun.com/exdb/mnist/
# * https://github.com/mrgloom/MNIST-dataset-in-different-formats

# %%
type(mnist)

# %%
mnist.train.images.shape

# %%
mnist.train.images

# %%
mnist.train.num_examples

# %%
mnist.test.num_examples

# %%
mnist.validation.num_examples

# %% [markdown]
# ### Visualizing the Data

# %%
import matplotlib.pyplot as plt
%matplotlib inline

# %%
mnist.train.images[1].shape

# %%
plt.imshow(mnist.train.images[1].reshape(28,28))

# %%
plt.imshow(mnist.train.images[1].reshape(28,28),cmap='gist_gray')

# %%
mnist.train.images[1].max()

# %%
plt.imshow(mnist.train.images[1].reshape(784,1))

# %%
plt.imshow(mnist.train.images[1].reshape(784,1),cmap='gist_gray',aspect=0.02)

# %% [markdown]
# ## Create the Model

# %%
x = tf.placeholder(tf.float32,shape=[None,784])

# %%
# 10 because 0-9 possible numbers
W = tf.Variable(tf.zeros([784,10]))

# %%
b = tf.Variable(tf.zeros([10]))

# %%
# Create the Graph
y = tf.matmul(x,W) + b

# %% [markdown]
# Loss and Optimizer

# %%
y_true = tf.placeholder(tf.float32,[None,10])

# %%
# Cross Entropy

# %%
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_true, logits=y))

# %%
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)

# %%
train = optimizer.minimize(cross_entropy)

# %% [markdown]
# ### Create Session

# %%
init = tf.global_variables_initializer()

# %%
with tf.Session() as sess:
    sess.run(init)

    # Train the model for 1000 steps on the training set
    # Using built in batch feeder from mnist for convenience

    for step in range(1000):

        batch_x , batch_y = mnist.train.next_batch(100)

        sess.run(train,feed_dict={x:batch_x,y_true:batch_y})

    # Test the Train Model
    matches = tf.equal(tf.argmax(y,1),tf.argmax(y_true,1))

    acc = tf.reduce_mean(tf.cast(matches,tf.float32))

    print(sess.run(acc,feed_dict={x:mnist.test.images,y_true:mnist.test.labels}))

# %% [markdown]
# While this may seem pretty good, we can actually do much better, the best models can get above 99% accuracy.
#


