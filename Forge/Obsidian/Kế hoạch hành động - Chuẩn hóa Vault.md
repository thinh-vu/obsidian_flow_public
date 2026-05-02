---
aliases:
  - Lộ trình bảo trì và vận hành Vault
progress: medium
blueprint:
  - "[[Obsidian PKM Mastery]]"
tags:
  - topic/pkm
  - topic/workflow
  - type/action-plan
created: 2026-04-29 05:55:00
---

# 🚀 Kế hoạch hành động: Chuyển hóa và Vận hành Vault

> [!ABSTRACT] Mục tiêu của bài học này
> Tệp này đóng vai trò là một **Action Plan** thực tế, giúp bạn hiểu cách một AI Agent (The Compiler) phân tích và điều phối "dòng chảy" của thông tin để tránh tình trạng tắc nghẽn và quá tải nhận thức.

---

## 1. Phân tích hiện trạng (Vault Audit)

Dưới đây là các cụm tri thức đang ở trạng thái thô (`Capture`) và cần được xử lý theo logic tiến hóa của FLOW.

### 🧪 Nhóm A: Hạt giống cần Tiến hóa (Evolve to Forge)
*Đây là những ghi chú độc lập, có tiềm năng trở thành các thực thể tri thức riêng biệt. Chúng cần được chuyển sang `Forge/` và nâng cấp nội dung.*

```base
filters:
  and:
    - progress == "raw"
    - or:
        - file.hasTag("type/concept")
        - file.name.contains("Tư duy")
        - file.name.contains("Luật")
views:
  - type: table
    name: "Cần nâng cấp lên Medium"
    order:
      - file.name
      - tags
```

### 🗜️ Nhóm B: Nguyên liệu cần Tích hợp (Integrate & Archive)
*Nội dung của những ghi chú này đã hoặc sẽ được "hút" vào các tệp Forge tổng hợp. Sau khi tích hợp, tệp gốc sẽ được đưa vào kho lưu trữ.*

```base
filters:
  and:
    - progress == "raw"
    - or:
        - file.hasTag("topic/fallacy")
        - file.hasTag("topic/bias")
views:
  - type: list
    name: "Sẵn sàng để Archive"
```

---

## 2. Lộ trình thực hiện (The Workflow)

| Bước | Hành động | Logic của FLOW |
| :--- | :--- | :--- |
| **01** | **Xác định cụm (Cluster)** | Tìm những điểm chung giữa các Capture (vd: cùng topic/parenting). |
| **02** | **Đúc kết (Forge)** | Tạo 1 file mới ở `Forge/` hoặc cập nhật file có sẵn. Trích xuất tinh hoa từ Capture đưa vào đây. |
| **03** | **Giải phóng (Release)** | Di chuyển Capture đã dùng vào `Vault/archived`. Không xóa (để bảo toàn nguồn gốc) nhưng không để ở Capture (để giảm nhiễu). |
| **04** | **Bản đồ hóa (Map)** | Đảm bảo file Forge mới được gắn vào ít nhất 1 Blueprint. |

---

## 3. Quản lý các thực thể phi tuyến tính (Canvas & Excalidraw)

> [!IMPORTANT] Quy tắc tổ chức file không phải Markdown
> Đừng phân loại theo **định dạng** (.canvas), hãy phân loại theo **mục đích**.

- **Giai đoạn nháp:** Để tại `Capture/` (Vd: `Brainstorm_Project_X.canvas`)
- **Giai đoạn hệ thống:** Để tại `Blueprint/` (Vd: `Bản đồ tư duy Phật giáo.canvas`)
- **Giai đoạn trình diễn:** Để tại `Exhibit/` (Vd: `Infographic_Climate_Change.excalidraw`)

---

## 🛠️ Trạng thái thực hiện (Live Tracking)

```base
filters:
  and:
    - file.hasTag("type/action-plan")
views:
  - type: table
    name: "Tiến độ bảo trì"
    order:
      - file.name
      - progress
```

---
**Lời nhắn từ AI Agent:** "Hệ thống chỉ mạnh mẽ khi dòng chảy không bị tắc nghẽn. Hãy mạnh dạn Archive những gì đã cũ để nhường chỗ cho những tư duy mới nảy mầm."
