# 更新所有包到最新版本
```bash
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```

# 导出所有包的版本信息
```bash
pip freeze > requirements.txt
```

# 安装导出版本文件中的所有包
```bash\
pip install -r requirements.txt
```

