---
created: "2026-04-29 06:05:00"
progress: medium
blueprint:
  - "[[Obsidian PKM Mastery]]"
tags:
  - topic/database
  - topic/pkm
  - type/synthesis
summary: "Hướng dẫn xây dựng Vault Obsidian theo tư duy quản trị cơ sở dữ liệu để tối ưu hóa khả năng truy xuất và mở rộng."
---

# Xây dựng hệ thống quản lý tri thức như một cơ sở dữ liệu

Ghi chú này đang tổng hợp cách biến các tệp Markdown đơn lẻ thành một hệ thống dữ liệu có cấu trúc và logic.

## 1. Tư duy 'Ghi chú là Dữ liệu'
Để Obsidian hoạt động hiệu quả, ta cần thay đổi cách nhìn:
- Đừng coi ghi chú là một tờ giấy, hãy coi nó là một **Record** trong bảng dữ liệu tri thức của bạn ([[Ghi chú là một Record - Đơn vị dữ liệu nhỏ nhất]]).
- Áp dụng [[Data Normalization - Tại sao cần Ghi chú Nguyên tử]] để tránh trùng lặp thông tin và dễ dàng kết nối chéo thông qua các **Foreign Keys** ([[Wikilinks là Foreign Keys - Kết nối các bảng dữ liệu]]).
- Đảm bảo tính duy nhất thông qua **Primary Key** ([[Primary Key - Tên file và tính duy nhất]]).

## 2. Thiết kế 'Hệ điều hành' tri thức
Một cơ sở dữ liệu tốt cần một hệ điều hành tốt. Trong Vault này, đó là luồng FLOW:
- **Capture:** Là quá trình Input dữ liệu thô.
- **Blueprint:** Là các **Views** hoặc **Indexes** giúp bạn tìm thấy dữ liệu khi cần.
- **Metadata:** Là lớp **Schema** trung gian giúp máy tính (và AI) hiểu được ý nghĩa của ghi chú ([[Metadata là Schema - Quy định cấu trúc cho dữ liệu]]).
- **Bảo toàn dữ liệu:** Áp dụng nguyên tắc [[ACID trong hệ thống file - Bảo vệ tính toàn vẹn tri thức]] để đảm bảo tri thức không bị mất mát do lỗi kỹ thuật.
- **Vòng đời:** Quản lý ghi chú thông qua chu trình [[CRUD trong Obsidian - Tạo Đọc Cập nhật Xóa]].

## 🛠️ Công việc dở dang (WIP)
- [-] Xây dựng bộ quy tắc đặt tên file (Primary Key) nhất quán để tránh xung đột.
- [-] Thử nghiệm việc tạo các 'Bảng' dữ liệu ảo bằng Dataview cho các dự án cụ thể.

---
> [!IMPORTANT]
> Mục tiêu cuối cùng không phải là tạo ra một database phức tạp, mà là tạo ra một hệ thống tự động hóa các công việc lặp lại để bạn tập trung vào việc **Tư duy**.

---

## 📚 Thư viện Quản trị Dữ liệu

```base
filters:
  and:
    - tags.contains("#topic/database")
    - progress == "raw"
views:
  - type: table
    name: "Data Management Captures"
    order:
      - file.name
      - summary
```
