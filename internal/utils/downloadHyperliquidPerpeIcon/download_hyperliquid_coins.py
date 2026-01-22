#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hyperliquid 官方币种图标批量下载器
图标地址: https://app.hyperliquid.xyz/coins/{symbol}.svg
数据来源: https://api.hyperliquid.xyz/info (type: "meta")
"""

import requests
import os
import time
from tqdm import tqdm
import sys

# ================== 配置区 ==================
OUTPUT_DIR = "hyperliquid_coins"      # 下载保存文件夹
ICON_BASE_URL = "https://app.hyperliquid.xyz/coins/{}.svg"
API_URL = "https://api.hyperliquid.xyz/info"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Content-Type": "application/json"
}
DELAY = 0.1  # 请求间隔（秒），避免触发限流
TIMEOUT = 10
RETRIES = 3
# ===========================================

def get_all_symbols():
    """从官方 meta 接口获取所有币种名称（永续 + 现货）"""
    payload = {"type": "meta"}
    for attempt in range(RETRIES):
        try:
            response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=TIMEOUT)
            if response.status_code == 200:
                data = response.json()
                symbols = set()

                # 1. 永续合约：universe[].name
                for asset in data.get("universe", []):
                    if "name" in asset:
                        symbols.add(asset["name"])

                # 2. 现货市场：spotMeta[].tokens[] 中的 name 或 tokenName
                for pair in data.get("spotMeta", {}).get("universe", []):
                    for token in pair.get("tokens", []):
                        name = token.get("name") or token.get("tokenName")
                        if name:
                            symbols.add(name)

                print(f"获取到 {len(symbols)} 个币种符号")
                return sorted(symbols)
        except Exception as e:
            print(f"第 {attempt + 1} 次请求 meta 失败: {e}")
            time.sleep(2)
    print("获取币种列表失败，请检查网络或 API 是否可用")
    sys.exit(1)


def download_icon(symbol, save_path):
    """下载单个图标，支持重试"""
    url = ICON_BASE_URL.format(symbol)
    for attempt in range(RETRIES):
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)
                return True, "成功"
            elif response.status_code == 404:
                return False, "404 不存在"
            else:
                return False, f"HTTP {response.status_code}"
        except Exception as e:
            if attempt == RETRIES - 1:
                return False, f"异常: {e}"
            time.sleep(0.5)
    return False, "重试失败"


def main():
    print("正在获取 Hyperliquid 全部币种列表...")
    symbols = get_all_symbols()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"开始下载图标 → 保存至: {os.path.abspath(OUTPUT_DIR)}")

    success = 0
    failed = 0
    skipped = 0

    # 使用 tqdm 进度条，美观专业
    for symbol in tqdm(symbols, desc="下载进度", unit="个"):
        save_path = os.path.join(OUTPUT_DIR, f"{symbol}.svg")
        
        # 如果已经下载过，跳过（支持增量更新）
        if os.path.exists(save_path):
            skipped += 1
            continue

        ok, msg = download_icon(symbol, save_path)
        if ok:
            success += 1
        else:
            if "404" in msg:
                failed += 1  # 404 算失败但常见
            else:
                print(f"\n{symbol} 下载失败: {msg}")
                failed += 1

        time.sleep(DELAY)  # 友好访问

    print("\n" + "="*50)
    print("下载完成！")
    print(f"成功: {success} 个")
    print(f"已存在跳过: {skipped} 个")
    print(f"失败/无图标: {failed} 个")
    print(f"全部图标保存在: {os.path.abspath(OUTPUT_DIR)}")
    print("="*50)


if __name__ == "__main__":
    main()
