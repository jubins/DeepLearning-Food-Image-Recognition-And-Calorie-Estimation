@jubins
Stpes to run an Image Classifier on Docker Using Tensorflow:

1. Install Docker

2. docker run hello-world

3. docker run -it gcr.io/tensorflow/tensorflow:latest-devel

4. Check Tensorflow:
	# python
	>> import tensorflow
	
5. Retrieve Images:
	# ctrl-D if you're still in Docker and then:
	$ cd $HOME
	$ mkdir tf_files
	$ cd tf_files
	$ curl -O https://goo.gl/NohU7G
	$ gzip -d food_datasets.tar.gz
	$ tar xzf DataSets.tar
	$ cd $HOME/tf_files/DataSets/food_photos
	
6. Link image dataset virtually to tensorflow:
	$docker run -it -v <GitHub Repository Clone Path>/DataSets/food_photos:/tf_files/ImageDataSets/food_photos gcr.io/tensorflow/tensorflow:latest-devel
	# ls /tf_files/DataSets
	food_photos
	
7. Retrieving the Training code:
	# cd /tensorflow
	# git pull

8. Training the Inception model:
	# python tensorflow/examples/image_retraining/retrain.py \
	--bottleneck_dir=/tf_files/ImageDataSets/bottlenecks \
	--how_many_training_steps 500 \
	--model_dir=/tf_files/ImageDataSets/inception \
	--output_graph=/tf_files/ImageDataSets/retrained_graph.pb \
	--output_labels=/tf_files/ImageDataSets/retrained_labels.txt \
	--image_dir /tf_files/DataSets/food_photos

	The retraining script will write out a version of the Inception v3 network with a final layer retrained to your categories to /tmp/output_graph.pb and a text file containing the labels to /tmp/output_labels.txt.

9. Using trained model to predict new images:
	# ctrl-D to exit Docker and then:
	$ curl -L goo.gl/NyNBG5 > $HOME/tf_files/ImageDataSets/label_image.py
	$ docker run -it -v <GitHub Repository Clone Path>/DataSets/test_photos:/tf_files/ImageDataSets/test_photos gcr.io/tensorflow/tensorflow:latest-devel
	
10. Predicting new images:
	# python /tf_files/ImageDataSets/label_image.py /ImageDataSets/test_photos/Pizza/pizza1.jpg
	# python /tf_files/label_image.py /ImageDataSets/test_photos/VegBurger/notburger_cake1.jpg


