import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
img = mnist.train.images[0].reshape(28, 28)

sess = tf.InteractiveSession()

img = img.reshape(-1, 28, 28, 1) #(n개의 이미지, 28행, 28열, 흑/백)
W1 = tf.Variable(tf.random_normal([3, 3, 1, 5])) #총 5개의 필터
# 필터 적용
conv2d = tf.nn.conv2d(img, W1, strides=[1, 2, 2, 1], padding='SAME')
print("conv2d=", conv2d)
sess.run(tf.global_variables_initializer())

# 출력
conv2d_img = conv2d.eval()
conv2d_img = np.swapaxes(conv2d_img, 0, 3)
for i, one_img in enumerate(conv2d_img):
    plt.subplot(1, 5, i + 1), plt.imshow(one_img.reshape(14, 14), cmap='gray')
    #plt.show()

# Max Pooling
# ksize = kernel size
pool = tf.nn.max_pool(conv2d, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
print("pool=", pool)

sess.run(tf.global_variables_initializer())
pool_img = pool.eval()
pool_img = np.swapaxes(pool_img, 0, 3)

#출력
for i, one_img in enumerate(pool_img):
    plt.subplot(1, 5, i + 1)
    plt.imshow(one_img.reshape(7, 7), cmap='gray')
    plt.show()
