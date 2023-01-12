# 资源文件比较工程

## 背景

该工程用于比较原始的apk和翻译的xlsx文件中的内容。
输入的数据为原始的apk文件和翻译公司生成的xlsx文件转换成的csv。
先从jenkins下载相关的apk，作为source输入，再把翻译公司的xlsx文件转换成csv。


## 前提

运行之前请先在电脑上安装相关python依赖。
```shell
    pip install -r requirements.txt
```


## 使用方法

典型的使用方法如下，

```shell
    # 英语
    python str_value_compare.py --source ./pangu.apk --source_col "en" --dest "China Oversea English Resources(2022-01-20).xlsx" --dest_col "English text" --dest_sheet "wukong"

    # 阿拉伯语
    python str_value_compare.py --source ./pangu.apk --source_col "ar" --dest "China Oversea English Resources(2022-01-20).xlsx" --dest_col "ar(Arabic)" --dest_sheet "wukong"

```

输出结果再当前目前下，

如果是阿拉伯语，就是ar_diff.csv。

如果是英语，就是en_diff.csv。

整体效果如图所示。

![Run result](./imgs/run_result.png)

![Diff CSV](./imgs/res_diff.png)
