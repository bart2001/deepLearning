import tensorflow as tf
import numpy as np

sentence = ("if you want to build a ship, don't drum up people together to "
            "collect wood and don't assign them tasks and work, but rather "
            "teach them to long for the endless immensity of the sea.")

char_set = list(set(sentence))  #25가지의 문자
char_dic = {w: i for i, w in enumerate(char_set)}
# 역사전 사용
inv_char_dic = {v: k for k, v in char_dic.items()}
#print(char_dic['a'])
#print(char_dic['0'])
#exit()


dataX = []
dataY = []

data_dim = len(char_set)
hidden_size = len(char_set)
num_classes = len(char_set)
sequence_length = 10

for i in range(0, len(sentence) - sequence_length):

    x_str = sentence[i : i + sequence_length]
    y_str = sentence[i + 1 : i + sequence_length + 1]
    #print(i, "=", x_str, '->', y_str)

    x = [char_dic[c] for c in x_str]
    y = [char_dic[c] for c in y_str]

    dataX.append(x)
    dataY.append(y)

print('dataX=', len(dataX[0]))
print('dataY=', len(dataY[0]))

batch_size = len(dataX)

X = tf.placeholder(tf.int32, [None, sequence_length]) # X_data
Y = tf.placeholder(tf.int32, [None, sequence_length]) # Y_label
X_one_hot = tf.one_hot(X, num_classes)

cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, X_one_hot, initial_state=initial_state, dtype=tf.float32)

weights = tf.ones([batch_size, sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

prediction = tf.argmax(outputs, axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(500):
        l, _ = sess.run([loss, train], feed_dict={X: dataX, Y: dataY})

        results = sess.run(prediction, feed_dict={X: dataX})

        if i % 10 == 0:
            for index, item in enumerate(results):

                char_list = [inv_char_dic[c] for c in item]
                print(''.join(char_list))

            #print("step={}, loss={:.03f}, Prediction={}".format(i, l, result))
