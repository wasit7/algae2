by Wasit Limprasert

# /marker/algae_marker.py 
To label objects,

1. put all images (*.jpg) in folder /dataset
2. Press number key (0 to 9) to select calss of object. There are avialable 10 classes
3. [left click] or ctrl + [left click] on image to label the area of object
4. alt + [left click] to remove the label
5. space bar to save
6. esc to close the window

# notebook.ipynb
The marked images from /marker/dataset must be moved to /storage/traning or /storage/evaluation
1. Prepare: To prepare the feature vectors (x) and labels (y). 
2. Train: To train a tree and save to dataset/timestamp.tree. The cross_val_score() can be commented to accelerate the training time
3. Combine: To cimbined all tree into dataset/forest.pic
4. Predict: and finally, using forest.pic to identify and count objects








