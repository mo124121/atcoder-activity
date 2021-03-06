#!/usr/bin/env python3

# https://github.com/paruma/atcoder_rust/blob/main/contest.py
# example
# ./contest.py abc206 b c

import sys
import os
import shutil

if len(sys.argv) <= 2:
    print("usage  : ./contest.py [contest_name] [task_name_list]", file=sys.stderr)
    print("example: ./contest.py abc206 b c", file=sys.stderr)
    sys.exit(1)


contest_name: str = sys.argv[1]
problems = sys.argv[2:]

RUST_PATH = "rust"
# ソースコードの準備(ディレクトリの生成)
dir_path: str = f"{RUST_PATH}/src/contest/{contest_name}/"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# ソースコードの準備(ファイルのコピー)
templete_file_path: str = f"{RUST_PATH}/src/contest/template.rs"
for problem in problems:
    dst_file_path = (
        f"{RUST_PATH}/src/contest/{contest_name}/{contest_name}_{problem}.rs"
    )
    if not os.path.exists(dst_file_path):
        shutil.copy(templete_file_path, dst_file_path)


# cargo.tomlコードの出力
with open(f"{RUST_PATH}/Cargo.toml", "a") as f:
    for problem in problems:
        f.write(
            f"""
[[bin]]
name = "{contest_name}_{problem}"
path = "src/contest/{contest_name}/{contest_name}_{problem}.rs"

"""
        )
