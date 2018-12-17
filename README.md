# Code for the paper "Diversity in Fashion Recommendation Using Semantic Parsing" (ICIP 2018)

This repository contains the code for the research paper titled ["Diversity in Fashion Recommendation Using Semantic Parsing"](https://sagarverma.github.io/others/icip18-fashion-diversity.pdf) by Sagar Verma, Sukhad Anand, Chetan Arora, and Atul Rai.

## Requirements
The code has been test on:

- Nvidia P5000 GPU
- Ubuntu 16.04 LTS
- [Pytorch](https://pytorch.org/) v0.4.0
- Opencv 3.0


## Model architecture
<img src="https://sagarverma.github.io/others/staqu_st_ten_arch.jpg">

## Dataset
1. [Fashion144k](https://esslab.jp/~ess/en/data/fashion144k_stylenet/)
2. [Fashion550k](https://esslab.jp/~ess/en/data/fashion550k/)
3. [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)
4. [Modified labels](https://drive.google.com/drive/folders/1WqK1e18roNaSSD2uia4axdTQQ3-hvkDO?usp=sharing)

## Description of files:

1 train.py : This file contains the code for training the model.
2 test.py : This file contains the code for testing the model on deep fashion dataset.
3 extract_features.py : This file contains the code for extracting features using the network from the images which can then
be compared to get the testing accuracy.

## Training:
1. Create a numpy file containing the train ids of the images on which the model has to be trained.
2. Create a numpy file containing the labels corresponding to trainids of the images used for training.
3. Give the created numpy files as input to the training script to begin the training.
4. Train the model until loss converges (40-50 epochs)

## Testing (to reproduce the results as in the research paper):

For each category (examples trousers etc)
1. Extract features from images corresponding to all categories and store them in a dictionary     
2. Get top 100 candidates for each image using stylenet and euclidean distance as a measure.
3. Use the euclidean distance as a measure to get the top-k accuracy from the extracted features.

## Trained weights

[Weigths](https://drive.google.com/drive/folders/1WqK1e18roNaSSD2uia4axdTQQ3-hvkDO?usp=sharing)

## Publication

S. Verma, S. Anand, C. Arora, and A. Rai, &quot;Diversity in Fashion Recommendation Using Semantic Parsing.&quot; <i>International Conference on Image Processing (**ICIP**)</i> (Oral) [PDF](https://sagarverma.github.io/others/icip18-fashion-diversity.pdf)


## Citation
Please cite the following paper if you find this repository useful.
```
@article{Sagar2018fashion,
  author      = {Sagar Verma and
                 Sukhad Anand and
                 Chetan Arora and
                 Atul Rai},
  title       = {Diversity in Fashion Recommendation Using Semantic Parsing},
  booktitle   = {ICIP},
  year        = {2018}
}
```

## Contact
For any queries, please contact
```
Sagar Verma: sagar15056@iiitd.ac.in
