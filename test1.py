# chao
# 时间：2023/5/23 9:25 下午


import tensorflow as tf

tensorflow_version = tf.__version__
gpu_available = tf.test.is_gpu_available()

print("tensorflow version:", tensorflow_version, "\tGPU available:", gpu_available)

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([1.0, 2.0], name="b")
result = tf.add(a, b, name="add")
print(result)