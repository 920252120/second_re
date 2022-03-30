import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
import evaluate as eva




def data_norm(file_path, index_station):  # index_station 用来指示公司的序列
    mydata = pd.read_csv(file_path, encoding='gbk')
    mydata = mydata[['index', index_station]]
    max_value = max(mydata[index_station])
    min_value = min(mydata[index_station])
    mydata[[index_station]] = mydata[[index_station]].apply(lambda x:(x - min_value) / (max_value - min_value))
    return mydata, max_value, min_value
    # print(mydata['1'])
    # print("mydata: {}, mydata['1']: {}".format(type(mydata), type(mydata['1'])))


def data_group(data, days_picked, days_topredict):  # size指的是取多少天的数据预测
    X = []
    Y = []
    for i in range(data.shape[0] - days_picked - days_topredict):
        X.append(np.array(data.iloc[i:(i + days_picked), 1].values, dtype=np.float32))
        Y.append(np.array(data.iloc[(i + days_picked):(i+days_picked+days_topredict), 1].values, dtype=np.float32))
    return X, Y


def set_dataset(X, Y, traintest_rate, batch_size):
    length = len(Y)
    trainx, trainy = X[:int(traintest_rate * length)], Y[:int(traintest_rate * length)]
    testx, testy = X[int(traintest_rate * length):], Y[int(traintest_rate * length):]
    train_loader = DataLoader(dataset=Mydataset(trainx, trainy), batch_size=batch_size)
    test_loader = DataLoader(dataset=Mydataset(testx, testy), batch_size=batch_size)
    return train_loader, test_loader


class Mydataset(Dataset):
    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def __getitem__(self, index):
        x1 = self.x[index]
        y1 = self.y[index]
        return x1, y1

    def __len__(self):
        return len(self.x)


class Fnn(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super(Fnn, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.linear1 = nn.Linear(self.input_size, self.hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        return out


class Lstm(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Lstm, self).__init__()  # 把RNN的实例转化为其父类的实例，然后调用init

        self.rnn = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=1,
            batch_first=True,  # 设置取每一批次的元素进行排列，使其取的每一批元素都是相邻元素
        )

        self.linear = nn.Linear(hidden_size, output_size)  # 全连接层，输入64维， 输出10维

    def forward(self, x):
        r_out, (h_n, h_c) = self.rnn(x, None)
        r_out = r_out[:, -1, :]
        out = self.linear(r_out)  # 取最后一次迭代的结果???
        return out


def fnn_train(i_size, h_size, o_size, lr, epochs, train_loader):
    fnn = Fnn(input_size=i_size, hidden_size=h_size, output_size=o_size)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(fnn.parameters(), lr =lr)
    for i in range(epochs):
        total_loss = 0
        for index, (data, label) in enumerate(train_loader):
            pred = fnn(data)
            label = label.squeeze(1)
            pred = pred.squeeze(1)
            loss = criterion(pred, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        # print(total_loss)
    torch.save({'state_dict': fnn.state_dict()}, 's.pkl')


def fnn_test(i_size, h_size, o_size, test_loader, save_file):
    fnn = Fnn(input_size=i_size, hidden_size=h_size, output_size=o_size)
    fnn.load_state_dict(torch.load(save_file)['state_dict'])
    preds = []
    labels = []

    for index, (data, label) in enumerate(test_loader):
        pred = fnn(data)
        preds.extend(pred.squeeze(1).tolist())
        labels.extend(label.squeeze(1).tolist())

        # print('预测值是%.2f, %.2f, 真实值是%.2f, %.2f' %(pred[0][0], pred[0][1], label[0][0], label[0][1]))
    return preds, labels


def lstm_train(input_size, hidden_size, output_size, epoch, train_loader):
    lstm = Lstm(input_size, hidden_size, output_size)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(lstm.parameters(), lr=lr)

    for epo in range(epoch):
        for i, (x, y) in enumerate(train_loader):
            x = x.unsqueeze(2)
            pred = lstm(x)
            # y = y.squeeze(1)
            # pred = pred.squeeze(1)
            loss = criterion(pred, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # print(total_loss)
        torch.save({'state_dict': lstm.state_dict()}, 'lstm.pkl')


def lstm_test(i_size, h_size, o_size, test_loader, save_file):
    lstm = Lstm(input_size=i_size, hidden_size=h_size, output_size=o_size)
    lstm.load_state_dict(torch.load(save_file)['state_dict'])
    preds = []
    labels = []

    for index, (data, label) in enumerate(test_loader):
        data = data.unsqueeze(2)
        pred = lstm(data)
        preds.extend(pred.squeeze(1).tolist())
        labels.extend(label.squeeze(1).tolist())

        # print('预测值是%.2f, 真实值是%.2f' % (preds[-1],  label[-1]))
    return preds, labels


def show_predict(pre, label):
    fig = plt.figure(figsize=(100, 20))
    ax = fig.add_subplot(1, 1, 1)
    preds = pd.Series(pre)
    labels = pd.Series(label)
    preds.plot(ax=ax, style='k-', label="pred")
    labels.plot(ax=ax, style='b-', label="labels")
    # plt.plot(preds, label="pred")
    # plt.plot(labels, label="labels")
    plt.legend()
    plt.show()
    plt.close()


def re_norm(data, max, min):
    return data*(max-min) + min


def mean_predict(data, days):
    if days == 1:
        return data
    result = []
    m = days
    length = len(data)
    for j in range(0, m-1):
        output = 0
        for z in range(0, j+1):
            output += data[z][j]
        output /= j+1
        result.append(output)
    for i in range(0, length-(m-1)):
        output = 0
        for z in range(1, m+1):
            output += data[i+z-1][m-z]
        output /= m
        result.append(output)
    for j in range(0, m-1):
        output = 0
        for z in range(0, j+1):
            output += data[length-1-z][m-1-j]
        output /= j+1
        result.append(output)
    return result









if __name__ == '__main__':
    input_size = 1
    seq_size = 30
    hidden_size = 64
    output_size = 7
    batch_size =30
    epoch = 500
    lr = 0.001
    traintest_rate = 0.8
    station = '出口南线'
    # file_path = r'C:\Users\LYQ\Desktop\datanalyze\test\to_2016\2016yearflow.csv'
    file_path = r'C:\Users\LYQ\Desktop\datanalyze\值得挖掘的公司数据\filtered.csv'
    save_file = 'lstm.pkl'

    mydata, max_value, min_value = data_norm(file_path, station)  # 获取station数据，并最大最小归一化
    X, Y = data_group(mydata, seq_size, output_size)  # 处理数据，根据预测需要的天数和输出来处理
    train_loader, test_loader = set_dataset(X, Y, traintest_rate, batch_size=batch_size)  # 设置数据集，rate为分割训练集和测试集的比例

    lstm_train(input_size, hidden_size, output_size, epoch,train_loader)  # 训练
    preds, labels = lstm_test(input_size, hidden_size, output_size, test_loader, save_file)  # 测试，返回预测数组和真实数组

    preds = mean_predict(preds, output_size)
    labels = mean_predict(labels, output_size)

    preds = eva.to_array(preds)
    labels = eva.to_array(labels)

    preds = re_norm(preds, max_value, min_value)  # 反归一化
    labels = re_norm(labels, max_value, min_value)

    show_predict(preds, labels)  # 可视化

    eva.evaluate(preds, labels)  # 评估预测结果

    # output = pd.DataFrame({'pred':preds, 'labels':labels})
    # output.to_csv(r'C:\Users\LYQ\Desktop\datanalyze\test\test.csv')



