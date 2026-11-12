# network-automation

网络运维自动化练习集 —— 用 Python 处理日常重复工作。

## 脚本

| 文件 | 作用 |
|---|---|
| `lesson4.py` | 读取设备清单，批量生成配置备份命令 |

## 快速开始

1. 安装 Python 3.10 或更高版本
2. 准备 `devices.txt`，每行一台设备，格式为 `设备名 空格 IP`：

```
SW1 10.1.1.1
SW2 10.1.1.2
R1 10.1.1.254
```

3. 运行脚本：

```bash
python lesson4.py
```

4. 结果打印到屏幕，同时写入 `backup_commands.txt`

## 示例输出

```
backup 10.1.1.1 配置到 SW1.cfg
backup 10.1.1.2 配置到 SW2.cfg
backup 10.1.1.254 配置到 R1.cfg
共 3 台设备，已写入 backup_commands.txt
```

## 环境

- Python 3.10+
- 无第三方依赖

## 说明

个人学习项目，用于练习 Python 基础语法：文件读写、字符串处理、函数、循环。

文中设备地址均为 RFC 5737 / RFC 3849 示例地址，不代表任何真实网络。

## 更新记录

- 2026-11-12 首次上传，完成备份命令生成器
