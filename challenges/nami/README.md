```bash
su nami
password: FLAG_32d066dfa71ff63c331604f937120fb7
cd ONEPIECE
```
```bash
find . -type f
```
<pre>
./East_Blue/Baratie/Casa_de_Zeff/flag.txt
./East_Blue/Loguetown/Casa_de_Bell-m??re/flag.txt
./Water_7/Blue_Station/Casa_de_Paulie/flag.txt
./Water_7/Carpenters_Cafe/Casa_de_Paulie/flag.txt
./Water_7/GalleyLa_Headquarters/Casa_de_Paulie/poneglyph.zip
./Alabasta/Spiders_Cafe/Casa_de_Mr. 0/flag.txt
./Alabasta/Katorea/Casa_de_Toto/flag.txt
./Zou/Right_Hind_Leg/Casa_de_Nekomamushi/flag.txt
./Zou/Left_Fore_Leg/Casa_de_Nekomamushi/flag.txt
./Whole_Cake_Island/Cacao_Island/Casa_de_Big_Mom/flag.txt
./Whole_Cake_Island/Caramel_Mountain/Casa_de_Big_Mom/flag.txt
</pre>

```bash
cat ./Water_7/GalleyLa_Headquarters/Casa_de_Paulie/poneglyph.zip
cat ./Alabasta/Spiders_Cafe/Casa_de_Mr. 0/flag.txt
```
<pre>
3fc06ae08a18afb1d58f6b8d027163526530ea6e71d607fb9b49a4c7e13484346268e70068
</pre>

## From Host
### MODIFY ./utils/nami_chacha.py
```python
print(chacha20_decrypt(bytes.fromhex("3fc06ae08a18afb1d58f6b8d027163526530ea6e71d607fb9b49a4c7e13484346268e70068"), "21430"))
```
```bash
python utils/nami_chacha.py
```
<pre>
FLAG_f492daceb72658abde3a6b6f639502cf
</pre>

# Extract zip:
```
FLAG_32d066dfa71ff63c331604f937120fb7
```