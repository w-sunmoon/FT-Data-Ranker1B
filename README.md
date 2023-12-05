# FT-Data-Ranker1B

### 文件说明

my_get_train_data.py 为**数据处理**代码

my_train.py 为**模型微调**代码

其余文件为上述两个脚本执行的**辅助文件**

### 操作步骤

1. 将所提供的所有文件放到**同一个路径**下面，本人使用的路径为/tmp/code，该路径为**绝对路径**，假设您使用的绝对路径为/tmp/yourpath

2. 将所提供文件里的所有/tmp/code均替换为/tmp/yourpath，具体来说：

    将my_get_train_data.py里所有/tmp/code 替换为 /tmp/yourpath

    将my_train.py里所有/tmp/code 替换为 /tmp/yourpath

    将install.sh第1行的/tmp/code 替换为 /tmp/yourpath

    将prepare_data_and_models.sh第8行/tmp/code 替换为 /tmp/yourpath

    将alpaca-cot-en-refine.yaml第3行与第4行/tmp/code 替换为 /tmp/yourpath

    将alpaca-cot-zh-refine.yaml 第3行与第4行/tmp/code 替换为 /tmp/yourpath

    将get_train_dataset_1b.py 第9、10、11、43行/tmp/code 替换为 /tmp/yourpath

3.  将my_train.py里第21行/tmp/output/sftmodel.zip替换为 您指定的输出路径，假设为/tmp/yourpath/sftmodel.zip

4. 打开终端：进入/tmp/yourpath

   输入：python my_get_train_data.py

   得到D_{process}于/tmp/yourpath/results/sample1b.jsonl

5. 输入：python my_train.py

   得到全参数微调后的模型zip包于/tmp/yourpath/sftmodel.zip

6. 根据 [提交指南 ]([FT-Data Ranker：大语言模型微调数据竞赛 -- 1B模型赛道_算法大赛_天池大赛-阿里云天池的赛制 (aliyun.com)](https://tianchi.aliyun.com/competition/entrance/532157/customize404))页面 6.1可以进行微调后模型的推理和本地评估

### 数据处理

get_train_dataset_1b.py 为对应的数据处理脚本，该脚本可得到用于训练的模型的数据，其中两个输入的改良数据集为执行[提交指南]([FT-Data Ranker：大语言模型微调数据竞赛 -- 1B模型赛道_算法大赛_天池大赛-阿里云天池的赛制 (aliyun.com)](https://tianchi.aliyun.com/competition/entrance/532157/customize404))页面3.1改良原始数据集后得到的结果

关于脚本中**TOKEN_NUMS**、**RATIO**两个参数设置的说明： TOKEN_NUMS代表了用于训练的样本数目。根据[文献](https://arxiv.org/abs/2303.14742)，对于大部分的任务而言，数据质量一定的情况下，用于指令微调的数据**越多**，最终得到的模型效果**越好**。RATIO表示微调数据中英数据的混合比例，已知实际面临的任务语言为英文，虽然大模型具有一定的涌现能力，但是其真正能解决的任务，或者说能处理的较好的任务还是和训练数据紧密相关。为了使训练数据与测试数据之间的**差异尽可能小**，我们选择将RATIO设置为1.0，即全采英文数据。在比赛的过程中，对于TOKEN_NUMS，我们设置了10W、20W、25W、30W，虽然从25W到30W之间，模型的最终得分提升的并不大，但30W对应的模型得分确实是最好的，当然训练的时间成本也在提升。对于RATIO，我们比较了0.5,  0.8，1.0，1.0对应的得分最高，这点与理论的分析保持一致。

### 全量微调

my_train.py运行后即可得到全量微调后的模型，比赛使用的微调核心代码deepspeed_train_1b.sh为结合实际的计算资源对competition_kit提供的文件进行适当调整所得

### 相关参考

Data-Juicer算子库介绍：[data-juicer/docs/Operators.md at main · alibaba/data-juicer · GitHub](https://github.com/alibaba/data-juicer/blob/main/docs/Operators.md)

LLM数据选择：https://arxiv.org/abs/2303.14742

