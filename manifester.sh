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

for f in *.apk; do
    echo "Processing $f ..."
    apktool d -q --force-manifest "$f"
    echo -e "\n\n#### File: $f ####\n" >> manifester_output.txt
    cat "${f::-4}/AndroidManifest.xml" >> manifester_output.txt
    rm -rf "${f::-4}"
done
