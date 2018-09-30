from pathlib import Path
from signature_db import signatures
import json
import os


home = str(Path.home())
testHome = home + '/Documents/Python Test/'
failed = []
for subdir, dirs, files in os.walk(home):
    for file in files:
        filepath = subdir + os.sep + file
        fileExt = Path(filepath).suffix
        try:
            with open(filepath, 'rb') as f:
                    fileHex = f.read(32)
                    print('Filename: '+ file)
                    for sig in signatures:
                        if fileExt == sig['ext']:
                            print('File extension matches pattern in db: '+ fileExt)
                            expectedHex = str(json.dumps(sig['hex'])[1:-1])
                            print('Expected hex: ' + expectedHex)
                            sigLen = len(json.dumps(sig['hex']))
                            gotHex = str(fileHex.hex()[0:sigLen-2]).upper()
                            print('Got hex: ' + gotHex)
                            if (gotHex == expectedHex):
                                print('hexes match')
                            else :
                                print('File extension does not match database - Possibly edited')
                                failed.append(filepath)
        except:
            pass

print ('Failed files: ')
for s in failed:
    print(s)


