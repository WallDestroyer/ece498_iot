import tensorflow as tf

import numpy as np

def function(session, loss):
    return loss.eval(session=session)[0][0]
    #return np.asscalar(session.run(loss))


