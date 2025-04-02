```bash
su usopp
password: FLAG_f492daceb72658abde3a6b6f639502cf
cd ONEPIECE
```
```bash
find . -type f
```
<pre>
./East_Blue/Romance_Dawn/Casa_de_Makino/flag.txt
./Water_7/Blue_Station/Casa_de_Lucci/flag.txt
./Water_7/Franky_House/Casa_de_Luffy/flag.txt
./Water_7/Shift_Station/Casa_de_Iceburg/flag.txt
./Alabasta/Rainbase/Casa_de_Crocodile/flag.txt
./Alabasta/Katorea/Casa_de_Pell/flag.txt
./Zou/Left_Belly_Fortress/Casa_de_Inuarashi/flag.txt
./Zou/Right_Fore_Leg/Casa_de_Nekomamushi/flag.txt
./Zou/Right_Hind_Leg/Casa_de_Kawamatsu/flag.txt
./Zou/Right_Belly_Fortress/Casa_de_Inuarashi/poneglyph.zip
./Whole_Cake_Island/Cacao_Island/Casa_de_Big_Mom/flag.txt
./Whole_Cake_Island/Caramel_Mountain/Casa_de_Pudding/flag.txt
</pre>

```bash
cat ./Zou/Right_Belly_Fortress/Casa_de_Inuarashi/poneglyph.zip
cat ./Zou/Right_Fore_Leg/Casa_de_Nekomamushi/flag.txt
```
<pre>
a77742694e1900d1493e396cd796da7d483b0c349a4c12df151d23ec19a9c184ba4f008a3e
</pre>

## From Host
### MODIFY ./utils/usopp.py
```python
decrypt("a77742694e1900d1493e396cd796da7d483b0c349a4c12df151d23ec19a9c184ba4f008a3e")
```
```bash
python utils/usopp.py
```
<pre>
Semilla encontrada: 1234
Texto descifrado: FLAG_32d066dfa71ff63c331604f937120fb7
</pre>

# Extract zip:
```
FLAG_1c7479a49573ee16e645c293c6b15dff
```