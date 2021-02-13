#!/usr/bin/env python
#!/trinity/shared/opt/python-3.7.1/bin/python3.7
# coding: utf-8
import numpy as np
import pandas as pd
import json
import pickle
import csv
from pandas.io.json import json_normalize
import scipy
import SALib
from SALib.sample import saltelli
import os
import subprocess

def writting_files(str_values, counter):
#     import itertools
    soc,sand,clay,ph,cn,bd = str_values 
    
    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return super(NpEncoder, self).default(obj)

    site_file = './work_kshen/site-min-malino.json' #site-min-kshen-3-layers.json'
    sim_file = './work_kshen/sim-min-malino.json'

#     soil_texture_pd = pd.read_csv('SoilTexture.csv', sep=";") 
#     soil_texture = np.asarray(soil_texture_pd.iloc[:,[0,2,4,5,6,7]])

    with open(site_file) as sf:
        site_data = json.load(sf)

    with open(sim_file) as simf:
        sim_data = json.load(simf)   

    #selecting necessary keys
    keys = list(site_data['SiteParameters']['SoilProfileParameters'][0].keys())
#     texture_keys = list(keys.copy()[i] for i in [3,4,7,8,11])
    our_keys = list(keys.copy()[i] for i in [1,3,4,9,10,11])

    #creating range for every soil parameter
#     organic_carbon_range=np.arange(2.58,6.20,0.4)
#     texture_class_range=list(soil_texture_pd['KA5-class'])
#     pore_volume_range=np.arange(0.48,0.67,0.02)
#     ph_range=np.arange(4.6,6.9,0.25)
#     cn_range=np.arange(10.9,12.4,0.15)
    
    soc=soc
    sand=sand
    clay=clay
    ph=ph
    cn=cn
    bd=bd

#     soil_parameters_range = [organic_carbon_range,texture_class_range,pore_volume_range,
#                              ph_range,cn_range]

    

    soil_parameters_names = ['SOC','Sand', 'Clay', 'pH', 'CN','BD']


    #saving site-file and sim-file
    #for the first key - SoilOrganicCarbon
    # for parameter in range(len(soil_parameters_range)):
#     for soc,ka5,pv,ph,cn in itertools.product(soil_parameters_range[0],soil_parameters_range[1],\
#                                               soil_parameters_range[2],soil_parameters_range[3],soil_parameters_range[4]):

    site_data_copy=site_data.copy()

    #writing main parameters
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[0]][0]=float(soc) 
#     site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]]=ka5
#    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]][0]=float(pv)
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]][0]=float(sand)
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[2]][0]=float(clay)
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[3]][0]=float(ph)
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[4]][0]=float(cn)
    site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[5]][0]=float(bd)



    #writing texture parameters
#     for c in range(len(texture_keys)):
#         data = soil_texture[np.where(soil_texture==ka5)[0][0],:][1:]
#         site_data_copy['SiteParameters']['SoilProfileParameters'][0][texture_keys[c]][0]=data[c]

    #constructing file name 
    SOC_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[0]][0])
#     KA5_value = '_KA5' + str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]])
 #   PV_value = str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]][0])
    sand_value =  str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[1]][0])
    clay_value =  str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[2]][0])
    ph_value =  str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[3]][0])
    CN_value =  str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[4]][0])
    BD_value =  str(site_data_copy['SiteParameters']['SoilProfileParameters'][0][our_keys[5]][0])


    file_name = str(SOC_value)+'_'+str(sand_value)+'_'+str(clay_value)+'_'+str(ph_value)+'_'+str(CN_value)+'_'+str(BD_value)
    site_file_name='site'+'_'+file_name+'.json'


    with open(site_file_name, 'w', encoding='utf-8') as sitef:
        json.dump(site_data_copy, sitef, ensure_ascii=False, indent=4, cls=NpEncoder)

    sim_data_copy=sim_data.copy()
    sim_data_copy['site.json']=site_file_name
    sim_data_copy['output']['file-name']=str(counter)+'out'+'_'+file_name+'.csv'
    sim_file_name='sim'+'_'+file_name+'.json'

    with open(sim_file_name, 'w', encoding='utf-8') as simf:
        json.dump(sim_data_copy, simf, ensure_ascii=False, indent=4, cls=NpEncoder)
    os.system('sh monicarunner.sh') 
problem = {
    'num_vars':6,
    'names':['SOC', 'Sand', 'Clay', 'pH', 'CN', 'BD'],
    'bounds':[[2.58, 5.20],
	      [0.06, 0.92],
	      [0.01, 0.23],
              [4.6, 6.9],
              [10.9, 12.4],
              [1120, 1330]]
}

param_values = saltelli.sample(problem, 100, calc_second_order=True)
counter=1000000
for st in range(len(param_values)):
    writting_files(param_values[st], counter)
    counter+=1
