import numpy as np

if __name__ == "__main__":
    for i in range(100):
        print(np.random.randint(0,3))
    # array = np.array([[1,2,3],[2,3,4]])
    # print(array)
    # print(array.size)
    # print(array.shape)
    # print(array.ndim)
    # print(array.dtype)
    # print(array.base)

    # array1 = np.array([1,2,3],dtype=np.int)
    # print(array1)
    # print(array1.dtype)
    # print(np.average(array1))
    # print(np.zeros((3,4)))
    # print(np.ones((3,4)))

    # 数列
    # print(np.arange(12).reshape((3,4)))
    # 生成线段
    # print(np.linspace(1,10,6).reshape(2,3))

    # a = np.array([10,20,30,40])
    # b = np.arange(4)
    #
    # print(a)
    # print(b)
    # print(b**2)
    # print(b<3)
    # print(np.sin(b))
    # print(a-b)
    # print(a*b)

    # 矩阵运算
    # a = np.array([[1,1],[0,1]])
    # b = np.arange(4).reshape((2,2))
    #
    # print(a)
    # print('----------')
    # print(b)
    # print('----------')
    # c = a*b
    # c_dot = np.dot(a,b)
    # print(c)
    # print('----------')
    # print(c_dot)

    # 取最大值与最小值
    # a = np.random.random((2,4))
    # print(a)
    # print('----------')
    # print(np.min(a, axis=0))
    # print(np.max(a))

    # 取索引值
    # A = np.arange(2,14).reshape(3,4)
    # print(A)
    # print(np.argmin(A))
    # print(np.argmax(A))
    # print(np.mean(A))
    # print(np.median(A))
    # print(np.cumsum(A))
    # print(np.diff(A))
    # print(np.nonzero(A))
    # print(np.sort(A))
    # print(np.transpose(A))
    # print(np.clip(A,5,9))

    # A = np.arange(3,15).reshape(3,4)
    # print(A)
    # print(A[1][1])
    # print(A[2:,])
    # print(A[:,1])
    # print('print row')
    # for row in A:
    #     print(row)
    #
    # print('print column')
    # for culomn in A.T:
    #     print(culomn)
    # print('item')
    # for item in A.flat:
    #     print(item)

    # A = np.array([1,1,1])
    # B = np.array([2,2,2])
    # C = np.vstack((A,B))
    # D = np.hstack((A,B))
    # print(C)
    # print(C.shape)
    # print(D)
    # print(D.shape)
    # print(A[:np.newaxis,])
    # print(A[np.newaxis,:].shape)