import tensorflow as tf

# Create some variables.
v1 = tf.get_variable(name="v1", shape=[3], initializer=tf.zeros_initializer())
v2 = tf.get_variable(name="v2", shape=[5], initializer=tf.zeros_initializer())

inc_v1 = v1.assign(v1+1)
dec_v2 = v2.assign(v2-1)

# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, and save the
# variables to disk.

with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.
  c = inc_v1.op.run()
  d = dec_v2.op.run()
  print(c, d)
  # Save the variables to disk.
  #save_path = saver.save(sess, "./model.ckpt")
  #print("Model saved in file: %s" % save_path)

