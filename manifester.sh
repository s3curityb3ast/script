#!/bin/bash
#ToolName:- Manifester
#Author :- Bimohini Panigrahi, Kaustubh Padwad
#Licence :- GPL3
#Description :- This tool will find all the apks in the current directory and fetch all data from manifiest file.


echo -ne      "                                                               
		##   ##   ##   #    # # ###### ######  ####  ##### ###### #####  
		# # # #  #  #  ##   # # #      #      #        #   #      #    # 
		#  #  # #    # # #  # # #####  #####   ####    #   #####  #    # 
		#     # ###### #  # # # #      #           #   #   #      #####  
		#     # #    # #   ## # #      #      #    #   #   #      #   #  
		#     # #    # #    # # #      ######  ####    #   ###### #    # "
	



mkdir temp 
for i in `find . -name *apk*`;do cp -rav $i temp/;done
cd temp
for i in `ls`;do apktool d $i;done
cd temp 
find . ! -name 'AndroidManifest.xml' -type f -exec rm -fr {} +
find . -type f -print0|xargs -0 strings -a --print-file-name > ../manifester_Output.txt
rm -fr temp

