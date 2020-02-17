import tensorflow as tf

import numpy as np



def function(shape):
    my_array = tf.random.uniform(shape=shape)#, dtype=tf.float32)
    return tf.Variable(my_array)