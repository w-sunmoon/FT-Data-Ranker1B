if [ ! -d "data" ]; then
    echo "make new directory data"
    mkdir data
else
    echo "data directory exists"
fi

cd /tmp/code/competition_kit/data

# prepare evaluation data
echo "Preparing evaluation data..."
wget http://dail-wlcb.oss-cn-wulanchabu.aliyuncs.com/dj-competition/eval_data/challenge-data.tar.gz
tar zxvf challenge-data.tar.gz

# prepare base models
echo "Preparing base models..."
mkdir -p models
cd models

echo "Falcon-1B"
wget http://dail-wlcb.oss-cn-wulanchabu.aliyuncs.com/dj-competition/huggingface/falcon-rw-1b.tar.gz
tar zxvf falcon-rw-1b.tar.gz

cd ..

# prepare raw data
echo "Preparing raw datasets..."
mkdir -p raw_data
cd raw_data
wget http://dail-wlcb.oss-cn-wulanchabu.aliyuncs.com/dj-competition/raw_data/raw_data_en.jsonl
wget http://dail-wlcb.oss-cn-wulanchabu.aliyuncs.com/dj-competition/raw_data/raw_data_zh.jsonl

cd -

