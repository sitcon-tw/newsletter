# SITCON Newsletter

## 注意事項

1. 請不要使用 CSS3 Selector (bs4 不支援)
2. CSS Selector 該行請以 `{` 結尾，不可分作多行寫（日後改進）
3. CSS Selector 該行結尾只能是空白或是 `{` ，後方不可有 CSS 內容（日後改進）
4. `./make.sh` 後請檢查一次輸出檔案再執行 `./deploy.sh`

## Build Instruciton

``` shell
./make.sh news-test
# Check ./build
./deploy.sh news-test
# Now you are in branch: gh-pages and just add one commit
git push # if you have checked your result
```
