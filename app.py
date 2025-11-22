import streamlit as st

# ----------------------------
# 세션 상태 초기화 (안전하게)
# ----------------------------
if "todos" not in st.session_state:
    st.session_state.todos = []        # 할 일 리스트

if "coins" not in st.session_state:
    st.session_state.coins = 0         # 코인

# items가 리스트인지 확인 (중요!!)
if "items" not in st.session_state or not isinstance(st.session_state.items, list):
    st.session_state.items = []        # 구매한 아이템

# ----------------------------
# 앱 제목
# ----------------------------
st.title("📝 할 일 + 코인 게이미피케이션")

# ----------------------------
# 할 일 추가
# ----------------------------
new_todo = st.text_input("할 일을 입력하세요:")

if st.button("추가", key="add_task"):
    if new_todo:
        st.session_state.todos.append({"task": new_todo, "done": False})
        st.success(f"'{new_todo}' 추가됨!")

# ----------------------------
# 할 일 목록 및 완료 버튼
# ----------------------------
st.subheader("📋 할 일 목록")

for idx, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([4, 1])

    with col1:
        status = "✅" if todo["done"] else "❌"
        st.write(f"{status} {todo['task']}")

    with col2:
        if not todo["done"]:
            if st.button("완료!", key=f"done_{idx}"):
                st.session_state.todos[idx]["done"] = True
                st.session_state.coins += 10  # 완료 시 코인 지급
                st.success(f"코인 +10! 현재 코인: {st.session_state.coins}")

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
        # 고유 key 지정 (중복 오류 방지)
        if st.button("구매", key=f"buy_{idx}"):
            if st.session_state.coins >= price:
                st.session_state.coins -= price
                st.session_state.items.append(item)
                st.success(f"{item} 구매 완료!")
            else:
                st.error("코인이 부족해요!")

# ----------------------------
# 구매 아이템 목록
# ----------------------------
if st.session_state.items:
    st.subheader("🎁 보유 아이템")
    for owned_item in st.session_state.items:
        st.write(f"- {owned_item}")
