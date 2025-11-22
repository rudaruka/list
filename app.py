import streamlit as st

# ----------------------------
# 세션 상태 초기화
# ----------------------------
if "todos" not in st.session_state:
    st.session_state.todos = []

if "coins" not in st.session_state:
    st.session_state.coins = 0

if "items" not in st.session_state:
    st.session_state.items = []

# ----------------------------
# 앱 제목
# ----------------------------
st.title("📝 할 일 + 코인 게이미피케이션")

# ----------------------------
# 할 일 추가 (Form 사용)
# ----------------------------
with st.form("add_todo_form"):
    new_todo = st.text_input("할 일을 입력하세요:", key="new_todo")
    submit_todo = st.form_submit_button("추가")

if submit_todo:
    if new_todo.strip() != "":
        st.session_state.todos.append({"task": new_todo, "done": False})
        st.success(f"'{new_todo}' 추가됨!")
        st.session_state.new_todo = ""  # 입력창 초기화
    else:
        st.error("빈 칸은 추가할 수 없어요!")

# ----------------------------
# 할 일 목록 (완료 시 제거)
# ----------------------------
st.subheader("📋 할 일 목록")

# 완료된 항목 index 모아두기
todos_to_remove = []

for idx, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"❌ {todo['task']}")

    with col2:
        if st.button("완료!", key=f"done_{idx}"):
            st.session_state.coins += 10
            st.success(f"코인 +10! 현재 코인: {st.session_state.coins}")
            todos_to_remove.append(idx)

# 완료된 항목 안전하게 제거 (뒤에서부터)
for idx in sorted(todos_to_remove, reverse=True):
    st.session_state.todos.pop(idx)

# ----------------------------
# 코인 현황
# ----------------------------
st.subheader(f"💰 현재 코인: {st.session_state.coins}")

# ----------------------------
# 상점
# ----------------------------
st.subheader("🛒 상점")

shop_items = {
    "배경 테마 🌄": 30,
    "캐릭터 모자 🎩": 50,
    "강화 포션 💎": 20
}

for idx, (item, price) in enumerate(shop_items.items()):
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"{item} - {price} 코인")

    with col2:
        if st.button("구매", key=f"buy_{idx}"):
            if st.session_state.coins >= price:
                st.session_state.coins -= price
                st.session_state.items.append(item)
                st.success(f"{item} 구매 완료!")
            else:
                st.error("코인이 부족해요!")
