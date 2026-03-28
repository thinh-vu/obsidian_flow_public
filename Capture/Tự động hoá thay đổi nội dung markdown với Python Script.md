---
aliases: 
created: 2024-09-30 23:21:00
progress: raw
blueprint: 
impact: 5
urgency: 0
tags:
  - advanced
  - automation
category:
---


> [!tip]
> Bạn có biết trong vault mẫu chứa các file script python giúp bạn xử lý nội dung markdown trong những trường hợp bất khả kháng mà có thể sẽ cực kỳ mất công hoặc bỏ cuộc nếu bạn gặp phải?

Vault mẫu Obsidian FLOW chứa các đoạn script python hữu ích tại thư mục `6. Vault/scripts` bao gồm
1. ` replace_md_text.py`: Thay thế 1 đoạn văn bản bất kỳ trong tất cả các file markdown thuộc thư mục chỉ định với đoạn văn bản mới. Hình 1
2. `update_properties_time_format.py`: Cập nhật định dạng dấu thời gian trong properties của ghi chú trong thư mục được chỉ định, áp dụng với cả thư mục con. Trường hợp này mình viết để sửa đổi định dạng Việt Nam (30-09-2024) sang định dạng chuẩn Thế giới (2024-09-30).
3. `yaml_add_field_tkinter_ui.py`: Giao diện đồ hoạ đơn giản cho phép lựa chọn thư mục ghi chú để sửa đổi hoặc bổ sung giá trị properties. Hình 2.

*(\*) Trong mỗi file có câu lệnh mẫu. Để biết cách cài đặt Python, vui lòng xem hướng dẫn tại [Vnstock](https://vnstocks.com/docs/khoa-hoc/python-cho-cong-cong-khoa-hoc-mien-phi) hoặc [Learn Anything](https://learn-anything.vn/kien-thuc/python/thiet-lap-moi-truong-python)*

Hình 1:
![](../6.%20Vault/attachments/run_python_script_in_visual_studio_code.png)

Hình 2:
![](../6.%20Vault/attachments/modify_markdown_yaml_front_matter.png)