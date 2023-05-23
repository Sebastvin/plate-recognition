from sklearn.model_selection import train_test_split
import os

"""""
Get a list of all the image filenames in the data folder
Folder can download from Google Drive, named 'dataset_cleaned'
""" ""
image_filenames = os.listdir(os.path.join('datasets', 'dataset_cleaned'))

"""""
Split the dataset into training and test sets 80/20
Warning, don't change the values in params train_test_split function 'test_size' and 'random_state'
otherwise the dataset will be different from others!
""" ""
train_filenames, test_filenames = train_test_split(
    image_filenames, test_size=0.2, random_state=42
)
