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

os.system('apt-get update -y')
os.system('apt-get install git -y')

os.system('cd /tmp/code')
os.system("wget http://dail-wlcb.oss-cn-wulanchabu.aliyuncs.com/dj-competition/competition_kit.zip")
os.system('unzip -d /tmp/code/ competition_kit.zip')


os.system('rm -rf /tmp/code/competition_kit/install.sh')
os.system('rm -rf /tmp/code/competition_kit/prepare_data_and_models.sh')
os.system('cp -r /tmp/code/install.sh /tmp/code/competition_kit/')
os.system('cp -r /tmp/code/prepare_data_and_models.sh /tmp/code/competition_kit/')
os.system('cd /tmp/code/competition_kit && sh install.sh')
os.system('cd /tmp/code/competition_kit && sh prepare_data_and_models.sh')


os.system('mkdir -p /tmp/code/results')
os.system('rm -rf /tmp/code/competition_kit/data-juicer/configs/data_juicer_recipes/alpaca_cot/alpaca-cot-en-refine.yaml')
os.system('rm -rf /tmp/code/competition_kit/data-juicer/configs/data_juicer_recipes/alpaca_cot/alpaca-cot-zh-refine.yaml')
os.system('cp -r /tmp/code/alpaca-cot-en-refine.yaml /tmp/code/competition_kit/data-juicer/configs/data_juicer_recipes/alpaca_cot/')
os.system('cp -r /tmp/code/alpaca-cot-zh-refine.yaml /tmp/code/competition_kit/data-juicer/configs/data_juicer_recipes/alpaca_cot/')
# 修改相关参数
os.system('cd /tmp/code/competition_kit/data-juicer && python tools/process_data.py --config configs/data_juicer_recipes/alpaca_cot/alpaca-cot-en-refine.yaml')
os.system('cd /tmp/code/competition_kit/data-juicer && python tools/process_data.py --config configs/data_juicer_recipes/alpaca_cot/alpaca-cot-zh-refine.yaml')


os.system('rm -rf /tmp/code/competition_kit/lm-training/get_train_dataset_1b.py')
os.system('cp -r /tmp/code/get_train_dataset_1b.py /tmp/code/competition_kit/lm-training/')
# 修改相关参数
os.system('cd /tmp/code/competition_kit/lm-training && python get_train_dataset_1b.py')