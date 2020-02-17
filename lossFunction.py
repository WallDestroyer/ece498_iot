import tensorflow as tf

import numpy as np


def function(a, X, b, y):
    #(a(X^t*X) + b^t*X - y) ** 2
    p =  tf.matmul(tf.transpose(b),X) + a * tf.matmul(tf.transpose(X) ,X)

    result = tf.math.squared_difference(p,2)
    return result
