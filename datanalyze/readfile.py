import pandas as pd




def load_data():
    cp_data_month = []
    for j in range(100):
        if j == 1:
            break
        if j== 2:
            continue
        if j == 15:
            continue
        if j == 18:
            continue
        if j == 24:
            continue
        if j == 35:
            continue
        if j == 39:
            continue
        if j == 40:
            continue
        if j == 41:
            continue
        if j == 42:
            continue
        if j == 57:
            continue
        if j == 65:
            continue
        if j == 72:
            continue
        if j == 76:
            continue
        if j == 91:
            continue
        if j == 99:
            continue
        data = []
        list = ['f', 'pl', 't', 'p', 'tot', 'md', 'ye', 'recTime', 'thetime']
        for i in range(1):
            path = 'C:\\Users\\LYQ\\Desktop\\datanalyze\\all0-100\\' + str(j + 1) + '\\rw' + str(
                j + 1) + '-2021-' + str(i + 1) + '.csv'
            to_path = r'C:\Users\LYQ\Desktop\datanalyze\to_all0-100' + '\\' +  str(j + 1) \
            + '\\rw' + str(j + 1) + '-2021-' + str(i + 1) + '.csv'


            df_data = pd.read_csv(path, header=None, sep='\\t', engine='python')
            df_data.columns = list
            print(df_data[['f', 't', 'p', 'tot', 'recTime', 'thetime']])
            df_data.to_csv(to_path)
        #     aa = df_data.values[-1, 4] - df_data.values[0, 4]
        #     if aa < 0:
        #         aa = aa1
        #
        #     data.append(aa)
        #     aa1 = aa
        # cp_data_month.append(data)

    return (cp_data_month)

if __name__ == '__main__':
    data = load_data()
    print(data)