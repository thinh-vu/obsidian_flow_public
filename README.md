# FLOW - Phương pháp quản lý tri thức tối ưu cho Obsidian

## Giới thiệu

> [!hint]
Chào mừng bạn ghé thăm không gian minh hoạ phương pháp quản lý kiến thức FLOW trong Obsidian. 
Phương pháp FLOW do Thịnh Vũ phát triển là kết quả của quá trình trải nghiệm, tương tác và chia sẻ với cộng đồng trong 3 năm qua. 
Obsidian FLOW là kết quả của những trăn trở, tìm tòi và nghiên cứu của anh nhằm tìm ra một hệ thống quản lý linh hoạt, đa dụng và cá nhân hoá quản lý cuộc sống "số" và hành trình tích luỹ kiến thức thú vị hơn.

Phương pháp **FLOW** được tối ưu tối đa cho Obsidian nhưng đồng thời có thể áp dụng với bất kỳ nền tảng dịch vụ lưu trữ và ghi chú nào.

Hy vọng **FLOW** sẽ giúp bạn khám phá một cách tiếp cận đơn giản nhưng mạnh mẽ trong tổ chức thông tin và ý tưởng một cách hiệu quả, linh hoạt và dễ dàng cá nhân hoá theo nhu cầu của bạn.

## Phương pháp FLOW là gì?

Hãy tưởng tượng bạn đang đứng giữa một cánh rừng lớn, đầy những cây xanh và vô số con đường nhỏ không rõ ràng. Đây chính là cảm giác của tôi khi đối mặt với việc quản lý ghi chú. Ý tưởng liên tục tràn ngập, nhưng mọi thứ cứ nằm lộn xộn, không có hệ thống. Mỗi khi cần tìm lại một ghi chú hoặc phát triển một ý tưởng, tôi cảm thấy như đang lạc lối trong chính không gian trí óc của tôi.

Tôi biết tôi cần một con đường rõ ràng hơn – một bản đồ giúp tôi điều hướng qua mớ hỗn độn đó. Và đó là khi phương pháp **FLOW** ra đời. FLOW không chỉ là một phương pháp, nó là lộ trình giúp tôi từ những ý tưởng ban đầu đến khi hoàn thiện, giống như việc rèn một thanh kiếm từ kim loại thô cho đến khi nó trở nên sắc bén và mạnh mẽ. 

**FLOW** là viết tắt của:

- **Forge** (_Rèn Luyện_): Thể hiện quá trình sáng tạo và không ngừng hoàn thiện từ ý tưởng thô sơ cho đến khi hoàn thiện. 
- **Link** (_Liên Kết_): Tượng trưng cho sự kết nối và liên hệ giữa các dự án, ý tưởng và nhiệm vụ khác nhau. **Link** thể hiện việc tổ chức các dự án ở một cấp độ trừu tượng, liên kết chúng với nhau.
- **Organize** (_Tổ Chức_): Đại diện cho việc sắp xếp và trưng bày các thành phẩm hoặc tài liệu đã hoàn thiện. **Organize** mang lại cảm giác trật tự và dễ dàng truy xuất thông tin.
- **Write** (_Viết_): Việc ghi chép và theo dõi tiến trình công việc, phản ánh quá trình phát triển liên tục của ý tưởng. **Write** đại diện cho hành động bắt tay vào việc viết để tư duy rành mạch đồng thời giúp duy trì dòng chảy của công việc.

Nói một cách ngắn gọn, phương pháp FLOW bao gồm một hệ thống các nguyên tắc, hướng dẫn và quy trình giúp bạn có thể làm quen cũng như tích hợp hoàn toàn lối tư duy và phương pháp làm việc vào cuộc sống cá nhân và hành trình tích luỹ tri thức của bạn.

## Tải về sử dụng

### Tải file zip về giải nén

Sử dụng cách này, bạn tải toàn bộ repo được chia sẻ dưới dạng 1 file zip, giải nén file và mở Open folder as Vault để sử dụng.

![](6.%20Vault/attachments/obsidian_flow_github_download_zip.png)

### Sao chép mẫu Vault dưới dạng 1 repo trong Github của bạn

> [!hint]
> Sử dụng cách này, bạn có thể đồng bộ Github repo về máy và sử dụng Git làm công cụ sao lưu mặc định. Thư mục Git có thể lưu trữ trong OneDrive, Google Drive, vv hay dịch vụ lưu trữ đám mây bất kỳ để tạo lớp sao lưu thứ 2. Khi đồng bộ với Github, bạn có thể xem nhanh các ghi chú thông qua Github mobile mà không cần Obsidian mobile (nhanh hơn), hoặc chỉnh sửa ghi chú với vscode.dev từ Github repo mà không cần đồng bộ trên máy trong những trường hợp bạn không tiện cài đặt Obsidian. Cũng có thể chỉnh sửa ghi chú theo cách này trên smartphone trong 1 số trường hợp cần thiết.

![](6.%20Vault/attachments/obsidian_flow_github_template_repo.png)


## Thiết lập Obsidian Vault của bạn theo phương pháp FLOW

>[!hint] Gợi ý
>Bạn có thể tìm thấy nội dung dưới đây tại trang mục lục giới thiệu phương pháp [Obsidian FLOW Methodology](4.%20Blueprint/Obsidian%20FLOW%20Methodology.md).

```dataview
TABLE tags
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), "Obsidian FLOW Methodology")
AND number(impact) >= 4
SORT aliases ASC, created DESC
```
## Một số lưu ý khi áp dụng phương pháp FLOW

- **Giữ cho hệ thống đơn giản**: Đừng tạo quá nhiều thư mục con phức tạp, hãy giữ cho cấu trúc của bạn dễ hiểu và dễ quản lý.
- **Sử dụng metadata và thẻ một cách thông minh**: Chỉ áp dụng khi cần thiết để hỗ trợ việc tìm kiếm và tổ chức.
- **Thường xuyên xem xét và cập nhật**: Dành thời gian để xem lại và sắp xếp lại ghi chú của bạn, đảm bảo chúng luôn phản ánh đúng trạng thái hiện tại.
- **Cá nhân hóa hệ thống**: Điều chỉnh phương pháp FLOW để phù hợp với nhu cầu và phong cách làm việc của bạn.

## Tại sao nên áp dụng phương pháp FLOW?

- **Đơn giản và trực quan**: FLOW giúp bạn tổ chức ghi chú theo một cấu trúc dễ hiểu, giảm thiểu sự phức tạp.
- **Linh hoạt và cá nhân hóa**: Bạn có thể điều chỉnh phương pháp để phù hợp với phong cách làm việc và mục tiêu cá nhân.
- **Hiệu quả trong việc tìm kiếm và truy cập thông tin**: Sử dụng metadata và thẻ một cách có mục đích giúp bạn nhanh chóng tìm thấy những gì tôi cần.