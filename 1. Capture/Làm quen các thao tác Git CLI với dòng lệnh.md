---
aliases:
  - Làm quen các thao tác Git CLI với dòng lệnh
created: 2024-09-19 06:09:48
status: raw
blueprint: 
impact: 
urgency: 
tags: 
category:
---
# Thiết lập Git

- Xem tất cả thông tin thiết lập cho Git hiện tại: `git config --list --show-origin` hoặc `git config --list`
- Đặt tên nhánh chính là main: `git config --global init.defaultBranch main`

# Khởi tạo Git
- Từ cmd mở thư mục cần quản lý phiên bản với Git, dùng dòng lệnh để kích hoạt `git init`
# Clone 1 repo bất kỳ

- Sử dụng câu lệnh `git clone https://github.com/libgit2/libgit2`
- Nếu lưu repo vào 1 thư mục có tên khác với tên của repo: `git clone https://github.com/libgit2/libgit2 mylibgit`
# Xem trạng thái git

- Sử dụng câu lệnh: `git status`
# Thêm 1 file vào danh sách theo dõi

- Sử dụng lệnh `git add README`
- Sử dụng câu lệnh short để trả về trạng thái vắn tắt: `git status -s`
# Ignore

Loại trừ 1 file bất kỳ để bỏ theo dõi
```
cat .gitignore
*.[oa]
*~
```
Trong đó: 
- `*.[oa]` giúp loại bỏ tất cả file có đuôi `.o` hay `.a`.
- `*~` giúp loại bỏ các file có chứa ký tự `~` là các file tạm được tạo ra bởi text editor.

Nguyên tắc:
- Dòng trống hoặc bắt đầu với # bị bỏ qua

Ví dụ
```
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

# Xem lịch sử thay đổi trong file

- Sử dụng lệnh `git diff`