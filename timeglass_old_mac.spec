# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['timeglass.py'],
             pathex=['/Users/Gekko/Tinkering/Python/timeglass'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk','tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl','tcl')],
             datas=[('Icons/', 'Icons')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='timeglass',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='Icons/timeglass.png')

app = BUNDLE(exe,
             name='timeglass.app',
             icon='Icons/timeglass.icns',
             bundle_identifier=None,
             info_plist={
        'LSUIElement': 'True'
})