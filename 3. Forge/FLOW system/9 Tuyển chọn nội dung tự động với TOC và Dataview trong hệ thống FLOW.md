---
aliases:
  - 92. Tuyển chọn nội dung tự động với TOC và Dataview trong hệ thống FLOW
created: 2024-09-16 23:09:24
status: done
blueprint:
  - "[[../../4. Blueprint/Obsidian FLOW Methodology|Obsidian FLOW Methodology]]"
impact: "5"
urgency: 
tags:
  - user-manual
category: 
---

Trong hệ thống **FLOW**, việc tổ chức thông tin không chỉ dừng lại ở việc sử dụng các thư mục (folders), mà còn bao gồm cả việc tạo ra các bản đồ nội dung với Blueprint[^1] để bạn dễ dàng điều hướng qua các ghi chú, dự án và chủ đề phức tạp. **Blueprint** có thể được sử dụng làm tấm bản đồ nội dung cho từng dự án, thư mục cụ thể, giúp bạn có cái nhìn tổng quan và quản lý thông tin một cách hiệu quả.

Bằng cách tận dụng **Dataview** plugin trong Obsidian, bạn có thể tự động tạo và cập nhật TOC dựa trên các thuộc tính metadata của từng ghi chú, như **status**, **impact**, **urgency**, và các thuộc tính khác. Điều này giúp bạn không cần phải chọn thủ công từng ghi chú, mà chỉ cần điều chỉnh metadata để tự động hiển thị chúng trong TOC.

---

## **Tạo Blueprint cho Vault hoặc Dự Án**

Một **Blueprint** đóng vai trò như "bản vẽ" khi bạn xây dựng một công trình, ở đây chính là những mục tiêu của bạn khi thực hiện trong toàn bộ Vault hoặc cho một thư mục/dự án cụ thể. Bạn có thể tạo **Blueprint** cho toàn Vault, riêng biệt cho từng dự án hoặc thư mục bất kỳ. Blueprint sẽ cung cấp một không gian tổng quan để dễ dàng truy cập vào các ghi chú liên quan mà không cần "đỏ mắt" duyệt qua từng thư mục.
### **1. Tạo Blueprint cho Vault**

#### **Bước 1: Tạo file Blueprint**

- Tạo một file ghi chú mới, ví dụ: **TOC.md** hoặc **Home.md**. Trong Vault này, tôi lựa chọn tên gọi TOC.md để thể hiện ngắn gọn nó là ghi chú chứa các nội dung tổng hợp.
- Đây sẽ là "nhà" cho toàn bộ Vault, nơi bạn có thể điều hướng nhanh qua các dự án, ghi chú quan trọng.
#### **Bước 2: Sử dụng Dataview để liệt kê các ghi chú theo trạng thái**

- Trong TOC.md, sử dụng **Dataview Query** để tự động liệt kê các ghi chú dựa trên thuộc tính metadata. Ví dụ: Bạn có thể hiển thị tất cả các ghi chú có trạng thái `medium` (đang phát triển) hoặc những ghi chú `done` (hoàn thành).

```dataview
table status, impact, urgency
from ""
where status = "medium" or status = "done"
sort urgency desc
```

- Lệnh trên sẽ liệt kê tất cả các ghi chú trong Vault có trạng thái là `medium` hoặc `done`, sắp xếp chúng theo độ cấp bách **urgency** từ cao xuống thấp.

### **2. Tạo TOC cho một dự án hoặc thư mục cụ thể**

#### **Bước 1: Tạo Blueprint cho dự án**

- Tạo một file ghi chú mới trong thư mục dự án, ví dụ: **Project X Map.md** hoặc **Dự Án Y.md**. Đây sẽ là nơi bạn điều hướng giữa các ghi chú thuộc về dự án cụ thể đó.

#### **Bước 2: Sử dụng Dataview để tự động hiển thị ghi chú liên quan**

- Trong TOC này, bạn có thể sử dụng **Dataview Query** để liệt kê các ghi chú thuộc dự án dựa trên metadata như **parent**, **status**, và **priority**.

```dataview
table status, priority, updated
from "/"
where file.folder = "3. Forge/FLOW system" and status != "archived"
sort priority asc, updated desc
```

- Câu lệnh trên sẽ liệt kê tất cả các ghi chú trong thư mục **3. Forge/FLOW system** có địa chỉ thư mục là "3. Forge/FLOW system" (để đảm bảo chỉ hiển thị ghi chú liên quan), loại bỏ các ghi chú đã được lưu trữ (`archived`) và sắp xếp chúng theo thứ tự ưu tiên **priority** từ thấp đến cao.

### **3. Tạo TOC dựa trên các tiêu chí khác như impact hoặc urgency**

- Bạn cũng có thể linh hoạt điều chỉnh các thuộc tính khác của metadata, chẳng hạn như **impact** hoặc **urgency** để tạo ra các danh sách ghi chú dựa trên mức độ quan trọng, độ khẩn cấp, hoặc trạng thái phát triển.

Ví dụ, TOC liệt kê ghi chú có **urgency** cao trước:

```dataview
table status, urgency, updated
from "Forge"
where urgency >= 5
sort urgency desc, updated desc
```

- Câu lệnh này sẽ liệt kê tất cả các ghi chú trong **Forge** có độ cấp bách từ 5 trở lên, sắp xếp theo mức độ khẩn cấp và ngày cập nhật mới nhất.

## **Sử dụng TOC để Quản lý Dự Án Hiệu Quả**

TOC không chỉ giúp bạn điều hướng qua các ghi chú mà còn đóng vai trò quản lý các dự án một cách hiệu quả. Việc tự động cập nhật TOC dựa trên metadata giúp bạn dễ dàng nắm bắt tiến trình, mức độ ưu tiên, và tình trạng phát triển của từng ghi chú, dự án mà không cần phải lục tung Vault để tìm kiếm.

- **Sắp xếp công việc theo mức độ ưu tiên**: Sử dụng metadata **priority** hoặc **urgency** để hiển thị các ghi chú cần làm trước. Điều này giúp bạn luôn tập trung vào những công việc quan trọng nhất.
  
- **Theo dõi tiến độ dự án**: Metadata **status** giúp bạn biết được ghi chú nào đang phát triển, đã hoàn thành, hoặc cần lưu trữ.

## **Tối Ưu Hóa Blueprint trong Vault của bạn**

### **Linh hoạt nhưng có cấu trúc**

Blueprint trong **FLOW** giúp bạn kết hợp giữa sự linh hoạt và cấu trúc vững chắc. Bằng cách sử dụng các thư mục để quản lý cấp độ cao và **Dataview** để tự động hóa việc tổ chức, bạn có thể duy trì Vault của mình một cách gọn gàng và có tổ chức, trong khi vẫn đảm bảo khả năng điều chỉnh nhanh chóng theo sự thay đổi của thông tin và dự án.

### **Tiết kiệm thời gian và công sức**

Thay vì phải cập nhật thủ công các danh sách trong TOC, bạn chỉ cần điều chỉnh metadata của từng ghi chú. Điều này giúp hệ thống luôn cập nhật theo thời gian thực, tiết kiệm thời gian và công sức.

### **Lời Kết**

Blueprint là một công cụ mạnh mẽ khi sử dụng trong Obsidian FLOW, đặc biệt khi kết hợp với **Dataview** để tự động hóa việc tổ chức. Với **FLOW**, bạn không chỉ tạo ra một hệ thống linh hoạt, dễ dàng điều hướng, mà còn giúp đảm bảo thông tin luôn được cập nhật và tổ chức một cách khoa học.

[^1]: Blueprint tương đương với các khái niệm bạn có thể nghe từ trước như TOC - Table of Content hay **MOC** - Map of Contents