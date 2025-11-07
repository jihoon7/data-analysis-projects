{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaaa330c-cad0-404c-bcaa-cff96199df6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "SYSTEM_PROMPT = \"너는 회사의 인사/복지 정책을 안내하는 친절한 도우미야. 답변은 명확하고 공손하게 해.\"\n",
    "\n",
    "USER_PROMPT = \"\"\"\n",
    "아래는 회사 내부 문서에서 추출된 내용입니다. 이를 참고하여 사용자의 질문에 정확히 답변해주세요.\n",
    "\n",
    "[문서 내용]\n",
    "{context_text}\n",
    "\n",
    "[사용자 질문]\n",
    "{query}\n",
    "\n",
    "[답변]\n",
    "\"\"\"\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "LLM RAG Project",
   "language": "python",
   "name": "llm-env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
