```bash
su luffy
password: onepiece
cd ONEPIECE
```
```bash
find . -type f
```
<pre>
./East_Blue/Syrup_Village/Casa_de_Kaya/flag.txt
./East_Blue/Arlong_Park/Casa_de_Arlong/flag.txt
./Water_7/Carpenters_Cafe/Casa_de_Lucci/flag.txt
./Water_7/GalleyLa_Headquarters/Casa_de_Paulie/flag.txt
./Alabasta/Nanohana/Casa_de_Kohza/flag.txt
./Alabasta/Katorea/Casa_de_Pell/flag.txt
./Zou/Left_Belly_Fortress/Casa_de_Inuarashi/flag.txt
./Zou/Left_Hind_Leg/Casa_de_Kawamatsu/flag.txt
./Zou/Left_Hind_Leg/Casa_de_Inuarashi/flag.txt
./Zou/Right_Hind_Leg/Casa_de_Nekomamushi/flag.txt
./Zou/Left_Fore_Leg/Casa_de_Kawamatsu/poneglyph.zip
./Whole_Cake_Island/Whole_Cake_Chateau/Casa_de_Big_Mom/flag.txt
</pre>
```bash
cat ./East_Blue/Syrup_Village/Casa_de_Kaya/flag.txt
```
<pre>Has encontrado un lugar lleno de secretos y misterios que apuntan a luffy</pre>

```bash
cat ./East_Blue/Arlong_Park/Casa_de_Arlong/flag.txt
```
<pre>747d75746f0209500001040552020553010601560557560108040003525650020d52060150</pre>

```bash
cat ./Water_7/Carpenters_Cafe/Casa_de_Lucci/flag.txt
```
<pre>Has encontrado un enemigo y ha tenido que huir</pre>

```bash
cat ./Water_7/GalleyLa_Headquarters/Casa_de_Paulie/flag.txt
```
<pre>Has encontrado un lugar abandonado</pre>

```bash
cat ./Alabasta/Nanohana/Casa_de_Kohza/flag.txt
```
<pre>Has encontrado un mapa que apunta a luffy</pre>

```bash
cat ./Alabasta/Katorea/Casa_de_Pell/flag.txt
```
<pre>Has encontrado un enemigo y ha tenido que huir</pre>

```bash
cat ./Zou/Left_Belly_Fortress/Casa_de_Inuarashi/flag.txt
```
<pre>Has encontrado un lugar abandonado</pre>

```bash
cat ./Zou/Left_Hind_Leg/Casa_de_Kawamatsu/flag.txt
```
<pre>Has encontrado un lugar peligroso</pre>

```bash
cat ./Zou/Left_Hind_Leg/Casa_de_Inuarashi/flag.txt
```
<pre>Has encontrado un lugar lleno de secretos y misterios que apuntan a luffy</pre>

```bash
cat ./Zou/Right_Hind_Leg/Casa_de_Nekomamushi/flag.txt
```
<pre>Has encontrado un tesoro que apunta a luffy</pre>

```bash
cat ./Whole_Cake_Island/Whole_Cake_Chateau/Casa_de_Big_Mom/flag.txt
```
<pre>Has encontrado un tesoro que apunta a luffy</pre>

## From Host
### MODIFY ./utils/luffy_xor.py
```python
print(xor_cipher(bytes.fromhex("747d75746f0209500001040552020553010601560557560108040003525650020d52060150"), "21430").decode())
```
```bash
python utils/luffy_xor.py
```
<pre>FLAG_08d3164f15a022f7fb28617afb39a63a</pre>

# Extract zip:
```
onepiece
```