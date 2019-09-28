#!/bin/bash

log=$(pwd)/gitPush.sh.log

echo "[$(date)] start" >> $log

echo "cd git top level dir(" `git rev-parse --show-toplevel` ")"
cd  `git rev-parse --show-toplevel`

for raw in $(find . -name "*.blend" 2>/dev/null | grep ".blend") ; do
	blend=${raw#*/}
    echo "blend file is ${blend}"
    echo "Start Render.py"
    #blender --background ${blend} --python Scripts/Render.py
    echo "Start ExportFBX.py"
    blender --background ${blend} --python Scripts/ExportFBX.py
	#echo "cp ${raw} -t ${fbx%/*}"
	#if [[ ! -d "3DAssets-OnlyFBX/${fbx%/*}" ]] ; then
	#	echo "mkdir 3DAssets-OnlyFBX/${fbx%/*}"
	#	mkdir 3DAssets-OnlyFBX/${fbx%/*} | tee -a $log
	#fi
	#cp ${raw} -t 3DAssets-OnlyFBX/${fbx%/*} | tee -a $log
	
done