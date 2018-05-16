import numpy as np
import operator
import pickle

##Directory containing the images which have to be compared
IMAGES_DIR = "datasets/DeepFashion/InShop/Img/"
 
##Directory containing the dictionaries for getting test accuracy 
DICTIONARY_DIR = "/media/Drive2/Staq/tests/in_shop/"

##dictionary containing the street images along with their respective labels
street_pickle = open("/media/Drive2/Staq/tests/in_shop/street.pickle",'rb')
##dictionary containing the street images along with their respective labels
shop_pickle = open("/media/Drive2/Staq/tests/in_shop/shop.pickle",'rb')
street_dict = pickle.load(street_pickle)
shop_dict = pickle.load(shop_pickle)

##measuring the respective accuracy
UNDER_20 = 0
UNDER_10 = 0
UNDER_5 = 0
UNDER_3 = 0
TOTAL = 0

h = 0
for key in shop_dict:
    if(key=='MEN'):
        dictdir = dictdi + 'men/'
    
    shop_images = shop_dict[key]
    street_images = street_dict[key]
    for i in range(len(street_images)):
        
        category_street = street_images[i].split('/')[2]
        
        ##Load the features for a particular image along with the scores of the labels to find which features correspond to which labels
        feat = dictdir + 'street/' + street_images[i].split('/')[2] +  '_' + street_images[i].split('/')[-1][:-4] +'_feature.npy'
        out = dictdir + 'street/' + street_images[i].split('/')[2] + '_' + street_images[i].split('/')[-1][:-4] +'_output.npy'
        locations = dictdir + 'street/' + street_images[i].split('/')[2] + '_' + street_images[i].split('/')[-1][:-4] +'_location.npy'
        
        input_ = street_images[i]
        
        try:
            street_feat = np.load(feat)
        except:
            continue
        
        street_out = np.load(out)
        street_loc = np.load(locations)
        
        ##sort the scores of the labels
        sorted_street = np.sort(street_out)
        sorted_street = sorted_street[::-1]
        
        ##GET top 6 labels corresponding to their features
        street_final_regions = []
        predict_street = np.zeros(59)
        for k in range(59):
            a = (street_out[k])
            b = sorted_street[6]
            if(a > b):
                predict_street[k] = 1
                street_final_regions.append(street_feat[street_loc[k]])
            else:
                street_final_regions.append([])
        
        diclist = {}
        
        final_images = []
        c = 0
        chklist = {}
        ##Get shop images of the category same as shop images
        for j in range(len(shop_images)):
            category_shop = shop_images[j].split('/')[2]
            
            if(category_shop!=category_street):
                continue
            name = shop_images[j].split('/')[2] + '_' + shop_images[j].split('/')[-2] + '_' + shop_images[j].split('/')[-1][:-4]
            if name in chklist:
                continue
            else:
                chklist[name] = 1
            final_images.append(shop_images[j])
            c = c + 1
            if(c==100):
                break
        ##GEt the features along with the respective features of shop images
        for j in range(len(final_images)):
            
            feat = dictdir + 'shop/' + final_images[j].split('/')[2] + '_' + final_images[j].split('/')[-1][:-4] +'_feature.npy'
            out = dictdir + 'shop/' + final_images[j].split('/')[2] + '_' +  final_images[j].split('/')[-1][:-4] +'_output.npy'
            locations = dictdir + 'shop/' + final_images[j].split('/')[2] + '_' + final_images[j].split('/')[-1][:-4] +'_location.npy'
            name_ = final_images[j].split('/')[2] +  '_' + final_images[j].split('/')[-1][:-4]
            name_ = name_.split('_')
            name = ''
            for i in range(len(name_) - 1):
                name = name  + name_[i] +'_'

            try:
                shop_feat = np.load(feat)
                shop_out = np.load(out)
                shop_locations = np.load(locations)
            except:
                if(j==0):
                    print ("not_found")
                    break
                else:
                    continue
            sorted_shop = np.sort(shop_out)[::-1]
            shop_final_regions = []
            predict_shop = np.zeros(59)
            for k in range(59):
                a = (shop_out[k])
                b = sorted_shop[6]
                if(a > b):
                    predict_shop[k] = 1
                    shop_final_regions.append(shop_feat[shop_locations[k]])
                else:
                    shop_final_regions.append([])
            d = 0
            cnt = 0
            ##Calculate euclidean distance of shop image features with street image features
            for k in range(len(predict_street)):
                if(predict_shop[k] == predict_street[k] and predict_shop[k]==1):
                    d1 = np.linalg.norm(shop_final_regions[k]-street_final_regions[k])
                    d1 = d1.sum()*10000
                    cnt = cnt + 1
                    d = d + d1
            if(cnt>0):
                d = d/cnt
            else:
                d = 100
            diclist[name] = d
            
        sorted_x = {}
        ##sort the calculated distances
        sorted_x = sorted(diclist.items(), key=operator.itemgetter(1))
        c = 0
        for key1 in sorted_x:
            if(key1[0]==result):
                total = total + 1
                
                if(c<=20):
                    under_20 = under_20 + 1
                if(c<=3):
                    under_3 = under_3 + 1
                if(c<=5):
                    under_5 = under_5 + 1
                if(c<=10):
                    under_10 = under_10 + 1
                    
    print ('under 30:')
    print (under_20)
    print ('under 10:')
    print (under_10)
    print ('under_5:')
    print (under_5)
    print ('under_3:')
    print (under_3)
    print ('total:')
    print (total)