# encoding: utf-8
import pandas as pd

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50

def print_csv():
    df = pd.read_csv("result_string.csv")
    # print(df["value"].head(1000))
    # df.to_csv('df_output.csv', encoding='utf-8')
    df = df.value.str.decode("latin1").str.encode("utf-8")
    df.to_csv('df_output.csv', encoding='utf-8')
    
print_csv()