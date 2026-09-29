# GitHub SSH 配置（国内网络，走 443 端口）

## 背景

国内网络直连 GitHub 的 HTTPS（443）经常被重置，SSH 默认的 22 端口也常被封锁。
解决方案：**用 SSH over 443**，把 SSH 流量伪装成 HTTPS 流量。

## 一次性配置

### 1. 生成密钥（如果已有可跳过）

```bash
ssh-keygen -t ed25519 -C "你的GitHub邮箱"

```

### 2. 添加公钥到GitHub

```bash
cat ~/.ssh/id_ed25519.pub | clip
```
GitHub 网页 -> 右上角头像 -> Settings -> SSH and GPG keys -> New SSH key
Title: 随便写 ， 如 Winddows Dell
Key: 粘贴公钥内容

### 3. 配置 ~/.ssh/config
在~/.ssh/下新建config文件 （无后缀），内容：
```text
Host github.com
  HostName ssh.github.com
  User git
  Port 443
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```
逐行含义：

Host github.com：匹配规则，连接 github.com 时生效

HostName ssh.github.com：实际连接的地址

User git：GitHub SSH 固定用户名

Port 443：走 HTTPS 端口，绕过 22 端口封锁

IdentityFile：指定用哪个私钥

IdentitiesOnly yes：只用指定密钥，避免认证次数超限


### 4. 测试连接
```bash
ssh -T git@github.com
```
成功输出：

text
Hi 你的用户名! You've successfully authenticated, but GitHub does not provide shell access.

### 5.把仓库地址改为SSH
```bash
git remote set-url origin git@github.com:用户名/仓库名.git
```
验证：
```bash
git remote -v
```
应该显示 git@github.com:... 开头。


### 关键点
一次配置，全局生效。以后所有 GitHub 仓库都走 SSH，不用重复配置。

私钥 id_ed25519 绝对不能泄露或上传到任何地方。

### 测试
先确认代理真的关了。如果你之前给 Git 配过代理，先检查并取消：

```bash
git config --global --get http.proxy
git config --global --get https.proxy
````
如果有输出，说明还配着代理，取消掉：
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```
然后测试 SSH 连接
```bash
ssh -T git@github.com
```
期望结果：

```text
Hi landlordsdream! You've successfully authenticated, but GitHub does not provide shell access.
```

然后测试实际推送
先做一个小的改动，比如修改 setup-ssh-github.md 里的一个标点，或者建一个临时文件，然后：

```bash
git add .
git commit -m "test: verify SSH push without proxy"
git push
```
期望结果：推送成功，没有 Connection was reset 或超时。

如果测试成功
说明你彻底摆脱了代理依赖。以后：

关不关代理都能 push

换网络（家里、公司、热点）大概率也能 push

不用再担心代理过期