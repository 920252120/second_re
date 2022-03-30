import functions as fun
import evaluate as eva


if __name__ == '__main__':

    input_size = 30
    hidden_size = 100
    output_size = 7
    lr = 0.001
    epochs = 50
    traintest_rate = 0.8
    station = '出口南线'
    save_file = 's.pkl'
    # file_path = r'C:\Users\LYQ\Desktop\datanalyze\test\to_2016\2016yearflow.csv'
    file_path = r'C:\Users\LYQ\Desktop\datanalyze\值得挖掘的公司数据\filtered.csv'

    mydata, max_value, min_value = fun.data_norm(file_path, station)
    X, Y = fun.data_group(mydata, input_size, output_size)
    train_loader, test_loader = fun.set_dataset(X, Y, traintest_rate, 1)
    fun.fnn_train(input_size, hidden_size, output_size, lr, epochs, train_loader)
    preds, labels = fun.fnn_test(input_size, hidden_size, output_size, test_loader, save_file)

    preds = fun.mean_predict(preds, output_size)
    labels = fun.mean_predict(labels, output_size)

    preds = eva.to_array(preds)
    labels = eva.to_array(labels)

    preds = fun.re_norm(preds, max_value, min_value)  # 反归一化
    labels = fun.re_norm(labels, max_value, min_value)

    fun.show_predict(preds, labels)

    eva.evaluate(preds, labels)