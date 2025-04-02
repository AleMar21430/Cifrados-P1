```bash
su zoro
password: FLAG_08d3164f15a022f7fb28617afb39a63a
cd ONEPIECE
```
```bash
find . -type f
```
<pre>
./East_Blue/Syrup_Village/Casa_de_Kaya/flag.txt
./Water_7/Franky_House/Casa_de_Luffy/flag.txt
./Alabasta/Alubarna/Casa_de_Crocodile/flag.txt
./Alabasta/Spiders_Cafe/Casa_de_Nico Robin/flag.txt
./Alabasta/Katorea/Casa_de_Pell/poneglyph.zip
./Zou/Left_Belly_Fortress/Casa_de_Nekomamushi/flag.txt
./Zou/Right_Fore_Leg/Casa_de_Nekomamushi/flag.txt
./Zou/Right_Hind_Leg/Casa_de_Inuarashi/flag.txt
./Zou/Left_Fore_Leg/Casa_de_Kawamatsu/flag.txt
./Zou/Left_Fore_Leg/Casa_de_Inuarashi/flag.txt
./Whole_Cake_Island/Caramel_Mountain/Casa_de_Big_Mom/flag.txt
./Whole_Cake_Island/Whole_Cake_Chateau/Casa_de_Katakuri/flag.txt
</pre>

```bash
cat ./Alabasta/Katorea/Casa_de_Pell/poneglyph.zip
cat ./Zou/Right_Fore_Leg/Casa_de_Nekomamushi/flag.txt
```
<pre>
90593df71c367d2e9b23d3712dd548a51d93cd43e00fa723f58810a6de5c5988102c8fcfc5
</pre>

## From Host
### MODIFY ./utils/zoro.py
```python
print(rc4_decrypt(bytes.fromhex("90593df71c367d2e9b23d3712dd548a51d93cd43e00fa723f58810a6de5c5988102c8fcfc5"), "21430"))
```
```bash
python utils/zoro.py
```
<pre>
FLAG_1c7479a49573ee16e645c293c6b15dff
</pre>

# Extract zip:
```
FLAG_08d3164f15a022f7fb28617afb39a63a
```