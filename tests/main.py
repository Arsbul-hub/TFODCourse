import cv2
import numpy as np
import os

def overlay_images(image1_filename, image2_filename, output_filename, opacity=1.0, blend_mode='multiply'):
    # Получаем абсолютные пути к изображениям и результату
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image1_path = os.path.join(script_dir, image1_filename)
    image2_path = os.path.join(script_dir, image2_filename)
    output_path = os.path.join(script_dir, output_filename)

    # Загружаем изображения
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Проверяем, что изображения были успешно загружены
    if img1 is None or img2 is None:
        raise ValueError("Не удалось загрузить изображение. Проверьте пути к файлам.")

    # Проверяем, что размеры изображений совпадают
    if img1.shape[:2] != img2.shape[:2]:
        height, width, channels = img2.shape
        img1 = cv2.resize(img1, (width, height), interpolation = cv2.INTER_AREA)

        #raise ValueError("Размеры изображений должны совпадать")
    # Приводим opacity к диапазону [0, 1]
    opacity = max(0.0, min(1.0, opacity))

    # Отключаем канал R (красный) в изображении img2
    img2[:, :, 2] = 0  # Устанавливаем все значения в канале R в 0

    # Применяем режим наложения
    if blend_mode == 'multiply':
        result = cv2.multiply(img1, img2, scale=1/255.0)
    elif blend_mode == 'screen':
        result = cv2.addWeighted(img1, 1-opacity, img2, opacity, 0)
    elif blend_mode == 'add':
        result = cv2.add(img1, img2)
    elif blend_mode == 'subtract':
        result = cv2.subtract(img1, img2)
    elif blend_mode == 'divide':
        result = cv2.divide(img1, img2)
    elif blend_mode == 'difference':
        result = cv2.absdiff(img1, img2)
    elif blend_mode == 'overlay':
        result = cv2.addWeighted(img1, 1-opacity, img1 * img2 + (1 - img1) * img1, opacity, 0)
    elif blend_mode == 'lighten':
        result = cv2.max(img1, img2)
    elif blend_mode == 'darken':
        result = cv2.min(img1, img2)
    else:
        raise ValueError("Неподдерживаемый режим наложения. Доступные режимы: 'multiply', 'screen', 'add', 'subtract', 'divide', 'difference', 'overlay', 'lighten', 'darken'.")

    # Сохраняем результат
    cv2.imshow("window_name", result)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()
    cv2.imwrite(output_path, result)

# Пример использования
overlay_images("./test2.jpg", "./test1.jpg", "output.png", opacity=1.0, blend_mode='difference')