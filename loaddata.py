import tensorflow as tf

img_height = 224
img_width = 224

train_data = tf.keras.utils.image_dataset_from_directory(
    "data/train",
    image_size=(img_height, img_width),
    label_mode="categorical")

test_data = tf.keras.utils.image_dataset_from_directory(
    "data/test",
    image_size=(img_height, img_width),
    label_mode="categorical")

valid_data = tf.keras.utils.image_dataset_from_directory(
    "data/valid",
    image_size=(img_height, img_width),
    label_mode="categorical")

class_names = train_data.class_names
print(class_names)