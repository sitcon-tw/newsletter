# SITCON Newsletter

## 注意事項 / Attention

1. 請不要使用 CSS3 selector (bs4 不支援)
2. CSS selector 不可分作多行寫（日後改進）
3. `./make.sh` 後請檢查一次輸出檔案再執行 `./deploy.sh`
4. 沒有測試過 Python 2 ，請用 Python 3



1. DO NOT use CSS3 selector. (Not supported in bs4)
2. DO NOT write CSS selector in multiple lines. (To be improved)
3. Please check the output file after `./make.sh` to make sure that all things are alright and
   then execute `./deploy.sh`
4. Not tested on Python 2, use Python 3

## 相依性 / Dependency

- Python 3
- [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4/4.3.2)
- html5lib
- pystache

### Debian-based Linux

``` shell
sudo apt-get install python3 python3-pip
sudo pip3 install beautifulsoup4 html5lib pystache
```

### OS X

``` shell
# Install dependency on OS X (assume you already have homebrew)
brew install python3
curl https://bootstrap.pypa.io/get-pip.py | python3
pip3 install beautifulsoup4 html5lib pystache
```

### 其他 / Other

- Install Python3
- Install beautifulsoup4
- Install pystache

([pip](https://pip.pypa.io/en/latest/) may be helpful)

## 烹調指南 / Build Instruciton

``` shell
./make.sh news-test
# Check ./build
./deploy.sh news-test
# Now you are in branch: gh-pages and just add one commit
git push # if you have checked your result
```
