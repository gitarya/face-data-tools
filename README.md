Here provide some tools to modify your face datasets.

## Requirements
```
pip install -r requirements.txt
```

##  Rename or resize your dataset
You can use organ_data.py to rename your original image name as class_number.png like this:
```
/home/david/datasets/my_dataset/test
├── Ariel_Sharon
│   ├── Ariel_Sharon_0006.png
│   ├── Ariel_Sharon_0007.png
│   ├── Ariel_Sharon_0008.png
├── Arnold_Schwarzenegger
│   ├── Arnold_Schwarzenegger_0006.png
...
...
```
To rename your image, just run this:
```
python organ_data.py --data_dir your_data_folder --save_dir your_path_to_save_renamed_data
```
The path should end with '/'.
if you want to resize your dataset, just set the argument resize as True and set the resize_num argument. The resize operator wouldn't rename your datasets.
```
python organ_data.py --data_dir your_data_folder --save_dir your_path_to_save_rensize_data
--resize True --resize_num 112
```


## Generate the pairs.txt
if you want to generate pairs.txt like lfw datasets, you should organize your data structure as above(the image name is consisted of folder name and number). Then you can use generate_pairs.py to generate pairs
```
python generate_pairs.py --data_dir your_data_path --save_dir your_path_to_save_pairs
```
