import streamlit as st
from modules.query_engine import search_similar_chunks
# from modules.rag_gpt import generate_answer  # GPT 연동 시 활성화

st.set_page_config(page_title="사내 휴가/복지 챗봇", page_icon="💬")
st.title("💼 사내 휴가/복지 안내 챗봇")
st.caption("사내 문서를 기반으로 의미를 파악해 정확한 답변을 제공합니다.")

query = st.text_input("질문을 입력해주세요!", placeholder="예: 병가는 유급인가요?")

if query.strip():
    results = search_similar_chunks(query, top_k=5, max_distance=0.95)

    if results:
        st.success("✅ 관련 내용을 찾았어요!")
        for i, doc in enumerate(results, 1):
            st.markdown(f"**문단 {i}**")
            st.write(doc)
            st.markdown("---")

        # GPT 연동 시 주석 해제
        # answer = generate_answer(query, results)
        # st.markdown("### 💬 GPT 종합 답변")
        # st.write(answer)

    else:
        st.warning("⚠️ 관련 문단을 찾지 못했어요.")
else:
    st.info("💡 아래 예시 질문을 눌러보세요.")

with st.expander("💬 예시 질문 보기"):
    examples = [
        "연차는 몇 일이나 되나요?",
        "병가는 유급인가요?",
        "휴가는 어떻게 신청하나요?",
        "식대는 지원되나요?",
        "복지 포인트는 어디서 쓸 수 있나요?"
    ]
    for ex in examples:
        if st.button(ex):
            query = ex
            st.experimental_rerun()
