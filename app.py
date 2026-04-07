import streamlit as st
import secrets
import string
import math
# Настройка заголовка сайта
st.set_page_config(page_title="Генератор паролей", page_icon="🔐")
st.title("🔐 Генератор и анализатор паролей")
# Функция расчета (та же, что в проекте)
def calculate_entropy(password):
  if not password: return 0
  n = 0
  if any(c in string.ascii_lowercase for c in password): n += 26
  if any(c in string.ascii_uppercase for c in password): n += 26
  if any(c in string.digits for c in password): n += 10
  if any(c in string.punctuation for c in password): n += 32
  return len(password) * math.log2(n) if n > 0 else 0
# Боковая панель с выбором режима
mode = st.sidebar.selectbox("Выберите действие:", ["Генерация", "Проверка моего пароля"])
if mode == "Генерация":
  st.subheader("Настройки генерации")
  length = st.slider("Длина пароля", 4, 32, 12)
  use_upper = st.checkbox("Заглавные буквы", True)
  use_digits = st.checkbox("Цифры", True)
  use_spec = st.checkbox("Спецсимволы", True)
  if st.button("Сгенерировать"):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_spec: chars += string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    st.success(f"Ваш пароль: `{password}`")
    entropy = calculate_entropy(password)
    st.info(f"Энтропия: {entropy:.2f} бит")
else:
  st.subheader("Проверка надежности")
  user_pwd = st.text_input("Введите ваш пароль", type="password")
    if user_pwd:
      entropy = calculate_entropy(user_pwd)
      st.write(f"Стойкость: **{entropy:.2f} бит**")
        if entropy < 40:
          st.error("Слабый пароль")
        elif entropy < 60:
          st.warning("Средняя надежность")
        else: 
          st.success("Высокая надежность")
