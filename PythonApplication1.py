playlist = [
    {
        "ten": "Em Của Ngày Hôm Qua",
        "ca_si": "Sơn Tùng M-TP",
        "the_loai": "Pop",
        "thoi_luong": 4.5
    },
    {
        "ten": "Nơi Này Có Anh",
        "ca_si": "Sơn Tùng M-TP",
        "the_loai": "Ballad",
        "thoi_luong": 5.0
    },
    {
        "ten": "Hãy Trao Cho Anh",
        "ca_si": "Sơn Tùng M-TP",
        "the_loai": "Rap",
        "thoi_luong": 4.2
    },
    {
        "ten": "See Tình",
        "ca_si": "Hoàng Thùy Linh",
        "the_loai": "Dance",
        "thoi_luong": 3.8
    },
    {
        "ten": "Waiting For You",
        "ca_si": "MONO",
        "the_loai": "Pop",
        "thoi_luong": 4.1
    }
]

def them_bai_hat():

    ten = input("Nhập tên bài hát: ")
    ca_si = input("Nhập tên ca sĩ: ")
    the_loai = input("Nhập thể loại: ")

    while True:

        try:
            thoi_luong = float(input("Nhập thời lượng (phút): "))

            if thoi_luong > 0:
                break
            else:
                print("Thời lượng phải lớn hơn 0!")

        except:
            print("Yêu cầu nhập số cho thời lượng!")

    bai_hat = {
        "ten": ten,
        "ca_si": ca_si,
        "the_loai": the_loai,
        "thoi_luong": thoi_luong
    }

    playlist.append(bai_hat)

    print("Đã thêm bài hát!\n")


def hien_thi_playlist():

    if len(playlist) == 0:
        print("Playlist đang trống!\n")
        return

    print("\n===== DANH SÁCH BÀI HÁT =====")

    for i in range(len(playlist)):

        bai_hat = playlist[i]

        print(f"""
Bài hát {i + 1}
Tên bài hát : {bai_hat['ten']}
Ca sĩ       : {bai_hat['ca_si']}
Thể loại    : {bai_hat['the_loai']}
Thời lượng  : {bai_hat['thoi_luong']} phút
-----------------------------
""")


def sap_xep_theo_ten():

    playlist.sort(key=lambda x: x["ten"])

    print("Đã sắp xếp theo tên bài hát!\n")

    hien_thi_playlist()


def sap_xep_theo_ca_si():

    playlist.sort(key=lambda x: x["ca_si"])

    print("Đã sắp xếp theo ca sĩ!\n")

    hien_thi_playlist()


def tim_theo_ten():

    tu_khoa = input("Nhập tên bài hát cần tìm: ").lower()

    tim_thay = False

    print("\n===== KẾT QUẢ =====")

    for bai_hat in playlist:

        if tu_khoa in bai_hat["ten"].lower():

            print(f"""
Tên bài hát : {bai_hat['ten']}
Ca sĩ       : {bai_hat['ca_si']}
Thể loại    : {bai_hat['the_loai']}
Thời lượng  : {bai_hat['thoi_luong']} phút
-----------------------------
""")

            tim_thay = True

    if tim_thay == False:
        print("Không tìm thấy!\n")


def tim_theo_ca_si():

    tu_khoa = input("Nhập tên ca sĩ cần tìm: ").lower()

    tim_thay = False

    print("\n===== KẾT QUẢ =====")

    for bai_hat in playlist:

        if tu_khoa in bai_hat["ca_si"].lower():

            print(f"""
Tên bài hát : {bai_hat['ten']}
Ca sĩ       : {bai_hat['ca_si']}
Thể loại    : {bai_hat['the_loai']}
Thời lượng  : {bai_hat['thoi_luong']} phút
-----------------------------
""")

            tim_thay = True

    if tim_thay == False:
        print("Không tìm thấy!\n")


def xoa_bai_hat():

    hien_thi_playlist()

    if len(playlist) == 0:
        return

    vi_tri = int(input("Nhập số thứ tự bài hát cần xóa: "))

    if 1 <= vi_tri <= len(playlist):

        playlist.pop(vi_tri - 1)

        print("Đã xóa bài hát!\n")

    else:
        print("Vị trí không hợp lệ!\n")


def ghi_file():

    file = open("playlist.txt", "w", encoding="utf-8")

    for bai_hat in playlist:

        dong = (
            bai_hat["ten"] + "|" +
            bai_hat["ca_si"] + "|" +
            bai_hat["the_loai"] + "|" +
            str(bai_hat["thoi_luong"]) + "\n"
        )

        file.write(dong)

    file.close()

    print("Đã lưu file!\n")


def doc_file():

    global playlist

    playlist.clear()

    try:
        file = open("playlist.txt", "r", encoding="utf-8")

        for dong in file:

            du_lieu = dong.strip().split("|")

            bai_hat = {
                "ten": du_lieu[0],
                "ca_si": du_lieu[1],
                "the_loai": du_lieu[2],
                "thoi_luong": float(du_lieu[3])
            }

            playlist.append(bai_hat)

        file.close()

        print("Đã đọc file!\n")

    except:
        print("Chưa có file dữ liệu!\n")


while True:

    print("========== QUẢN LÝ PLAYLIST ==========")
    print("1. Thêm bài hát")
    print("2. Hiển thị playlist")
    print("3. Sắp xếp theo tên bài hát")
    print("4. Sắp xếp theo ca sĩ")
    print("5. Tìm kiếm theo tên bài hát")
    print("6. Tìm kiếm theo ca sĩ")
    print("7. Xóa bài hát")
    print("8. Ghi playlist vào file")
    print("9. Đọc playlist từ file")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn: ")

    print()

    if lua_chon == "1":
        them_bai_hat()

    elif lua_chon == "2":
        hien_thi_playlist()

    elif lua_chon == "3":
        sap_xep_theo_ten()

    elif lua_chon == "4":
        sap_xep_theo_ca_si()

    elif lua_chon == "5":
        tim_theo_ten()

    elif lua_chon == "6":
        tim_theo_ca_si()

    elif lua_chon == "7":
        xoa_bai_hat()

    elif lua_chon == "8":
        ghi_file()

    elif lua_chon == "9":
        doc_file()

    elif lua_chon == "0":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!\n")
