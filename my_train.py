import os
import random
import numpy as np
import torch
# 使用 random 模块
random.seed(6)
# 使用 numpy
np.random.seed(6)
# 在 PyTorch 中
torch.manual_seed(6)
os.system('pip install transformers==4.31.0')

#  训练
# 修改相关参数
os.system('rm -rf /tmp/code/competition_kit/lm-training/train_scripts/deepspeed_train_1b.sh')
os.system('cp -r /tmp/code/deepspeed_train_1b.sh /tmp/code/competition_kit/lm-training/train_scripts/')
os.system('cd /tmp/code/competition_kit/lm-training && sh train_scripts/deepspeed_train_1b.sh \
    /tmp/code/competition_kit/data/models/falcon-rw-1b \
    /tmp/code/results/sample1b.jsonl\
    /tmp/code/competition_kit/data/models/falcon-rw-1b-sft')
os.system('cd /tmp/code/competition_kit/data/models/ && zip -r /tmp/output/sftmodel.zip ./falcon-rw-1b-sft')