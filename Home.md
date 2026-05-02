![[Navigation Bar]]

> [!abstract] 🌊 FLOW VAULT
> Chào mừng bạn đến với nhà máy tri thức cá nhân. Sử dụng thanh điều hướng phía trên hoặc các bảng tóm tắt bên dưới để bắt đầu.

## 📌 TRUY CẬP NHANH
- [[Content Plan]]: Quản lý nội dung & xuất bản.
- [[Obsidian PKM Mastery]]: Hướng dẫn & phương pháp hệ thống.
- [[Reading Challenges]]: Thư viện sách & lộ trình đọc.
- [[CHANGELOG]]: Lịch sử cập nhật Vault.

---

## 📥 Ý TƯỞNG MỚI
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - or:
      - file.inFolder("Capture")
      - '!note.progress'
views:
  - type: table
    name: "Inbox"
    limit: 5
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
```

---

## 🔥 ĐIỂM NÓNG
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - impact >= 5
views:
  - type: table
    name: "Hot"
    limit: 3
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - summary
```

---
> [!tip] Mẹo
> Mọi chi tiết vận hành chuyên sâu đã có tại **FLOW Dashboard** (Tự động mở khi khởi động Vault).