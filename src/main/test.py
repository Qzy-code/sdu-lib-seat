import logging
import os
import sys
import time
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--userid', type=str, help='山东大学学号')
    parser.add_argument('--passwd', type=str, help='山东大学统一身份认证密码')
    paras = parser.parse_args()
    logging.basicConfig(format='%(asctime)s  %(filename)s : %(message)s',
                        level=logging.INFO, stream=sys.stdout)
    logging.info(paras.userid)
    time.sleep(30)
    logging.info(paras.passwd)
