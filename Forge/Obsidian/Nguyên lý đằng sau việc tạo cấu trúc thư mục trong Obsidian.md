---
created: 2026-04-29 23:25:00
progress: medium
rank: 5
blueprint:
  - "[[Obsidian PKM Mastery]]"
tags:
  - topic/pkm
  - topic/obsidian
  - type/article
cover:
---

Khi mới sử dụng Obsidian, câu hỏi đầu tiên khiến chúng ta bối rối nhất thường là: *"Mình nên tạo bao nhiêu thư mục?"*. Theo phản xạ tự nhiên, chúng ta tìm đến những tiêu chuẩn phổ biến của giới PKM: Zettelkasten với 3 thư mục, PARA với 4 thư mục, hay Ideaverse với 4 thư mục. 

Bạn hăm hở thiết lập theo họ. Nhưng chỉ sau vài tuần, bạn bắt đầu thấy lấn cấn: *"Mình nên lưu file ảnh đính kèm ở đâu?"*, *"Template của các plugin đưa vào thư mục nào cho gọn?"*. Cuối cùng, bạn đẻ ra hàng tá thư mục con chằng chịt, phá vỡ hoàn toàn cấu trúc ban đầu. 

Tại sao những hệ thống danh tiếng toàn cầu lại trở nên lộn xộn khi đưa vào Obsidian? Vấn đề không nằm ở việc bạn kém ngăn nắp, mà nằm ở sự xung đột giữa **lý thuyết tổ chức** và **đặc tính kỹ thuật** của công cụ.

### 1. Góc khuất kỹ thuật của Obsidian

Khác với Notion hay Evernote, Obsidian là phần mềm quản lý file Markdown cục bộ. Việc các file nằm ngay trên ổ cứng của bạn sinh ra những nhu cầu quản lý đặc thù:

- Bạn cần một nơi để chứa hàng ngàn file đính kèm.
- Bạn cần một khu vực tách biệt để lưu trữ các file mẫu thông qua core-plugin.
- Các plugin hỗ trợ tư duy trực quan như Excalidraw luôn đòi hỏi không gian riêng để lưu trữ cấu hình hoặc kịch bản chạy.

Đó là lý do chúng ta có nhu cầu sử dụng thư mục để nhóm các cài đặt ít dùng lại một nơi. Một kiến trúc bền vững phải có không gian riêng cho hệ thống vận hành bên dưới, chứ không chỉ thuần túy là nơi chứa nội dung bề nổi.

### 2. Sự khiên cưỡng của các hệ thống vay mượn

Khi bưng bê nguyên xi các phương pháp nổi tiếng vào Obsidian, chúng ta đang vô tình vi phạm **Nguyên tắc MECE** (Độc lập và Toàn diện) và **Nguyên lý Kim tự tháp** trong việc phân cấp logic.

- **Zettelkasten (3 thư mục):** Bản chất Zettelkasten là một triết lý tư duy thuần túy, không phải là một kiến trúc phần mềm. Việc áp dụng 3 nhóm thư mục này khiến bạn hoàn toàn không có chỗ cho tệp đính kèm hay cài đặt hệ thống. Bạn buộc phải tạo thêm các thư mục ngoại lai, phá vỡ cấu trúc nguyên bản.
- **BASB của Tiago Forte (4 thư mục):** Phương pháp này được thiết kế cho hệ thống file truyền thống từ kỷ nguyên Evernote thịnh hành. Việc nhét file cấu hình hay bản mẫu của Obsidian vào thư mục *Resources* là một sự cưỡng ép logic. Hơn nữa, với giới hạn 4 thư mục, bạn bắt buộc phải tạo rất nhiều tầng thư mục con bên trong, dựng lên những bức tường ngăn cách khiến việc truy xuất trở nên nặng nề.
- **Ideaverse của Nick Milo:** Dù thiết kế cho Obsidian, nhưng việc gộp chung file cài đặt hệ thống và đính kèm vào thư mục `Atlas` (nơi chứa Bản đồ tri thức) vẫn tạo ra sự pha trộn khiên cưỡng giữa dữ liệu tri thức và rác kỹ thuật.

### 3. Nguyên lý của FLOW: Xây dựng nhà máy sản xuất tư duy

Từ việc nhìn nhận những lỗ hổng trên, kiến trúc **6 thư mục của FLOW PKM** được thiết kế không phải để chạy theo số lượng, mà để đáp ứng triệt để hai yếu tố: Giới hạn sinh học của não bộ và Tính nguyên bản của Obsidian.

Tại sao lại là con số 6?

- **Định luật Miller (7±2):** Não bộ con người chỉ xử lý hiệu quả khoảng 7 nhóm thông tin cùng lúc. Cấu trúc 6 thư mục nằm ở mức vừa vặn hoàn hảo. Mở Vault lên, bạn nhìn bao quát toàn bộ hệ thống mà không bị ngợp.
- **Tính vòng đời:** Thay vì phân loại theo chủ đề (rất dễ trùng lặp), FLOW phân loại theo **Vòng đời của tri thức**. Ghi chú giống như nguyên liệu đi qua 5 phân xưởng: thu thập, rèn dũa, lắp ráp và thành phẩm. Sự phân chia này đảm bảo tính độc lập và không chồng chéo.
- **Tôn trọng đặc tính kỹ thuật:** Thư mục cuối cùng được tách riêng làm khu vực kỹ thuật. Nó ôm trọn toàn bộ file đính kèm, bản mẫu, và cấu hình hệ thống. Sự rạch ròi này giúp các không gian dữ liệu phía trên luôn được tối ưu, không bị file hệ thống xâm lấn.

### Tạm kết

Đừng xây dựng hệ thống thư mục của bạn dựa trên việc bắt chước mù quáng số lượng thư mục của người khác. Một kiến trúc vững chắc phải thuyết phục được tính logic (MECE) và phải dung hòa được đặc thù của công cụ bạn đang dùng. 

Khi các thư mục được thiết kế dựa trên vòng đời tự nhiên của tri thức và đáp ứng đủ các rào cản kỹ thuật, hệ thống của bạn sẽ tĩnh tại. Bạn sẽ hiếm khi phải tốn năng lượng để tái cấu trúc lại Vault, mà có thể dành trọn vẹn dung lượng tâm trí cho việc kiến tạo những góc nhìn sâu sắc.