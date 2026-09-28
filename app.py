import hashlib
import streamlit as st

# مفتاح سري خاص بك فقط (تأكد من مطابقته للمفتاح المستخدم في تطبيق التداول)
SECRET_MASTER_KEY = "TAHSEEN_TRADING_APP_SECRET_2026"

st.set_page_config(
    page_title="Trading App Keygen", page_icon="🔑", layout="centered"
)

st.title("🔑 أداة تفعيل تطبيق التداول")
st.markdown("---")

# إدخال Device ID الذي أرسله العميل
device_id_input = st.text_input(
    "أدخل Device ID الخاص بالمستخدم:",
    placeholder="مثال: dev_9f87b6a54321",
)


# دالة توليد الكود الفريد بناءً على Device ID
def generate_license_key(dev_id: str) -> str:
  if not dev_id:
    return ""
  raw_string = f"{dev_id.strip()}_{SECRET_MASTER_KEY}"
  full_hash = hashlib.sha256(raw_string.encode()).hexdigest()
  formatted_key = (
      f"{full_hash[:4]}-{full_hash[4:8]}-{full_hash[8:12]}-{full_hash[12:16]}"
  ).upper()
  return formatted_key


if st.button("توليد كود التفعيل 🚀", type="primary"):
  if device_id_input:
    key = generate_license_key(device_id_input)
    st.success("تم توليد كود التفعيل بنجاح:")
    st.code(key, language="text")
    st.info(
        "قم بنسخ الكود وإرساله للعميل عبر واتساب (00963998313377) مع إثبات"
        " الدفع."
    )
  else:
    st.warning("الرجاء إدخال Device ID صالح أولاً.")