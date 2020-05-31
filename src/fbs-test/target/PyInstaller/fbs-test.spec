# -*- mode: python -*-

block_cipher = None


a = Analysis(['F:\\Python\\PyQt5\\Dijkstra.GUI.PyQt5\\src\\fbs-test\\src\\main\\python\\main.py'],
             pathex=['F:\\Python\\PyQt5\\Dijkstra.GUI.PyQt5\\src\\fbs-test\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['f:\\python\\pyqt5\\dijkstra.gui.pyqt5\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['F:\\Python\\PyQt5\\Dijkstra.GUI.PyQt5\\src\\fbs-test\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='fbs-test',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='F:\\Python\\PyQt5\\Dijkstra.GUI.PyQt5\\src\\fbs-test\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='fbs-test')
