#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


def function(loss, lr):
    optimizer = tf.train.AdamOptimizer(lr).minimize(loss)
    return optimizer

