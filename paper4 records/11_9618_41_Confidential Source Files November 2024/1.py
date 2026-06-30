import os        # 文件、目录、环境变量
import sys       # Python 运行环境
import math      # 数学函数
import random    # 随机数
import datetime  # 日期时间
import json      # JSON 数据
import re        # 正则表达式
import pathlib   # 路径处理
import subprocess # 执行系统命令
import sqlite3   # SQLite 数据库
import logging   # 日志
# import bencodepy
# from pprint import pprint

# with open("Office2021ForMac.torrent", "rb") as f:
#     torrent = bencodepy.decode(f.read())

# info = torrent[b"info"]

# print("announce:")
# print(torrent.get(b"announce", b"").decode(errors="replace"))

# print("\nname:")
# print(info.get(b"name", b"").decode(errors="replace"))

# print("\npiece length:")
# print(info.get(b"piece length"))

# print("\nnumber of pieces:")
# pieces = info.get(b"pieces", b"")
# print(len(pieces) // 20)

# print("\nfiles:")
# if b"files" in info:
#     for file in info[b"files"]:
#         path_parts = [
#             p.decode(errors="replace")
#             for p in file[b"path"]
#         ]
#         print("/".join(path_parts), file[b"length"], "bytes")
# else:
#     print(info.get(b"name", b"").decode(errors="replace"), info.get(b"length"), "bytes")

help(logging)