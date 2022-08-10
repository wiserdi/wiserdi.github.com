import os

def test(data_path, length):
    if length > len(os.listdir(data_path)):
        print('Out of Length')
        return None
    print(os.listdir(data_path))
    for num in range(0, length):
        file_name = os.listdir(data_path)[num]
        new_name = file_name.replace('Hong Kong', 'HandK')  # 替换
        os.rename(data_path + file_name, data_path + new_name)

test('C:/Users/AndyC/wiserdi.github.io/source/stuff/', len(os.listdir("C:/Users/AndyC/wiserdi.github.io/source/stuff/")))
