
import streamlit as st
import random
import string

# إعداد الصفحة
st.set_page_config(page_title="Alphabet AI Simulation", page_icon="🔤")
st.title("📘 Alphabet Wizard Smart Book - AI Simulation")
st.write("🧠 هذه محاكاة تفاعلية لتدريب الطفل على نطق الحروف باستخدام الذكاء الاصطناعي.")

# تهيئة المتغيرات داخل session_state
if 'target' not in st.session_state:
    st.session_state.target = random.choice(string.ascii_uppercase)
if 'correct_count' not in st.session_state:
    st.session_state.correct_count = 0
if 'wrong_count' not in st.session_state:
    st.session_state.wrong_count = 0
if 'mistakes' not in st.session_state:
    st.session_state.mistakes = []
if 'answered' not in st.session_state:
    st.session_state.answered = False

# عرض الحرف المطلوب
st.markdown(f"### 🔤 نطق الحرف المطلوب: **{st.session_state.target}**")

# إدخال المستخدم
user_input = st.text_input("📣 أدخل الحرف الذي نطقته:")

# التحقق من الإجابة
if user_input and not st.session_state.answered:
    if user_input.strip().upper() == st.session_state.target:
        st.success("✅ صحيح! أحسنت!")
        st.session_state.correct_count += 1
    else:
        st.error("❌ غير صحيح. حاول مرة أخرى.")
        st.session_state.wrong_count += 1
        st.session_state.mistakes.append(st.session_state.target)
    st.session_state.answered = True

# عرض مستوى التقدم
total_attempts = st.session_state.correct_count + st.session_state.wrong_count
if total_attempts > 0:
    accuracy = st.session_state.correct_count / total_attempts
    st.progress(accuracy)
    st.info(f"🎯 تم الإجابة على {total_attempts} حرفًا: ✅ {st.session_state.correct_count} صحيح | ❌ {st.session_state.wrong_count} خطأ")

# عرض الحروف التي تحتاج إلى مراجعة
if st.session_state.mistakes:
    review_letters = list(set(st.session_state.mistakes))
    st.warning(f"📌 الحروف التي تحتاج إلى مراجعة: {' - '.join(review_letters)}")

# عرض نصائح تعليمية
with st.expander("📚 نصائح لتحسين تعلم الحروف الأبجدية"):
    st.write("""
- استخدم بطاقات تعليمية ملوّنة لجذب الانتباه.
- اربط كل حرف بكلمة وصورة (A = Apple 🍎).
- شجّع الطفل على نطق الحرف بصوت عالٍ.
- كرّر الحروف من خلال الألعاب والنشاطات اليومية.
- استخدم الأغاني التعليمية لحروف اللغة الإنجليزية.
""")

# زر الانتقال إلى حرف جديد
if st.session_state.answered:
    if st.button("🔄 التالي"):
        st.session_state.target = random.choice(string.ascii_uppercase)
        st.session_state.answered = False
        st.experimental_rerun()
