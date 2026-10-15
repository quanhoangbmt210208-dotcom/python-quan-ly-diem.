
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 1. Tạo DataFrame
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Lan", "Minh", "Nam", "Phuc", "Trang"
    ],
    "Chuyen_can": [8, 9, 7, 10, 8, 6, 9, 7, 8, 10],
    "Giua_ky": [7, 8, 6, 9, 8, 5, 9, 7, 8, 9],
    "Cuoi_ky": [8, 9, 7, 10, 8, 6, 9, 8, 7, 10]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hiển thị bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df.round(2), use_container_width=True)

# 4. Thống kê
st.subheader("Thống kê kết quả")

diem_tb = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5).sum()

st.write(f"Điểm tổng kết trung bình của lớp: **{diem_tb:.2f}**")
st.write(
    f"Sinh viên có điểm cao nhất: **{sv_cao_nhat['Ho_ten']}** "
    f"({sv_cao_nhat['Tong_ket']:.2f})"
)
st.write(
    f"Sinh viên có điểm thấp nhất: **{sv_thap_nhat['Ho_ten']}** "
    f"({sv_thap_nhat['Tong_ket']:.2f})"
)
st.write(f"Số sinh viên đạt (điểm tổng kết ≥ 5): **{so_sv_dat}**")

# 5. Chọn sinh viên
st.subheader("Tra cứu điểm sinh viên")

ten_sv = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")
st.write(f"**Chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 6. Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# 7. Thông tin người tạo
st.markdown("---")
st.caption("Họ tên: NGUYỄN HOÀNG QUÂN | MSSV: 066208017381")
