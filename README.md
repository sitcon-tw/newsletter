# SITCON Newsletter

## 注意事項

1. 請不要使用 CSS3 Selector (bs4 不支援)
2. CSS Selector 該行請以 `{` 結尾，不可分作多行寫（日後改進）
3. CSS Selector 該行結尾只能是空白或是 `{` ，後方不可有 CSS 內容（日後改進）
4. `./make.sh` 後請檢查一次輸出檔案再執行 `./deploy.sh`
5. 沒有測試過 Python 2 ，請用 Python 3

## Dependency

- Python 3
- [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4/4.3.2)
- html5lib
- pystache

### Debian-based Linux

``` shell
sudo apt-get install python3 python3-pip
sudo pip3 install beautifulsoup4 html5lib pystache
```

### For OS X

``` shell
# Install dependency on OS X (assume you already have homebrew)
brew install python3
curl https://bootstrap.pypa.io/get-pip.py | python3
pip3 install beautifulsoup4 html5lib pystache
```

### Other

- Install Python3
- Install beautifulsoup4
- Install pystache

([pip](https://pip.pypa.io/en/latest/) may be helpful)

## Build Instruciton

``` shell
./make.sh news-test
# Check ./build
./deploy.sh news-test
# Now you are in branch: gh-pages and just add one commit
git push # if you have checked your result
```
