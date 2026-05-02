---
created: "2026-04-29 06:10:00"
progress: medium
blueprint:
  - "[[Obsidian PKM Mastery]]"
tags:
  - topic/database
  - topic/metadata
  - type/synthesis
summary: "Phân tích cách thiết kế metadata và câu lệnh truy vấn để biến Vault thành một thực thể thông minh."
---

# Tối ưu hóa truy vấn và cấu trúc metadata

Làm thế nào để 'nói chuyện' với dữ liệu trong Obsidian một cách hiệu quả nhất?

## 1. Metadata: Cầu nối giữa Người và Máy
Sử dụng [[Metadata là Schema - Quy định cấu trúc cho dữ liệu]] một cách thông minh:
- **Tính nhất quán:** Luôn sử dụng cùng một kiểu định dạng cho metadata (ví dụ: ngày tháng YYYY-MM-DD).
- **Tính tối giản:** Chỉ giữ lại những trường metadata thực sự cần thiết cho việc truy vấn. Quá nhiều metadata sẽ làm loãng [[Structured vs Unstructured Data - Cuộc chiến giữa YAML và Body]].

## 2. Truy vấn: Từ tìm kiếm đến khám phá
Thay vì dùng tính năng Search mặc định, hãy dùng các câu lệnh [[Query - Nghệ thuật đặt câu hỏi cho dữ liệu]].
- Sử dụng **Base Query** để tạo ra các danh mục động trong Blueprint.
- Kết hợp nhiều tiêu chí lọc (AND, OR, NOT) để tìm ra những mối liên hệ ẩn giấu giữa các ghi chú thuộc các Blueprint khác nhau.

## 🛠️ Công việc dở dang (WIP)
- [x] Thiết kế lại hệ thống Tag để tránh bị 'lạm phát Tag'.
- [-] Xây dựng các mẫu Template chuẩn cho từng loại Record (Project, Book, Person...).

---
> [!NOTE]
> Một hệ thống metadata tốt là một hệ thống 'tàng hình' - nó hỗ trợ bạn mà không làm phiền quá trình sáng tác của bạn.
