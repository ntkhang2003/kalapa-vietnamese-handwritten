import argparse
from test import correct
from PIL import Image
import os
import csv

from vietocr.vietocr.tool.predictor import Predictor
from vietocr.vietocr.tool.config import Cfg

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_test', help='folder contain images to read')
    parser.add_argument('--config', type=str, default='config/config.yml')
    parser.add_argument('--device', type=str, default='cuda:0', help='cuda:0 or cpu')
    parser.add_argument('--weight_path', type=str, default='weights/transformer_ocr.pth')
    args = parser.parse_args()
    return args
def main():
    args = parse_args()
    device = args.device
    weight_path = args.weight_path
    config = args.config
    dir_test = args.dir_test

    config = Cfg.load_config_from_file(config)
    config['weights'] = weight_path
    config['device'] = device
    detector = Predictor(config)

    result = {}

    for filename in os.listdir(dir_test):
        img_path = os.path.join(dir_test, filename)
        img = Image.open(img_path)
        answer = detector.predict(img, return_prob=False)
        result[img_path] = answer

    fields = ['id', 'answer']
    with open('result.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for id, answer in result.items():
            writer.writerow([id, answer])

if __name__ == "__main__":
    main()