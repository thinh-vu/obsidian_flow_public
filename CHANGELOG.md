# Nhật ký cập nhật FLOW Vault

## [2026-05-01] Tối giản hệ thống, Tối đa dòng chảy

Trong bản cập nhật này, tôi đã thực hiện một đợt tối ưu toàn diện Vault. Mục tiêu: Trả hệ thống về đúng bản chất của phương pháp FLOW, tập trung vào kiến tạo tri thức thay vì cài cắm và duy trì plugin.

### Thiết lập mặc định: Khởi động với FLOW Dashboard
Từ nay, **hành động mặc định khi mở Vault** đã được thiết lập để tự động mở **FLOW Dashboard (Home)**. 
- Thay vì phải dựa dẫm vào thanh Sidebar (cây thư mục) vốn dễ gây rối mắt và phân tâm, Dashboard sẽ cung cấp cho bạn cái nhìn tổng quan ngay lập tức về "sức khoẻ" của Vault (tiến độ công việc, các ghi chú đang xử lý, streaks).
- Việc điều hướng nhanh chóng tới các module quan trọng có thể thực hiện trực tiếp từ **"Bảng nội dung" (Navigation)** ngay trong Dashboard một cách tập trung và hiệu quả hơn.

## 1. FLOW PKM Plugin: Đưa mọi thứ về một mối

Trước đây, để quản lý nhiệm vụ, bạn phải dùng kết hợp nhiều plugin rườm rà. Hệ quả là bộ nhớ làm việc bị quá tải khi phải liên tục chuyển đổi giữa các ngữ cảnh và giao diện khác nhau.

**Cập nhật mới:**
- FLOW PKM Plugin giờ đây đã được tích hợp sẵn tính năng quản lý nhiệm vụ. 
- Toàn bộ tiến độ và công việc của bạn được tự động tổng hợp và hiển thị trực quan ngay trên FLOW Dashboard.
- Không cần dùng app bên thứ 3, không cần thiết lập lằng nhằng. Mọi thứ vận hành một cách liền mạch từ bước lên ý tưởng đến thực thi.

## 2. Giao diện Borderism: Tinh gọn, Hiệu suất cao

Một giao diện tốt không phải là giao diện rực rỡ nhất, mà là giao diện giúp bạn ít bị phân tâm nhất. Đó là lý do tôi tuỳ biến và áp dụng theme **Borderism** cho FLOW Vault.

Đây là sự kết hợp có chủ đích từ hai theme xuất sắc:
- **Từ Border:** Kế thừa giao diện tinh gọn, cắt bỏ các viền (border) và chi tiết thừa, tối ưu không gian hiển thị.
- **Từ Prism:** Giữ lại hệ thống Admonition sắc nét và typography trình bày chuẩn mực. Cấu trúc font chữ được thiết kế để không chỉ đẹp trên màn hình mà còn hỗ trợ in ấn xuất bản cực kỳ tốt.

## 3. Lược bỏ sự phù phiếm

Tri thức chỉ phát huy sức mạnh khi các ghi chú được kết nối với nhau, không phải từ việc bạn cài bao nhiêu công cụ. Càng ít plugin, độ trễ càng thấp, tư duy càng sắc bén. Tôi đã quyết định loại bỏ hoàn toàn các plugin sau khỏi Vault:

- **Dataview:** Đã được thay thế hoàn toàn bằng **Obsidian Base Plugin**. Tốc độ truy xuất nhanh hơn, ổn định hơn. Toàn bộ các block query trong các file mẫu (template, blueprint) đã được tôi chuẩn hoá lại cú pháp.
- **Obsidian Projects & Tasks Calendar Wrapper:** Đã được thay thế hoàn toàn, vì FLOW PKM Plugin hiện tại đã tích hợp tính năng quản lý công việc và thời gian tiện lợi hơn rất nhiều.
- **Linting & Obsidian Reminder:** Các tính năng tự động này thường tạo ra sự phân tâm không đáng có, làm gián đoạn dòng suy nghĩ của bạn khi viết. 

**Takeaway:**
Sự giàu có về số lượng plugin thường tạo ra sự nghèo nàn về sự chú ý. Bằng việc lược bỏ triệt để những thứ không cần thiết, FLOW Vault giờ đây nhẹ nhàng, sắc bén và thực sự sẵn sàng trở thành một nhà máy sản xuất tri thức đáng tin cậy của bạn. 
