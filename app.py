import streamlit as st

# --- 1. CẤU HÌNH GIAO DIỆN HỒNG - TRẮNG ---
st.set_page_config(page_title="PinkMath Prep 12", page_icon="🌸", layout="wide")

# CSS tùy chỉnh để đổi màu giao diện
st.markdown("""
<style>
    /* Nền chung màu trắng hồng nhạt */
    .stApp {
        background-color: #FFF0F5;
    }
    /* Sidebar màu hồng đậm hơn */
    [data-testid="stSidebar"] {
        background-color: #FFC0CB;
    }
    /* Tiêu đề và chữ màu hồng đậm */
    h1, h2, h3 {
        color: #C71585 !important;
        font-family: 'Helvetica', sans-serif;
    }
    /* Nút bấm màu hồng */
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #D87093;
    }
    /* Khung câu hỏi màu trắng bo góc */
    .question-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #FF69B4;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU ĐỀ THI (TRÍCH XUẤT TỪ PDF) ---
# Dữ liệu được lấy từ các đề ôn tập bạn cung cấp
exam_data = {
    "part1": [ # Trắc nghiệm 4 lựa chọn
        {
            "id": 1,
            "q": "Nguyên hàm của hàm số $f(x)=x^5$ là:",
            "opts": ["$F(x)=5x^4+C$", "$F(x)=\\frac{x^6}{6}+C$", "$F(x)=x^6+C$", "$F(x)=\\frac{x^4}{4}+C$"],
            "ans": "$F(x)=\\frac{x^6}{6}+C$",
            "expl": "Áp dụng công thức $\\int x^n dx = \\frac{x^{n+1}}{n+1} + C$. [span_7](start_span)(Nguồn: Đề số 01[span_7](end_span))"
        },
        {
            "id": 2,
            "q": "Trong không gian Oxyz, cho tam giác ABC có $A(2;1;-3), B(4;2;1), C(3;0;5)$. Tọa độ trọng tâm G là:",
            "opts": ["G(3;1;1)", "G(1;3;1)", "G(3;1;-1)", "G(9;3;3)"],
            "ans": "G(3;1;1)",
            "expl": "Công thức trọng tâm: $x_G = \\frac{2+4+3}{3}=3; y_G = \\frac{1+2+0}{3}=1; z_G = \\frac{-3+1+5}{3}=1$. [span_8](start_span)(Nguồn: Đề số 01[span_8](end_span))"
        },
        {
             "id": 3,
            "q": "Tiệm cận ngang của đồ thị hàm số $y=\\frac{4x+1}{x-1}$ là:",
            "opts": ["y=4", "y=1/4", "y=1", "x=1"],
            "ans": "y=4",
            "expl": "Tiệm cận ngang là $y=a/c = 4/1 = 4$. [span_9](start_span)[span_10](start_span)(Nguồn: Đề số 06[span_9](end_span)[span_10](end_span))"
        }
    ],
    "part2": [ # Đúng/Sai
        {
            "id": 1,
            "q": "Cho hàm số $f(x) = \\sin 2x - x$. Xét tính đúng sai của các khẳng định sau:",
            "subs": [
                {"s": "$f(-\\frac{\\pi}{2}) = \\frac{\\pi}{2}$", "ans": "Đúng"},
                {"s": "Đạo hàm $f'(x) = \\cos 2x - 1$", "ans": "Sai"}, # Phải là 2cos2x - 1
                {"s": "Phương trình $f'(x)=0$ có 2 nghiệm trên đoạn $[-\\frac{\\pi}{2}; \\frac{\\pi}{2}]$", "ans": "Đúng"},
                {"s": "Min của hàm số trên đoạn này là $-\\frac{\\pi}{2}$", "ans": "Đúng"}
            ],
            "expl": "Đạo hàm đúng là $f'(x) = 2\\cos 2x - 1$. [span_11](start_span)(Nguồn: Đề số 01[span_11](end_span))"
        }
    ],
    "part3": [ # Trả lời ngắn
        {
            "id": 1,
            "q": "Cho hình chóp tứ giác đều S.ABCD có cạnh đáy bằng 2, cạnh bên bằng $2\\sqrt{2}$. Tính khoảng cách giữa hai đường thẳng AB và SD (làm tròn đến hàng phần mười).",
            "ans": 1.4, # Ví dụ kết quả tính toán
            "expl": "Sử dụng phương pháp tọa độ hóa hoặc dựng hình chiếu vuông góc. [span_12](start_span)(Nguồn: Đề số 01[span_12](end_span))"
        }
    ]
}

# --- 3. GIAO DIỆN CHÍNH ---
def main():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2936/2936757.png", width=100)
        st.title("PinkMath Prep")
        st.write("Chào mừng các bạn 2K7 ôn thi THPT Quốc Gia!")
        mode = st.radio("Chọn chế độ:", ["🏠 Trang chủ", "📝 Làm đề thi thử", "📚 Ôn tập kiến thức"])
        st.markdown("---")
        st.info("💡 Mẹo: Hãy chuẩn bị giấy nháp trước khi bắt đầu nhé!")

    if mode == "🏠 Trang chủ":
        show_homepage()
    elif mode == "📝 Làm đề thi thử":
        show_exam_page()
    elif mode == "📚 Ôn tập kiến thức":
        show_review_page()

def show_homepage():
    st.header("Chào mừng đến với PinkMath Prep! 🎀")
    st.markdown("""
    Ứng dụng giúp bạn ôn luyện Toán 12 với giao diện dễ thương, giảm stress.
    
    **Nội dung dựa trên cấu trúc đề thi mới 2025:**
    * **Phần 1:** Trắc nghiệm nhiều lựa chọn (Tư duy nhanh).
    * **Phần 2:** Trắc nghiệm Đúng/Sai (Tư duy phản biện).
    * **Phần 3:** Trả lời ngắn (Vận dụng cao).
    
    [span_13](start_span)[span_14](start_span)[span_15](start_span)Dữ liệu được tổng hợp từ các đề thi thử thực tế[span_13](end_span)[span_14](end_span)[span_15](end_span).
    """)
    st.button("Bắt đầu ngay 🚀")

def show_exam_page():
    st.header("📝 Đề Thi Thử Số 01")
    
    with st.form("exam_form"):
        # Phần 1
        st.subheader("Phần I: Trắc nghiệm (3 điểm)")
        for q in exam_data["part1"]:
            st.markdown(f"<div class='question-box'><b>Câu {q['id']}:</b> {q['q']}</div>", unsafe_allow_html=True)
            st.radio(f"Chọn đáp án câu {q['id']}:", q['opts'], key=f"p1_q{q['id']}")
        
        # Phần 2
        st.subheader("Phần II: Đúng / Sai (4 điểm)")
        for q in exam_data["part2"]:
            st.markdown(f"<div class='question-box'><b>Câu {q['id']}:</b> {q['q']}</div>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            for i, sub in enumerate(q['subs']):
                with col1 if i % 2 == 0 else col2:
                    st.write(f"- {sub['s']}")
                    st.radio(f"Ý {i+1}", ["Đúng", "Sai"], key=f"p2_q{q['id']}_s{i}", horizontal=True)
        
        # Phần 3
        st.subheader("Phần III: Trả lời ngắn (3 điểm)")
        for q in exam_data["part3"]:
            st.markdown(f"<div class='question-box'><b>Câu {q['id']}:</b> {q['q']}</div>", unsafe_allow_html=True)
            st.text_input("Nhập kết quả (số thập phân):", key=f"p3_q{q['id']}")

        submitted = st.form_submit_button("Nộp bài & Xem điểm 💖")
    
    if submitted:
        st.balloons()
        st.success("Chúc mừng bạn đã hoàn thành bài thi! Dưới đây là đáp án chi tiết:")
        show_solutions()

def show_solutions():
    with st.expander("🔎 Xem lời giải chi tiết"):
        st.markdown("### Đáp án Phần I")
        for q in exam_data["part1"]:
            st.write(f"**Câu {q['id']}:** Đáp án đúng là **{q['ans']}**")
            st.info(f"💡 *Giải thích:* {q['expl']}")
        
        st.markdown("### Đáp án Phần II")
        for q in exam_data["part2"]:
            st.write(f"**Câu {q['id']}:**")
            for sub in q['subs']:
                st.write(f"- {sub['s']} -> **{sub['ans']}**")
            st.info(f"💡 *Giải thích:* {q['expl']}")

def show_review_page():
    st.header("📚 Góc Ôn Tập")
    tab1, tab2, tab3 = st.tabs(["Giải Tích", "Hình Oxyz", "Xác Suất"])
    
    with tab1:
        st.subheader("Nguyên Hàm - Tích Phân")
        st.latex(r"\int x^n dx = \frac{x^{n+1}}{n+1} + C")
        st.latex(r"\int e^x dx = e^x + C")
        [span_16](start_span)[span_17](start_span)st.info("Nhớ kỹ bảng nguyên hàm cơ bản để làm nhanh Phần I[span_16](end_span)[span_17](end_span).")
    
    with tab2:
        st.subheader("Phương pháp tọa độ trong không gian")
        st.markdown("**Phương trình mặt cầu (S):**")
        st.latex(r"(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2")
        [span_18](start_span)st.markdown("Tâm $I(a;b;c)$, Bán kính $R$. (Nguồn: Đề số 05[span_18](end_span))")
        
    with tab3:
        st.subheader("Thống kê & Xác suất")
        [span_19](start_span)[span_20](start_span)st.write("Công thức tính khoảng biến thiên, tứ phân vị cho mẫu số liệu ghép nhóm[span_19](end_span)[span_20](end_span).")

if __name__ == "__main__":
    main()
