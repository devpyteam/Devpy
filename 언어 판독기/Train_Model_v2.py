from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

# 데이터셋
train = "train.csv"
test = "test.csv"

# 데이터셋을 불러옵니다.
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=train,
    target_dtype=np.int,
    features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=test,
    target_dtype=np.int,
    features_dtype=np.float32)

x_data = training_set.data
y_data = training_set.target
y = [[0]for i in range(y_data.size)]
count=0
for i in y_data:
    y[count][0] = i
    count += 1
y_data = [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]

X = tf.placeholder(tf.float32, shape = [None,26])
Y = tf.placeholder(tf.float32, shape = [None,3])

w1 = tf.Variable(tf.random_normal([26,10]))
b1 = tf.Variable(tf.random_normal([10]))
L1 = tf.nn.relu(tf.matmul(X,w1)+b1)

w2 = tf.Variable(tf.random_normal([10,20]))
b2 = tf.Variable(tf.random_normal([20]))
L2 = tf.nn.relu(tf.matmul(L1,w2)+b2)

w3 = tf.Variable(tf.random_normal([20,10]))
b3 = tf.Variable(tf.random_normal([10]))
L3 = tf.nn.relu(tf.matmul(L2,w3)+b3)

w4 = tf.Variable(tf.random_normal([10,3]))
b4 = tf.Variable(tf.random_normal([3]))

model = tf.matmul(L3,w4)+b4

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=Y))
optimizer = tf.train.AdadeltaOptimizer(learning_rate=0.01).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(100001):
        cost_val, _ = sess.run([cost,optimizer], feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step,": ",cost_val)

    correct_prediction = tf.equal(tf.argmax(model,1), tf.arg_max(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print('Accuracy: ', sess.run(accuracy, feed_dict={X:x_data, Y: y_data}))