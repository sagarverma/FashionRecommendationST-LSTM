DIVERSITY IN FASHION RECOMMENDATION USING SEMANTIC PARSING

This repository contains the code for the research paper titled "DIVERSITY IN FASHION RECOMMENDATION USING SEMANTIC PARSING"
accepted at International conference on image processing(ICIP).

Description of files:

1 train.py : This file contains the code for training the model.
2 test.py : This file contains the code for testing the model on deep fashion dataset.
3 extract_features.py : This file contains the code for extracting features using the network from the images which can then
be compared to get the testing accuracy.

Process for training:
1. Create a numpy file containing the train ids of the images on which the model has to be trained.
2. Create a numpy file containing the labels corresponding to trainids of the images used for training.
3. Give the created numpy files as input to the training script to begin the training.
4. Train the model until loss converges (40-50 epochs)

Process used for testing(To reproduce the results as in the research paper):

For each category (examples trousers etc)
1. Extract features from images corresponding to all categories and store them in a dictionary     
2. Get top 100 candidates for each image using stylenet and euclidean distance as a measure.
3. Use the euclidean distance as a measure to get the top-k accuracy from the extracted features.

The sample numpy files for labels and trainids can be found at:
https://drive.google.com/open?id=1zOAXY5tDG_FLM-yunN11r3VTUrq8c1Ly

The pre-trained model on fashion-550k dataset can be found at:
https://drive.google.com/open?id=1rP9HmsriSiRHoqmP0xQcyVMv70hGPg1G
