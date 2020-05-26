#! usr/bin/python3
#! coding: utf-8
# font_link: https://www.topster.es/
import os
import time
#if sys.platform=='linux':
R='\033[31m'
G='\033[32m'
GL='\033[32;1m'
B='\033[34m'
BA = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue ligth
W='\033[0;1m'
def esp():
   recom=['Procura cerrar siempre el caño cuando no lo uses',
   'Deposita la basura en tachos específicos',
   'Reduce el uso de transporte público. Es preferible usar bicicleta o caminar',
   'Disminuye el uso de plásticos',
   'Si ves a alguien atentar contra el ambiente, denúncialo!',
   'Experimenta en el mundo del reciclaje',
   'Reusa productos y transformalos en cosas increíbles',
   'Siembra un árbol, el planeta te lo agradecera'] 
   for i in recom:
       print(BB,'[+]',i)
       time.sleep(1)
def eng():
    recom=["Always try to close the spout when you don't use it ",
    "Deposit the garbage in specific bins",
    'Reduce the use of public transport. It is preferable to use a bicycle or walk ', 'Decrease the use of plastics', 'If you see someone attack the environment, report it!',
    'Experiment in the world of recycling', 
    'Reuse products and transform them into incredible things',
    'Plant a tree, the planet will thank you'         
    ]  
    for j in recom:   
        print(BB,'[+]',j)
        time.sleep(1)
os.system('clear')

title_sp='''
                         ,,         ,,                                               
  .g8"""bgd               db       `7MM                                               
.dP'     `M                          MM                                               
dM'       ` `7MM  `7MM  `7MM    ,M""bMM   .gP"Ya  `7MMpMMMb.pMMMb.   ,pW"Wq.  ,pP"Ybd 
MM            MM    MM    MM  ,AP    MM  ,M'   Yb   MM    MM    MM  6W'   `Wb 8I   `" 
MM.           MM    MM    MM  8MI    MM  8M""""""   MM    MM    MM  8M     M8 `YMMMa. 
`Mb.     ,'   MM    MM    MM  `Mb    MM  YM.    ,   MM    MM    MM  YA.   ,A9 L.   I8 
  `"bmmmd'    `Mbod"YML..JMML. `Wbmd"MML. `Mbmmd' .JMML  JMML  JMML. `Ybmd9'  M9mmmP' 
                                                                                      
           ,,                   ,,                                                 
         `7MM                 `7MM                                  mm             
           MM                   MM                                  MM             
 .gP"Ya    MM      `7MMpdMAo.   MM   ,6"Yb.  `7MMpMMMb.   .gP"Ya  mmMMmm   ,6"Yb.  
,M'   Yb   MM        MM   `Wb   MM  8)   MM    MM    MM  ,M'   Yb   MM    8)   MM  
8M""""""   MM        MM    M8   MM   ,pm9MM    MM    MM  8M""""""   MM     ,pm9MM  
YM.    ,   MM        MM   ,AP   MM  8M   MM    MM    MM  YM.    ,   MM    8M   MM  
 `Mbmmd' .JMML.      MMbmmd'  .JMML.`Moo9^Yo..JMML  JMML. `Mbmmd'   `Mbmo `Moo9^Yo.
                     MM                                                            
                   .JMML.                                                          
                                                                                    
'''
title_en="""
                                                                                                   ,...    
MMP""MM""YMM          `7MM                                                                       .d' ""    
P'   MM   `7            MM                                                                       dM`       
     MM       ,6"Yb.    MM  ,MP' .gP"Ya       ,p6"bo   ,6"Yb.  `7Mb,od8  .gP"Ya       ,pW"Wq.   mMMmm      
     MM      8)   MM    MM ;Y   ,M'   Yb     6M'  OO  8)   MM    MM' "' ,M'   Yb     6W'   `Wb   MM        
     MM       ,pm9MM    MM;Mm   8M""""""     8M        ,pm9MM    MM     8M""""""     8M     M8   MM        
     MM      8M   MM    MM `Mb. YM.    ,     YM.    , 8M   MM    MM     YM.    ,     YA.   ,A9   MM        
   .JMML.    `Moo9^Yo..JMML. YA. `Mbmmd'      YMbmd'  `Moo9^Yo..JMML.    `Mbmmd'      `Ybmd9'  .JMML.      
 
           ,,                                  ,,                                        
  mm    `7MM                                `7MM                                  mm    
  MM      MM                                  MM                                  MM    
mmMMmm    MMpMMMb.   .gP"Ya      `7MMpdMAo.   MM   ,6"Yb.  `7MMpMMMb.   .gP"Ya  mmMMmm  
  MM      MM    MM  ,M'   Yb       MM   `Wb   MM  8)   MM    MM    MM  ,M'   Yb   MM    
  MM      MM    MM  8M""""""       MM    M8   MM   ,pm9MM    MM    MM  8M""""""   MM    
  MM      MM    MM  YM.    ,       MM   ,AP   MM  8M   MM    MM    MM  YM.    ,   MM    
  `Mbmo .JMML  JMML. `Mbmmd'       MMbmmd'  .JMML.`Moo9^Yo..JMML  JMML. `Mbmmd'   `Mbmo 
                                   MM                                                   
                                 .JMML.                                                                                                                                                          
 """                                                                                                         
print(BA+'\nWelcome...           Bienvenido...\n')
print(W+'''
Aqui te daremos recomendaciones para el cuidado del ambiente	
Here we give u recommendation to care the planet
''')
print(G+'Before start tell me ur language spanish or english')
while True:
    n=input(G+'Select a language (en/sp): ')
    if n.lower()=='en':
        print(title_en)
        print('\n')
        eng()
        break
    elif n.lower()=='sp':
        print(title_sp)
        print('\n')
        esp()
        break 
    else:
        print(R+'Input invalidated')
        print(R+'Entrada incorrecta')
        continue       
    
     