# Recurrent Neural Network (RNN) Reading Resource

## 1. How it works?
1. [LSTM-GRU-from-scratch](https://github.com/kaustubhhiware/LSTM-GRU-from-scratch/blob/master/module.py)
2. [Implementing LSTM Neural Network from Scratch](https://www.kaggle.com/navjindervirdee/lstm-neural-network-from-scratch)
3. [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

## 1. Batch, Timestamp, dimension

1. [What is the timestep in Keras' LSTM?](https://stackoverflow.com/questions/54009661/what-is-the-timestep-in-keras-lstm)
2. [请问rnn和lstm中batchsize和timestep的区别是什么？](https://www.zhihu.com/question/279046805)

## 2. LSTM weights and bias

1. [Demystifying LSTM Weights and Bias Dimensions (has typo in kernel in recurrent kernel)](https://medium.com/analytics-vidhya/demystifying-lstm-weights-and-biases-dimensions-c47dbd39b30a)
2. [How LSTM store the weights? (TF official source code line 1911)](https://github.com/keras-team/keras/blob/1d81a20292ca6926e595d06a6cd725dbb104a146/keras/layers/recurrent.py#L1911)
3. [How to interpret weights in a LSTM layer in Keras [closed]](https://stackoverflow.com/questions/42861460/how-to-interpret-weights-in-a-lstm-layer-in-keras)
4. [What is the meaning of multiple kernels in keras lstm layer?](https://stackoverflow.com/questions/55723284/what-is-the-meaning-of-multiple-kernels-in-keras-lstm-layer)
4. [Understanding LSTM and its diagrams](https://medium.com/mlreview/understanding-lstm-and-its-diagrams-37e2f46f1714)

## 3. How to prepare data
1. [循环神经网络系列（四）基于LSTM的MNIST手写体识别](https://nulls.blog.csdn.net/article/details/83745098)
2. 

## 4. Stateful and Stateless
1. [Difference Between Return Sequences and Return States for LSTMs in Keras](https://machinelearningmastery.com/return-sequences-and-return-states-for-lstms-in-keras/)
2. [Stateful and Stateless LSTM for Time Series Forecasting with Python](https://machinelearningmastery.com/stateful-stateless-lstm-time-series-forecasting-python/)

## 5. Return sequence, Return hidden state, Return cell state
1. [Setting and resetting LSTM hidden states in Tensorflow 2](https://adgefficiency.com/tf2-lstm-hidden/)

## 6. Different batch size when training and predicting
**Sometimes the number of training batch and prediction batch is different, especially in production. To do that, it is
important to change the structure of the model and load the weights first**
1. [How to use Different Batch Sizes when Training and Predicting with LSTMs](https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/)