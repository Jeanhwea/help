# 查找并批量拉取git远程仓库数据
```sh
for dotgit in `find $(pwd) -type d -name '.git'`; do cd $dotgit/.. && pwd && git pull ; done
```
