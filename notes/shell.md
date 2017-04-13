# 查找并批量拉取git远程仓库数据
```sh
for dotgit in `find $(pwd) -name '.git'`; do cd $dotgit && cd .. && pwd && git pull ; done
```
