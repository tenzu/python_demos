# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
import time

time0 = time.time()
# 下载数据需要一点时间
faces = fetch_lfw_people()
time1 = time.time()
print('下载数据集时间:\n', time1 - time0, 's')
print('数据集包含的keys:\n', faces.keys())
print('样本数和特征数:\n', faces.data.shape)
print('images包含的信息(样本数, 62*47像素的图像):\n', faces.images.shape)

# 随机获取 36 张脸的数据
random_indexes = np.random.permutation(len(faces.data))
X = faces.data[random_indexes]
example_faces = X[:36, :]


# 绘制函数
def plot_faces(faces):
    fig, axes = plt.subplots(6,
                             6,
                             figsize=(10, 10),
                             subplot_kw={
                                 'xticks': [],
                                 'yticks': []
                             },
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(faces[i].reshape(62, 47), cmap='bone')
    plt.show()


# 绘制随机抽取的 36 张脸
plot_faces(example_faces)

# 绘制特征脸
time0 = time.time()
pca = PCA(svd_solver='randomized')
pca.fit(X)
time1 = time.time()
print('训练时间:\n', time1 - time0, 's')
print('降维后的样本数量和特征数:\n', pca.components_.shape)
# 绘制降维后的特征脸
plot_faces(pca.components_[:36, :])
