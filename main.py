import random

vocabulary = [
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
        "question": "Переведите фразовый глагол «jemanden loswerden»:",
        "options": ["Избавиться от кого-то", "Потерять кого-то", "Найти кого-то", "Пригласить кого-то"],
        "answer": "Избавиться от кого-то"
    },
    {
        "question": "Что означает эмоция «So ein Mist!»?",
        "options": ["Вот досада! / Чёрт возьми!", "Какая красота!", "Вот это да!", "Как интересно!"],
        "answer": "Вот досада! / Чёрт возьми!"
    },
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
        "question": "Глагол «schleifen» в тексте означал:",
        "options": ["Волочить / тащить по земле", "Точить меч", "Быстро бежать", "Ломать"],
        "answer": "Волочить / тащить по земле"
    },
    {
        "question": "Переведите составное слово «der Zauberlehrling»:",
        "options": ["Ученик чародея / подмастерье", "Великий маг", "Волшебная палочка", "Легенда о магии"],
        "answer": "Ученик чародея / подмастерье"
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
    }
]

def run_quiz():
    score = 0
    questions = vocabulary.copy()
    random.shuffle(questions)
    
    print("=== ВИКТОРИНА ПО НЕМЕЦКИМ СЛОВАМ ===\n")
    
    for i, item in enumerate(questions, 1):
        print(f"Вопрос {i}/{len(questions)}: {item['question']}")
        
        options = item['options'].copy()
        random.shuffle(options)
        
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
            
        while True:
            try:
                user_choice = int(input("\nВаш ответ (введите номер 1-4): "))
                if 1 <= user_choice <= 4:
                    break
                print("Пожалуйста, введите число от 1 до 4.")
            except ValueError:
                print("Нужно ввести цифру!")
                
        selected_option = options[user_choice - 1]
        if selected_option == item['answer']:
            print("✨ Правильно!\n")
            score += 1
        else:
            print(f"❌ Неправильно. Правильный ответ: {item['answer']}\n")
            
    print("=" * 35)
    print(f"Игра окончена! Ваш результат: {score} из {len(questions)}")
    if score == len(questions):
        print("🏆 Отличный результат! Все слова усвоены!")
    elif score >= len(questions) // 2:
        print("👍 Хороший результат! Повторите ещё разок для закрепления.")
    else:
        print("📚 Стоит ещё раз просмотреть список слов.")

if __name__ == "__main__":
    run_quiz()
