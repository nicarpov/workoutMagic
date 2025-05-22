exercises = [
        {
            "id": 1,
            "name": "Отжимания от пола",
            "muscle_groups": [ "грудь", "трицепцы"],
            "equipment": ["пол", "кроссовки"]
        },
        {
            "id": 2,
            "name": "Приседания со штангой",
            "muscle_groups": [ "квадрицепцы", "спина"],
            "equipment": ["штанга"]
        }
    ]

def  getExerciseInfo(id: int):
    try:
        return next(filter(lambda x: x['id'] == id, exercises))
    except StopIteration:
        return {}
