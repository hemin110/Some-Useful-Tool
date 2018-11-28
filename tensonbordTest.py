#encoding=utf-8

import tensorflow as tf
from tensorflow.python.platform import gfile


graph = tf.get_default_graph()
_ = tf.train.import_meta_graph("E://workgit//ml4dzjz//classfication_82_cpu//checkpoint//model.ckpt-125000.meta")
summary_write = tf.summary.FileWriter("F://tflog" , graph)


