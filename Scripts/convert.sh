#!/bin/bash

log=$(pwd)/gitPush.sh.log

echo "[$(date)] start" >> $log

echo "[Messeage by convert.sh]cd git top level dir(" `git rev-parse --show-toplevel` ")"
cd  `git rev-parse --show-toplevel`

for raw in $(git log origin/develop..develop --stat | grep ".blend") ; do
	if [ ${raw##*.} = "blend" ]; then
		echo "[Messeage by convert.sh] blend file is ${raw}"
		echo "[Messeage by convert.sh] Start Render.py"
		blender --background ${raw} --python Scripts/Render.py
		echo "[Messeage by convert.sh] Start ExportFBX.py"
		blender --background ${raw} --python Scripts/ExportFBX.py
	fi	
done
echo '[Messeage by convert.sh] git commit -m "Auto Generate FBX/render image"'
git add *.fbx
git add *.png
git commit -am "Auto convert FBX and render image"