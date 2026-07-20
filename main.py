import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Немецкая Викторина", page_icon="🇩🇪", layout="centered")

st.title("🇩🇪 Викторина по немецким словам и фразам")
st.write("Проверьте и закрепите знания 31 слова и выражения из сказки!")

# Полная база из 31 слова и выражения
VOCABULARY = [
    # 1. Идиомы и фразы
    {
        "question": "Что означает «vor lauter ...»?",
        "options": ["От изобилия / за избытком чего-то", "Перед самым началом", "Вместо чего-то", "Вопреки всему"],
        "answer": "От изобилия / за избытком чего-то"
    },
    {
        "question": "Как переводится «etwas rückgängig machen»?",
        "options": ["Отменить / расколдовать что-то", "Сделать что-то заново", "Забыть о чём-то", "Увеличить вдвое"],
        "answer": "Отменить / расколдовать что-то"
    },
    {
        "question": "Переведите «in Erfüllung gehen»:",
        "options": ["Исполняться / сбываться", "Заполнять емкость", "Уходить в отпуск", "Заканчиваться"],
        "answer": "Исполняться / сбываться"
    },
    {
        "question": "Что значит выражение «um die Wette»?",
        "options": ["Наперегонки / на спор", "По кругу", "Вокруг замка", "С трудом"],
        "answer": "Наперегонки / на спор"
    },
    {
        "question": "Переведите «Lust auf etwas haben»:",
        "options": ["Хотеть / иметь желание полакомиться чем-то", "Бояться чего-то", "Быть против чего-то", "Забыть про что-то"],
        "answer": "Хотеть / иметь желание полакомиться чем-то"
    },
    {
        "question": "Переведите «in Ohnmacht fallen»:",
        "options": ["Падать в обморок", "Уходить в отпуск", "Впадать в ярость", "Засыпать"],
        "answer": "Падать в обморок"
    },
    {
        "question": "Что значит «kurz entschlossen»?",
        "options": ["Быстро решившись / не долго думая", "Коротко сказав", "Случайно", "Едва успев"],
        "answer": "Быстро решившись / не долго думая"
    },
    {
        "question": "Что означает «sich vor jemandem aufbauen»?",
        "options": ["Встать во весь рост перед кем-то", "Прятаться за чьей-то спиной", "Строить дом рядом", "Обходить стороной"],
        "answer": "Встать во весь рост перед кем-то"
    },
    {
        "question": "Как переводится «jemandem Angst machen»?",
        "options": ["Пугать кого-то / нагонять страх", "Успокаивать кого-то", "Смешить кого-то", "Искать кого-то"],
        "answer": "Пугать кого-то / нагонять страх"
    },
    {
        "question": "Переведите фразовый глагол «jemanden loswerden»:",
        "options": ["Избавиться от кого-то", "Потерять кого-то", "Найти кого-то", "Пригласить кого-то"],
        "answer": "Избавиться от кого-то"
    },
    {
        "question": "Что значит «sich auf den Weg machen» (macht sich auf)?",
        "options": ["Отправляться в путь", "Заблудиться", "Строить дорогу", "Останавливаться на ночлег"],
        "answer": "Отправляться в путь"
    },

    # 2. Разговорные выражения и эмоции
    {
        "question": "Что означает эмоция «So ein Mist!»?",
        "options": ["Вот досада! / Чёрт возьми!", "Какая красота!", "Вот это да!", "Как интересно!"],
        "answer": "Вот досада! / Чёрт возьми!"
    },
    {
        "question": "Что значит вопрос «Was soll der Unsinn?»?",
        "options": ["Что это за глупости / дичь?", "Сколько это стоит?", "Где мы находимся?", "Кто это сделал?"],
        "answer": "Что это за глупости / дичь?"
    },

    # 3. Глаголы
    {
        "question": "Что делает дракон, когда «schmollt»?",
        "options": ["Дуется / капризничает", "Смеётся", "Улетает", "Громко рычит"],
        "answer": "Дуется / капризничает"
    },
    {
        "question": "Что делает дракон, когда «grummelt»?",
        "options": ["Тихо ворчит / бурчит", "Громко поёт", "Чихает", "Танцует"],
        "answer": "Тихо ворчит / бурчит"
    },
    {
        "question": "Глагол «zischeln» означает:",
        "options": ["Шипеть / прошипеть", "Громко кричать", "Шептаться обо всём", "Свистеть"],
        "answer": "Шипеть / прошипеть"
    },
    {
        "question": "Что происходит, когда что-то «qualmt»?",
        "options": ["Густо дымит / валит дым", "Взрывается", "Искрится", "Замерзает"],
        "answer": "Густо дымит / валит дым"
    },
    {
        "question": "Что делает снежинка, когда «purzelt»?",
        "options": ["Кувыркается / вываливается", "Быстро летит вверх", "Тает в воздухе", "Застывает"],
        "answer": "Кувыркается / вываливается"
    },
    {
        "question": "Глагол «schlängeln» (sich) означает:",
        "options": ["Извиваться кольцами (как змея/дракон)", "Прыгать на месте", "Бежать по прямой", "Прятаться в нору"],
        "answer": "Извиваться кольцами (как змея/дракон)"
    },
    {
        "question": "Что делает дракон, когда «speit Feuer»?",
        "options": ["Изрыгает / плюёт пламя", "Тушит огонь", "Разводит костёр", "Глотает угли"],
        "answer": "Изрыгает / плюёт пламя"
    },
    {
        "question": "Глагол «schleifen» в контексте текста означал:",
        "options": ["Волочить / тащить по земле", "Точить меч", "Быстро бежать", "Ломать"],
        "answer": "Волочить / тащить по земле"
    },
    {
        "question": "Что произошло, когда снеговик «weggeschmolzen» ist?",
        "options": ["Он растаял", "Он сломался", "Его унесло ветром", "Его украли"],
        "answer": "Он растаял"
    },

    # 4. Составные слова (Komposita)
    {
        "question": "Переведите «die Sommerferien»:",
        "options": ["Летние каникулы", "Зимние праздники", "Солнечный день", "Летний отдых в горах"],
        "answer": "Летние каникулы"
    },
    {
        "question": "Переведите составное слово «der Zauberlehrling»:",
        "options": ["Ученик чародея / подмастерье", "Великий маг", "Волшебная палочка", "Легенда о магии"],
        "answer": "Ученик чародея / подмастерье"
    },
    {
        "question": "Что такое «das Kostümfest»?",
        "options": ["Костюмированный праздник", "Официальный приём", "Спортивный турнир", "Детский концерт"],
        "answer": "Костюмированный праздник"
    },
    {
        "question": "Переведите «der Feuerdrache»:",
        "options": ["Огнедышащий дракон", "Лесной змей", "Водяной монстр", "Огненный шар"],
        "answer": "Огнедышащий дракон"
    },
    {
        "question": "Что такое «der Schneemann»?",
        "options": ["Снеговик", "Дед Мороз", "Снежный обвал", "Ледяной дворец"],
        "answer": "Снеговик"
    },
    {
        "question": "Переведите «der Schlossbewohner»:",
        "options": ["Обитатель / житель замка", "Стражник замка", "Строитель замка", "Гость замка"],
        "answer": "Обитатель / житель замка"
    },
    {
        "question": "Что такое «der Flammenwerfer» в сказке?",
        "options": ["Огнедышащее чудовище / огнемёт", "Костёр", "Факел", "Печь"],
        "answer": "Огнедышащее чудовище / огнемёт"
    },
    {
        "question": "Переведите «der Hofstaat»:",
        "options": ["Придворные / свита", "Королевство", "Замковый двор", "Главный повар"],
        "answer": "Придворные / свита"
    },
    {
        "question": "Что такое «die Schneeflocke»?",
        "options": ["Снежинка", "Снеговик", "Сугроб", "Метель"],
        "answer": "Снежинка"
    },
    {
        "question": "Переведите «die Schlossterrasse»:",
        "options": ["Терраса замка", "Замковая башня", "Ворота замка", "Подвал замка"],
        "answer": "Терраса замка"
    }
]

# Инициализация состояния
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.questions = VOCABULARY.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.answered = False
    st.session_state.selected_option = None

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.questions = VOCABULARY.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.answered = False
    st.session_state.selected_option = None

q_index = st.session_state.current_index
total_questions = len(st.session_state.questions)

if q_index < total_questions:
    st.progress((q_index) / total_questions)
    current_q = st.session_state.questions[q_index]
    
    st.subheader(f"Вопрос {q_index + 1} из {total_questions}")
    st.write(f"### {current_q['question']}")

    # Сохраняем перемешанные варианты ответов
    options_key = f"options_{q_index}"
    if options_key not in st.session_state:
        opts = current_q['options'].copy()
        random.shuffle(opts)
        st.session_state[options_key] = opts
    
    options = st.session_state[options_key]

    selected = st.radio("Выберите вариант ответа:", options, key=f"radio_{q_index}", disabled=st.session_state.answered)

    if not st.session_state.answered:
        if st.button("Ответить", type="primary"):
            st.session_state.answered = True
            st.session_state.selected_option = selected
            if selected == current_q['answer']:
                st.session_state.score += 1
            st.rerun()
    else:
        if st.session_state.selected_option == current_q['answer']:
            st.success("✨ Правильно!")
        else:
            st.error(f"❌ Неправильно. Правильный ответ: **{current_q['answer']}**")

        if st.button("Следующий вопрос ➡️"):
            st.session_state.current_index += 1
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.rerun()

else:
    st.progress(1.0)
    st.balloons()
    st.header("🎉 Игра окончена!")
    score = st.session_state.score
    st.subheader(f"Ваш результат: **{score}** из **{total_questions}**")

    if score == total_questions:
        st.success("🏆 Идеально! Вы выучили все слова!")
    elif score >= total_questions // 2:
        st.info("👍 Отличный результат!")
    else:
        st.warning("📚 Стоит пройти викторину еще раз.")

    if st.button("Пройти викторину заново 🔄"):
        restart_quiz()
        st.rerun()
