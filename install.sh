cd /tmp/code/competition_kit/
pip install git+https://github.com/HYLcool/simhash-py.git

# for training
cd lm-training
pip install -r requirements.txt
cd ..

# for evaluation
cd lm-evaluation-harness
pip install -e .
cd ..


# for data-juicer
git clone https://openi.pcl.ac.cn/wsunmoon/data-juicer.git
cd data-juicer
pip install -v -e .[all]
