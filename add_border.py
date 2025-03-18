import os
import math
from PIL import Image, ImageOps

def add_custom_border(image_path, output_path, border=(0, 0), border_color='white'):
    """
    Добавляет цветное поле (рамку) к изображению с возможностью настройки ширины по вертикали и горизонтали.

    :param image_path: Путь к исходному изображению.
    :param output_path: Путь для сохранения нового изображения.
    :param border: Кортеж с размерами рамки (горизонтальная, вертикальная).
    :param border_color: Цвет рамки в формате RGB (например, (255, 0, 0) — красный).
    """
    # Распаковываем значения ширины рамки
    horizontal_border, vertical_border = border

    # Открываем изображение
    with Image.open(image_path) as img:
        # Создаем рамку с разными размерами по сторонам
        bordered_image = ImageOps.expand(
            img,
            border=(horizontal_border, vertical_border, horizontal_border, vertical_border),
            fill=border_color
        )
        # Сохраняем результат
        bordered_image.save(output_path)

# Пример использования
if __name__ == "__main__":
    input_folder = input('Выберите папку с исходными изображениями: ')
    output_folder = input('Выберите папку для сохранения: ')

    minimal_width = 0
    minimal_height = 0
    horizontal_frames = 0
    vertical_frames = 0

    choice = input('Вы хотите выбрать ширину рамки самостоятельно? (да/нет): ')

    if choice == 'да':
        horizontal_frames = input('Введите ширину рамки справа и слева: ')
        vertical_frames = input('Введите ширину рамки справа и слева: ')
    else:
        minimal_width = input('Введите минимальную ширину изображения: ')
        minimal_height = input('Введите минимальную высоту изображения: ')

    border_color = input('Выберите цвет рамки: ')

    # Создаем выходную папку, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Проходим по всем файлам в папке
    for filename in os.listdir(input_folder):
        # Проверяем, является ли файл изображением (по расширению)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Добавляем рамку и сохраняем
            if choice == 'нет':
                with Image.open(input_path) as img:
                    horizontal_frames, vertical_frames = img.size

                horizontal_frames -= int(minimal_width)
                vertical_frames -= int(minimal_height)
                if horizontal_frames > 0:
                    horizontal_frames = 0
                else:
                   horizontal_frames = math.ceil(abs(horizontal_frames * 0.5))
                if vertical_frames > 0:
                    vertical_frames = 0
                else:
                   vertical_frames = math.ceil(abs(vertical_frames * 0.5))

            border = (horizontal_frames, vertical_frames)

            add_custom_border(input_path, output_path, border, border_color)
            print(f"Обработано: {filename}")