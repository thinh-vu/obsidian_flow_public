---
aliases:
  - Database Management in Obsidian
  - Series chia sẻ Obsidian 101
created: "2026-05-02 00:00:00"
progress: active
tags:
  - topic/obsidian
  - topic/database
  - topic/pkm
  - type/moc
summary: "Bản đồ trung tâm (Master MOC) tập hợp tư duy, phương pháp và kỹ thuật để biến Obsidian thành một cơ sở dữ liệu tri thức mạnh mẽ."
---
![[Navigation Bar]]

# Blueprint: Obsidian PKM Mastery

> [!ABSTRACT] Tầm nhìn
> Obsidian không chỉ là một trình soạn thảo văn bản, nó là một **Cơ sở dữ liệu dựa trên tệp (File-based Database)**. Thấu hiểu các quy luật gốc của quản trị dữ liệu và bản chất sinh học của nhận thức giúp bạn xây dựng một hệ thống làm việc thực sự sinh lời.

---

## 📌 Ghi chú nòng cốt (Core Notes)

### 🧠 Trụ cột 1: Khởi nguồn & Định hình tư duy
Tập trung vào việc chẩn đoán những "căn bệnh" lưu trữ thông tin và cung cấp lăng kính nhận thức đúng đắn.
- [[Bạn tìm đến Obsidian vì nỗi đau gì?]]
- [[5 lăng kính định hình phong cách sử dụng Obsidian]]
- [[Giải mã PKM - Những nguyên lý nhận thức định hình mọi hệ thống ghi chú]]
- [Giới thiệu phương pháp FLOW](../Exhibit/Giới%20thiệu%20phương%20pháp%20FLOW.md)

### 🏗️ Trụ cột 2: Các Khái niệm Cơ sở Dữ liệu
Ánh xạ các khái niệm Database vào thế giới Obsidian.
- [[Ghi chú là một Record - Đơn vị dữ liệu nhỏ nhất]]
- [[Metadata là Schema - Quy định cấu trúc cho dữ liệu]]
- [[Primary Key - Tên file và tính duy nhất]]
- [[Wikilinks là Foreign Keys - Kết nối các bảng dữ liệu]]
- [[Structured vs Unstructured Data - Cuộc chiến giữa YAML và Body]]

### ⛓️ Trụ cột 3: Quan hệ, Cấu trúc & Phương pháp
Cách kết nối, bảo vệ tính nhất quán và giải quyết bài toán tư duy ở cấp độ kỹ thuật.
- [[Quan hệ Một-Nhiều và Nhiều-Nhiều trong Obsidian]]
- [[Data Normalization - Tại sao cần Ghi chú Nguyên tử]]
- [[Data Integrity - Giữ cho Metadata luôn sạch và nhất quán]]
- [[Sự khác biệt giữa Tag và Folder dưới góc độ Database]]
- [[Nguyên lý đằng sau việc tạo cấu trúc thư mục trong Obsidian]]
- [[Tạo nhiều wikilink có làm bạn thông minh hơn]]

### 🔍 Trụ cột 4: Truy vấn & Hiển thị
Biến dữ liệu tĩnh thành thông tin động.
- [[Query - Nghệ thuật đặt câu hỏi cho dữ liệu]]
- [[Database View - Hiển thị dữ liệu dưới dạng bảng và danh sách]]
- [[MOC là một Index - Tăng tốc độ truy xuất thông tin]]
- [[CRUD trong Obsidian - Tạo Đọc Cập nhật Xóa]]

---

## 🌊 Hệ thống phương pháp FLOW (The FLOW Methodology)

> [!ABSTRACT] Triết lý FLOW
> PKM không phải là một kho chứa tĩnh, mà là một **Dòng chảy (Flow)**. Tri thức phải di chuyển liên tục từ dạng thô sang tinh để tạo ra giá trị.

### 📌 Các bước trong Dòng chảy

1. **Capture (Thu thập):** Trạm trung chuyển ý tưởng thô. Không được để rác ở lại đây quá lâu.
   - [[Vòng đời của một ghi chú]]
   - [[Quy tắc đặt tên nội dung theo phương pháp FLOW]]
2. **Track (Theo dõi):** Kỷ luật hằng ngày để giữ cho dòng chảy không bị tắc nghẽn.
   - [[Chiến lược sử dụng tag trong phương pháp FLOW]]
3. **Forge (Rèn giũa):** Nơi tư duy nội sinh nảy mầm. Kết nối và đúc kết các ghi chú thô.
   - [[Nguyên tắc áp dụng phương pháp FLOW]]
   - [[Phương pháp quản lý cấu trúc Vault linh hoạt với FLOW]]
   - [[Sử dụng Wikilinks đúng cách trong Obsidian FLOW]]
4. **Blueprint (Bản thiết kế):** Hệ thống MOC và Dashboard để quản lý các dự án tri thức.
   - [[Tuyển chọn nội dung tự động với TOC và Dataview trong hệ thống FLOW]]
   - [[Nguyên tắc quản lý properties trong Obsidian FLOW]]
5. **Exhibit (Trưng bày):** Đầu ra thực tế. Tri thức chỉ thực sự sống khi nó được chia sẻ.
   - [[Sử dụng template note trong phương pháp FLOW]]

---

## 🛠️ Đúc kết (Synthesis)

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - progress == "medium"
    - file.hasLink(this.file.name)
views:
  - type: table
    name: "Synthesis Notes"
    order:
      - file.name
      - summary
```

---

## 📚 Ý tưởng sơ khai (Raw Notes)

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - progress == "raw"
    - file.hasLink(this.file.name)
views:
  - type: list
    name: "Raw Notes"
```
