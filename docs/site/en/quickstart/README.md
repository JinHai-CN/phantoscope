# Phantoscope Quick Start
## Prerequisites
Ensure that you have installed Phantoscope in your operating system. See [Install](#README.md)

## Prepare Your Environment
    chmod +x prepare.sh
    ./prepare.sh

## Download Image Package

    curl http://www.vision.caltech.edu/Image_Datasets/Caltech256/256_ObjectCategories.tar -o /tmp/vgg-example.tar

## Upload Image Package
		tar xvf /tmp/vgg-example.tar
		python load_data.py -s 127.0.0.1:5000 -a example -p example /tmp/vgg-example
## Search with the Default Application

    curl --location --request POST '127.0.0.1:5000/v1/application/example/search' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    	"fields": {
            "example": {
                "url": "https://tse2-mm.cn.bing.net/th/id/OIP.C3pWPyFPhBMiBeWoncc24QHaCq?w=300&h=108&c=7&o=5&dpr=2&pid=1.7"
            }
        },
        "topk": 10,
        "nprobe": 20
    }'
