# cf http://bluebirdofoz.hatenablog.com/entry/2018/04/23/000656
# cf http://bluebirdofoz.hatenablog.com/entry/2019/07/21/213610

import bpy,sys

def fbx_export_geometry(arg_filepath='./export.fbx'):
  # FBXエクスポート
  # bpy.ops.export_scene.fbx()
  # エクスポート設定(デフォルト値)
  bpy.ops.export_scene.fbx(
    filepath=arg_filepath,
    #version='BIN7400',
    #use_selection=False,
    #global_scale=1.0,
    #apply_unit_scale=True,
    #apply_scale_options='FBX_SCALE_NONE',
    #bake_space_transform=False,
    object_types={'ARMATURE', 'MESH'},
    #use_mesh_modifiers=True,
    #use_mesh_modifiers_render=True,
    #mesh_smooth_type='OFF',
    #use_mesh_edges=False,
    #use_tspace=False,
    #use_custom_props=False,
    #add_leaf_bones=True,
    #primary_bone_axis='Y',
    #secondary_bone_axis='X',
    #use_armature_deform_only=False,
    #armature_nodetype='NULL',
    bake_anim=False,
    #bake_anim_use_all_bones=True,
    #bake_anim_use_nla_strips=True,
    #bake_anim_use_all_actions=True,
    #bake_anim_force_startend_keying=True,
    #bake_anim_step=1.0,
    #bake_anim_simplify_factor=1.0,
    #path_mode='COPY',
    #embed_textures=True
    #batch_mode='OFF',
    #use_batch_own_dir=True,
    #use_metadata=True
  )
  # 出力対象の種別
  #  'EMPTY'：エンプティ
  #  'CAMERA'：カメラ
  #  'LAMP'：ランプ
  #  'ARMATURE'：アーマチュア
  #  'MESH'：メッシュ
  #  'OTHER'：その他
  # パスモードの種類
  #  'AUTO'：自動
  #  'ABSOLUTE'：絶対
  #  'RELATIVE'：相対的
  #  'MATCH'：マッチ
  #  'STRIP'：ストリップパス
  #  'COPY'：コピー
  return

# 関数の実行例
path = bpy.context.blend_data.filepath.rstrip(bpy.path.basename(bpy.context.blend_data.filepath)) + "../" +  bpy.path.basename(bpy.context.blend_data.filepath).split(".")[0] +".fbx"

fbx_export_geometry(path)