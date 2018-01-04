import tensorflow as tf
import numpy as np

# cross-entropy, one_hot 함수를 더 간단하게 코드로 구현해보자!!!

xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)

x_data = xy[:, :-1]
y_data = xy[:, -1:]

nb_classes = 7   # 0~6

X = tf.placeholder(tf.float32, [None, 16])
Y = tf.placeholder(tf.int32, [None, 1])

# one_hot_encoding
Y_one_hot = tf.one_hot(Y, nb_classes)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='weight')

# hypothesis
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits=logits)

# cross-entropy cost funcion
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# 예측 테스트
prediction = tf.arg_max(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})

        if step % 100 == 0:
            cost_val, accuracy_val = sess.run([cost, accuracy]
                , feed_dict={X: x_data, Y: y_data})
            print("step={}\tcost_val={:.3f}\taccuracy_val={:.2%}"
                  .format(step, cost_val, accuracy_val))

    prediction_val = sess.run(prediction, feed_dict={X: x_data})
    for p, y in zip(prediction_val, y_data.flatten()):
        #print("[{}] Prediction: {} True Y: P {}".format(p == int(y), p, int(y)))
        print("[{}] 예측={} 실제={}".format(p == int(y), p, int(y)))