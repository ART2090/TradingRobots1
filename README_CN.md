# 🚀 Go Quant Trading Platform
一个基于hyperliquid的量化交易机器人，用Go语言编写的高性能加密货币量化交易系统。
一个使用 Go 构建的 **实时交易 + 策略引擎 + 回测 + 数据中心 + 盈利监控** 的量化交易系统。
支持全币种监控、动态盈利锁定、订单追踪、历史数据存储与分析。

---

## ✨ Features
- **实时盈利监控**：首页展示账户实时盈亏、持仓、收益曲线
- **订单追踪系统**：用户输入参数后自动监控全币种行情并触发下单
- **动态盈利锁定**：根据用户设置自动跟踪价格并锁定利润
- **全币种行情中心**：实时保存价格、未平仓量、成交额、资金费率等
- **历史数据存储**：为回测、策略优化、开仓计划提供数据基础
- **模块化策略引擎**：可插拔策略、支持多策略并行
- **事件驱动架构**：goroutine + channel 实现高性能异步处理
- **风险控制模块**：止损、止盈、仓位管理
- **可视化配置页面**：用户可自定义策略参数、风控参数、交易所设置

---

## 🏗️ Architecture Overview
系统采用分层架构，包含实时交易、数据中心、策略引擎、风控、监控等核心模块。

```
cmd/
internal/
  core/            # 核心事件总线
  exchange/        # 交易所 API 封装
  strategy/        # 策略模块
  tracker/         # 订单追踪系统
  profitlock/      # 动态盈利锁定模块
  datacenter/      # 全币种行情中心 + 历史数据存储
  dashboard/       # 实时盈利监控
  risk/            # 风控模块
  storage/         # 数据库
  utils/           # 工具函数
configs/
docs/
scripts/
```

---

## 📊 Core Modules
### **1. 实时盈利监控（Dashboard）**
- 展示账户实时盈亏
- 展示持仓、收益曲线、策略表现
- 支持多交易所、多币种

### **2. 订单追踪系统（Order Tracker）**
- 用户输入参数（价格区间、触发条件、交易量等）
- 系统实时监控全币种行情
- 条件满足时自动下单
- 支持多策略并行监控

### **3. 动态盈利锁定（Profit Lock）**
- 根据用户设置的参数自动跟踪价格
- 动态调整止盈点
- 防止利润回吐
- 类似“移动止盈（Trailing Take Profit）”但更智能

### **4. 全币种行情中心（Market Data Center）**
- 实时抓取全币种行情
- 保存：
  - **价格走势**
  - **未平仓量（Open Interest）**
  - **24h 成交额**
  - **资金费率（Funding Rate）**
- 提供历史数据用于：
  - 策略优化
  - 回测
  - 开仓计划

### **5. 策略引擎（Strategy Engine）**
- 可插拔策略
- 支持多策略并行
- 支持实时交易 + 回测复用同一套逻辑

---

## 📦 Project Structure
- **cmd/**：主程序入口
- **internal/core**：事件总线、调度器
- **internal/exchange**：交易所 API 抽象层
- **internal/strategy**：策略模块
- **internal/tracker**：订单追踪系统
- **internal/profitlock**：动态盈利锁定
- **internal/datacenter**：行情中心 + 历史数据
- **internal/dashboard**：实时盈利监控
- **internal/risk**：风控模块
- **internal/storage**：SQLite3 或其他数据库
- **configs/**：配置文件
- **docs/**：架构文档、策略说明
- **scripts/**：启动脚本、部署脚本

---

## 🚀 Quick Start
```
git clone https://github.com/ART2090/TradingRobots1.git
cd TradingRobots1
cp configs/config.example.yaml configs/config.yaml
go run cmd/trader/main.go
```

---

## 🧪 Example Strategies
- **Moving Average Crossover**
- **Grid Trading**
- **Momentum Strategy**

---

## ⚠️ Security & Disclaimer
请勿上传任何敏感信息：

- **API Key / Secret**
- **私钥 / 助记词**
- **真实交易记录**
- **真实策略参数**
- **可直接盈利的核心策略逻辑**

本项目仅用于学习与研究。

---

## 🗺️ Roadmap
- **Web Dashboard**（实时可视化）
- **更多交易所支持**
- **策略可视化工具**
- **回测性能优化**

---

## 👤 About the Author
Golang developer focusing on:

- **高性能系统设计**
- **量化交易系统**
- **跨平台工程化实践**
