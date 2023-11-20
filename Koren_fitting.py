# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:05:37 2023

@author: Chiffa
"""
import numpy as np
from math import cos, log, exp
from scipy.optimize import curve_fit
import json
import matplotlib.pyplot as plt
from  ImageStorage import ImageStorage
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
def get_data_from_lib(tube_name):
    with open ('TubeIVlib.json', 'r') as file:
        TubeIVdict = json.load(file)
   
    IV_data = TubeIVdict.get(str(tube_name))
    
    U_gk_ = list(IV_data.keys())

    U_gk_ =[float(u) for u in U_gk_]
    I_a_list = []
    U_ak_list = []
    U_gk_list = []
    for U_gk_i in U_gk_:
        for tuple_UI in  IV_data.get(str(U_gk_i)):
            U_ak_i, I_a_i = tuple_UI 
            I_a_list.append(I_a_i/1000)
            U_ak_list.append(U_ak_i)
            U_gk_list.append( U_gk_i)
    I_array = np.array(I_a_list)
    Uak = np.array(U_ak_list)
    Ugk = np.array( U_gk_list)
    U_array = np.vstack( (Ugk, Uak) )
    
    return  U_array, I_array, Uak, Ugk
    
def Koren_eq(U, mu, Ex, K_g1, K_p, K_vb, V_ct):
    Ugk, Uak = U
    E1 = (Uak/K_p)*np.log( 1 + np.exp( K_p*( (1/mu) + (Ugk + V_ct)/(K_vb + Uak**2)**0.5  ) ) ) 
    Ia = E1**Ex*(1+ np.sign(E1))/K_g1
    # Ia = E1**Ex*2/K_g1
    return Ia

# Bounds = ((70, 1, 900, 300, 100 ),(150, 2, 2000, 800, 500))
# MU=33 KG1=2603.17 KP=305.48 KVB=57.09 VCT=0.3363 EX=1.792
# Initial_guess =[33,	1.792,	2603.17,	 	305.48,	57.09] 
# , p0 = Initial_guess, bounds=Bounds
# https://www.diyaudio.com/community/threads/vacuum-tube-spice-models.243950/page-133
def fit_Koren(U_array, I_array):
    Koren_parameters, pcov_fit  = curve_fit(Koren_eq, U_array, I_array, maxfev = 1500000)
    perr = np.sqrt(np.diag(pcov_fit))
    return Koren_parameters, perr

def function_fit(tube_name):
    U_array, I_array, Uak, Ugk = get_data_from_lib(str(tube_name))
    
    Koren_parameters, perr = fit_Koren(U_array, I_array)
    Koren_parameters = [round(p, 3) for p in Koren_parameters]
    perr = [round(p, 3) for p in perr]
    (mu, Ex, K_g1, K_p, K_vb, V_ct) = Koren_parameters
    (mu_err, Ex_err, K_g1_err, K_p_err, K_vb_err, V_ct_err) = perr
    print('Koren_parameters', '\n',
          '\n',
          'mu', mu, '+/-' , mu_err ,'\n',
          'Ex',Ex,'+/-' ,Ex_err,'\n',
          'K_g1',K_g1,'+/-' ,K_g1_err, '\n',
          'K_p', K_p,'+/-' , K_p_err,'\n',
          'K_vb', K_vb,'+/-',K_vb_err ,'\n',
          'V_ct', V_ct, '+/-',V_ct_err ,'\n',
          )
  
    with open ('TubeIVlib.json', 'r') as file:
            TubeIVdict = json.load(file)
       
    IV_data = TubeIVdict.get(str(tube_name))
    
    
    # Koren_parameters = [33,  1.792, 2603.1, 305.48, 57.09, 0.3363 ]
    for U_gk_i in list(IV_data.keys()):
        IV_list = IV_data.get(str(U_gk_i))
        I_a_list = []
        U_ak_list = []
        for tuple_UI in  IV_list:
                    U_ak_i, I_a_i = tuple_UI 
                    I_a_i = I_a_i/1000.0
                    I_a_list.append(I_a_i)
                    U_ak_list.append(U_ak_i)
                    
        U_ak_model = np.linspace(min(U_ak_list), max((U_ak_list)), 10*len(U_ak_list))
        I_model = []
        for U_ak_i in U_ak_model:
            I_model_i = Koren_eq((float(U_gk_i),  U_ak_i), *Koren_parameters)
            I_model.append(I_model_i )
  
        fig = plt.figure(0)
        plt.plot(U_ak_model , np.array(I_model),   U_ak_list, I_a_list )
        fig.show()
        fig1 = plt.figure(1)
        plt.plot(U_ak_model , np.array(I_model) )
        plt.savefig('modeled_curve.png', bbox_inches='tight')
        modeled_curve_image  = Image.open('modeled_curve.png')   
        modeled_curve_image  = modeled_curve_image.convert("RGBA")
        # 
        fig1.show()
        fig2 = plt.figure(2)
        datasheet_image = ImageStorage.image

            # im = plt.imread('6n1p-e.jpg')
            # im =  plt.imread(datasheet_image)
        I_model = [i*1000 for i in I_model]
        
        
        plt.imshow( datasheet_image, extent=[0, 350, 0, 100], zorder=0)
        plt.plot( U_ak_model , I_model, zorder=1)
 
        fig2.show()
        fig2.savefig('comparsion.png') 
        image  = Image.open('comparsion.png')   
        image  = image.convert("RGBA")
        qim = ImageQt(image )
         
        pixmap =QtGui. QPixmap(QtGui.QImage(qim))
        ImageStorage.crop_result =  pixmap     
        
    modeled_curve_image  = Image.open('modeled_curve.png')  
    modeled_curve_image  = modeled_curve_image.convert("RGBA")
    width, height = modeled_curve_image.size
 
        # Setting the points for cropped image
    left = 51
    top = 0.025*height
    right = width-8
    bottom = 0.92*height
         
        # Cropped image of above dimension
        # (It will not change original image)
        
        
    modeled_curve_image= modeled_curve_image.crop((left, top, right, bottom))
    width, height = datasheet_image.size
    modeled_curve_image = modeled_curve_image.resize( (width, height) )
    new_img = Image.blend(datasheet_image, modeled_curve_image, 0.5)
    new_img.show()
