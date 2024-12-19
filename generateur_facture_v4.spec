# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['generateur_facture_v4.py'],
    pathex=[],
    binaries=[],
    datas=[('tableau/tableau_fermage.xlsx', 'tableau'), ('assets/img/Fermage.png', 'assets/img'), ('assets/fonts', 'assets/fonts'), ('assets/img/facturation_fermage.ico', 'assets/img')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='generateur_facture_v4',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\img\\facturation_fermage.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='generateur_facture_v4',
)
