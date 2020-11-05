'''
author：小靳哥哥
project：三层神BP经网络模型
'''
# 导入numpy并命名为np
import numpy as np

'''
# 构造神经网络
'''


class NeuralNetwork():
    def __init__(self):
        # 随机数生成的种子随机数生成的种子
        np.random.seed(1)
        # 将权重转换为值为-1到1且平均值为0的3乘1矩阵
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    # 定义signoid函数的导数
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    # 计算sigmoid函数的导数

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    # 训练
    def train(self, train_inputs, train_outputs, train_iterations):  # 输入 输出 迭代次数
        # 训练模型在不断调整权重的同时做出准确预测
        for iteration in range(train_iterations):
            # 通过神经元提取训练数据
            output = self.think(train_inputs)
            # 反向传播错误率
            error = train_outputs - output
            # 进行权重调整
            adjustments = np.dot(train_inputs.T, error *
                                 self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
    # 输出

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


# 初始化类
neural_network = NeuralNetwork()

print("开始随机生成权重: ")
print(neural_network.synaptic_weights)

# 载入训练数据（3个输入值，一个输出值）
train_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
train_outputs = np.array([[0, 1, 1, 0]]).T
neural_network.train(train_inputs, train_outputs, 150000)

print("最终所得权重： ")
print(neural_network.synaptic_weights)


'''
测试
'''
print('开始测试')
input_1 = str(input("输入第一个值: "))
input_2 = str(input("输入第一个值: "))
input_3 = str(input("输入第一个值: "))

print("输入值: [", input_1, input_2, input_3, ']')
print("输出结果: ")
print(neural_network.think(np.array([input_1, input_2, input_3])))
