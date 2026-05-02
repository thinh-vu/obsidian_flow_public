---
aliases:
  - 8. Quy tắc đặt tên nội dung trong Obsidian FLOW
created: 2024-09-16 23:09:47
progress: medium
blueprint: "[[../Blueprint/Obsidian PKM Mastery|FLOW Methodology]]"
impact: "5"
urgency: 
tags:
  - system/manual
category: 
---
## **Đặt Tên Thư Mục**

> [!hint]
> **Nguyên tắc 7 (+/- 2)**: Giới hạn số lượng thư mục trong mỗi cấp tối đa từ 1-9, đẹp nhất là 7. Điều này giúp giữ cho cấu trúc của Vault dễ quản lý, đảm bảo việc ghi nhớ và duyệt lại nội dung không bị quá tải. Số lượng này tuân theo "quy luật 7" trong nhận thức, một nghiên cứu chỉ ra rằng con người thường chỉ có thể nhớ và xử lý khoảng 7 mục thông tin cùng một lúc.

- **Ngắn gọn và có ý nghĩa**: Tên thư mục cần ngắn gọn, dễ hiểu nhưng đủ sức gợi nhớ chức năng của nó.
- **Dùng danh từ hoặc động từ nhất quán**: Nếu bạn quyết định dùng danh từ (ví dụ: `Library`), hãy nhất quán sử dụng danh từ cho tất cả thư mục khác (ví dụ: `Vault`). Nếu dùng động từ (như `Capture`), hãy đảm bảo tất cả thư mục đều có dạng động từ (ví dụ: `Organize`, `Write`).

## **Đặt Tên File**

### **Đánh số để sắp xếp thứ tự xuất hiện**

Để giữ cho các file luôn được sắp xếp ngăn nắp trong thư mục, hãy sử dụng cấu trúc:

```
THỨ_TỰ + ". " + NỘI_DUNG_CHÍNH + ĐỊNH_DẠNG_FILE
```

Với cách đặt tên này, các file sẽ tự động sắp xếp theo thứ tự bảng chữ cái trong bất kỳ thư mục nào, giúp dễ dàng theo dõi và duyệt qua.

#### **Thứ tự thuận**

Khi các file được tạo ra liên tục và không có yêu cầu sắp xếp lại, các file sẽ có dạng:

```
1. Obsidian Methodology Map.canvas
2. Phương pháp tổ chức thông tin.md
3. Yêu cầu bắt trong cấu trúc Obsidian Vault.md
```

#### **Thứ tự chen ngang (Insert)**

Nếu bạn cần thêm một ghi chú vào vị trí giữa của dãy số đã có, thay vì đổi tên toàn bộ các file sau đó, bạn có thể chèn file mới bằng cách phân nhánh số thứ tự:

- **Phương pháp phân nhánh**: Thêm ký tự chữ cái sau số thứ tự, ví dụ `3a`, để chèn một ghi chú mới mà không làm xáo trộn toàn bộ thứ tự file hiện có. Đây là cách mà [Niklas Luhmann](https://en.wikipedia.org/wiki/Niklas_Luhmann) đã sử dụng trong hệ thống ghi chú Zettelkasten của mình, nơi mỗi ghi chú có thể được mở rộng hoặc bổ sung theo cách phân nhánh logic.

Ví dụ:

```
1. Obsidian Methodology Map.canvas
2. Phương pháp tổ chức thông tin.md
3. Yêu cầu bắt trong cấu trúc Obsidian Vault.md
3a. Cấu trúc mở rộng.md
4. Thiết kế hệ thống ghi chú.md
```

### **Sử dụng ký tự đặc biệt hoặc biểu tượng**

- Bạn có thể thêm các biểu tượng hoặc ký tự đặc biệt (ví dụ: emoji) vào tiêu đề file để làm nổi bật các ghi chú quan trọng hoặc ghi chú thường xuyên sử dụng.
- Ví dụ: `⚡ Quick Capture.md` hoặc `📅 Daily Log 15-09-2024.md`.

## **Làm Nổi Bật Thư Mục và File**

> [!tip] 
> Sử dụng plugin **Iconize** trong Obsidian để thêm biểu tượng (icon) cho thư mục và file. Điều này giúp không gian làm việc trở nên thú vị hơn và giúp bạn dễ dàng nhận diện các nội dung quan trọng.

- **Đặt icon cho các thư mục chính**: Ví dụ, thư mục **Capture** có thể có biểu tượng ✍️, **Forge** có thể là 🔨, **Blueprint** là 📐.
- **Biểu tượng riêng cho file quan trọng**: Bạn có thể gán các biểu tượng khác nhau cho các file dự án chính, để dễ dàng nhận diện chúng chỉ qua cái nhìn đầu tiên.

### **Lưu ý Chung**
- Hãy luôn tuân thủ nguyên tắc đơn giản và nhất quán trong cách đặt tên. Điều này giúp bạn dễ dàng mở rộng và duy trì hệ thống theo thời gian.
- Tránh sử dụng các ký tự đặc biệt có thể gây lỗi khi di chuyển hoặc đồng bộ file trên các hệ thống khác nhau (ví dụ: `/`, `\`, `?`, `*`).

---

Với các hướng dẫn trên, bạn sẽ có một hệ thống tổ chức rõ ràng, trực quan và dễ dàng quản lý theo phương pháp **FLOW**, giúp tối ưu hóa việc ghi chú và phát triển dự án trong Obsidian.