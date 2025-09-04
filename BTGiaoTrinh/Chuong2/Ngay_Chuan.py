
chuan = {
    "hai": "Thứ 2",
    "thứ hai": "Thứ 2",
    "thu hai": "Thứ 2",
    "Hai": "Thứ 2",
    "Thu hai": "Thứ 2",
    "TH": "Thứ 2",
    "th": "Thứ 2",
    "Tht": "Thứ 2",


    "ba": "Thứ 3",
    "thứ ba": "Thứ 3",
    "thu ba": "Thứ 3",
    "Ba": "Thứ 3",
    "Thu ba": "Thứ 3",
    "Tb": "Thứ 3",
    "tb": "Thứ 3",
    "TB": "Thứ 3",

    "tư": "Thứ 4",
    "thứ tư": "Thứ 4",
    "thu tư": "Thứ 4",
    "Tư": "Thứ 4",
    "Thu tư": "Thứ 4",
    "tu": "Thứ 4",
    "Tu": "Thứ 4",
    "tt": "Thứ 4",
    "TT": "Thứ 4",

    "năm": "Thứ 5",
    "thứ năm": "Thứ 5",
    "thu nam": "Thứ 5",
    "Năm": "Thứ 5",
    "Thu nam": "Thứ 5",
    "nam": "Thứ 5",
    "Nam": "Thứ 5",
    "tn": "Thứ 5",
    "TN": "Thứ 5",


    "sáu": "Thứ 6",
    "thứ sáu": "Thứ 6",
    "thu sau": "Thứ 6",
    "Sáu": "Thứ 6",
    "Thu sau": "Thứ 6",
    "sau": "Thứ 6",
    "Sau": "Thứ 6",
    "ts": "Thứ 6",
    "TS": "Thứ 6",


    "bảy": "Thứ 7",
    "thứ bảy": "Thứ 7",
    "thu bay": "Thứ 7",
    "Bảy": "Thứ 7",
    "Thu bay": "Thứ 7",
    "bay": "Thứ 7",
    "Bay": "Thứ 7",
    "t7": "Thứ 7",
    "T7": "Thứ 7",


    "chủ nhật": "Chủ nhật",
    "chunhat": "Chủ nhật",
    "Chủ nhật": "Chủ nhật",
    "Chunhat": "Chủ nhật",
    "cn": "Chủ nhật",
    "CN": "Chủ nhật"

}

def chuan_ngay(d):
    d = d.lower().strip()  # chữ thường + loại khoảng trắng
    return chuan.get(d, None)  # trả về None nếu không hợp lệ
