```
   )' .                                                                                      
  /    \      (\-./                                                                         
 /     |    _/ o. \                ___   ___   ___         ___   ___   ___   ___   ___       
|      | .-'      y)-             |   |   | |   | | |     |   | |       |   |     |   |     
|      |/       _/ \ __,_____     |-+-    + |   +-  |     |-+-|  -+-    +   |-+-  |-+-      
\     /j   _'.\(@)  / __.==--'    |       | |   | | |     |   |     |   |   |     |  \      
 \   ( |    `.''  )/#(-'          |      ---   ---   ---         ---         ---             
  \  _`-     |   / `-'                                                                      
    '  `-._  <_ (                                                                           
          `-.      
```
# PDBlaster
PDBlaster is designed to extract PDB file paths from large sample sets of executable files. The intention of the tool is to simplify the process of extraction, basic repeat entry analysis, and username discovery of/from the PDB file paths of large sample sets of maliscious executables. This allows for quick and easy creation of PDB path detail datasets. More detail can be found in the Security Risk Advisors [PDBlaster Blog Post](https://securityriskadvisors.com/blog/pdblaster-making-bread-from-attacker-breadcrumbs/).

# Acknowledgements
* This tool was inspired by this [Fireye Blog Post](https://www.fireeye.com/blog/threat-research/2019/08/definitive-dossier-of-devilish-debug-details-part-one-pdb-paths-malware.html), written by Steve Miller
* This tool uses [pefile](https://github.com/erocarrera/pefile) to pull the PDB file path from samples


# Usage
```
usage: pdblaster.py [-h] -s SAMPLES -o OUTPUT [-p PAUSE] [-u] [-r] [--summary]
                    [--sherlock]

optional arguments:

  -h, --help            show this help message and exit

  -s SAMPLES, --samples SAMPLES
                        Specify the location of your samples

  -o OUTPUT, --output OUTPUT
                        Specify the location for your csv output

  -p PAUSE, --pause PAUSE
                        Specify a sleep interval for every 500 files (default
                        is 0)

  -u, --users           Print discovered usernames

  -r, --repeats         Check for PDB and username repeats across samples

  --summary             Print a sumamry of samples with PDB paths

  --sherlock            Run discovered usernames through sherlock username
                        checker
```



# Examples

This shows two sample outputs when running pdblaster against [theZoo](https://github.com/ytisf/theZoo) with different commandline arguments.

To run these tests on your own:

1. Clone (or download and unzip) theZoo ```git clone https://github.com/ytisf/theZoo```
2. Change into the Zoo malware binaries directory ```cd /PATH/TO/theZoo-master/malwares/Binaries/```
3. Unzip the files containing the binary samples ```find . -name "*.zip" | while read filename; do unzip -o -P infected -d "`dirname "$filename"`" "$filename"; done;```
4. Copy the files into a single directory (NOTE: This will copy ALL of the files) ```find -type f -print0|xargs -0r mv -it /LOCATION/OF/EXPORT/```

### Summary, PDB/Username Repeat Analysis, and Username Display:

Input:

```test@ubuntu:~/home/PDBlaster$ python3 pdblaster.py -s /home/test/theZoo/ -o /home/outputs/ --summary --repeats --users```

Output (NaN means no value is present):
```

   )' .                                                                                      
  /    \      (\-./                                                                         
 /     |    _/ o. \                ___   ___   ___         ___   ___   ___   ___   ___       
|      | .-'      y)-             |   |   | |   | | |     |   | |       |   |     |   |     
|      |/       _/ \ __,_____     |-+-    + |   +-  |     |-+-|  -+-    +   |-+-  |-+-      
\     /j   _'.\(@)  / __.==--'    |       | |   | | |     |   |     |   |   |     |  \      
 \   ( |    `.''  )/#(-'          |      ---   ---   ---         ---         ---             
  \  _`-     |   / `-'                                                                      
    '  `-._  <_ (                                                                           
          `-.      


Pulling PDB path from 3143 samples!
Output saved to: home/outputs/output20191121130612.csv
Processing File: 3143 of 3143

--------------------FILENAMES WITH PDB PATHS--------------------
                                                 file                                            pdbname        username
0                                           njRAT.exe  C:\\Users\\algha_000\\AppData\\Local\\Temporar...       algha_000
1   f152ed03e4383592ce7dd548c34f73da53fc457ce8f26d...  c:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
2   Torpig miniloader_0F82964CF39056402EE2DE919363...                                 packaigee.pdb\x00'             NaN
3   Torpig miniloader_83419EEA712182C1054615E4EC7B...                                nantietive.pdb\x00'             NaN
4   bd039bb73f297062ab65f695dd6defafd146f6f233c451...  d:\\vb_c++\\Explosive\\ExplosiveTr\\4-2013\\to...             NaN
5   Torpig miniloader_87851480DEB151D3A0AA9A425FD7...                               intterfaece.pdb\x00'             NaN
6                    F1E546FE9D51DC96EB766EC61269EDFB  d:\\Projects\\WinRAR\\SFX\\build\\sfxrar32\\Re...             NaN
7   Potao_DebugVersion_5199FCD031987834ED3121FB316...     E:\\svn\\sapotao\\BIN\\node69-dropper.pdb\x00'             NaN
8   ea335556fecaf983f6f26b9788b286fbf5bd85ff403bb4...  d:\\vb_c++\\c++\\Profiler-P\\SmartSender\\wnhe...             NaN
9   1ee894c0b91f3b2f836288c22ebeab44798f222f17c255...  C:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
10  Torpig miniloader_C3366B6006ACC1F8DF875EAA1147...                                  packaghe.pdb\x00'             NaN
11  97ab07c8020aead6ce0d9196e03d3917045e65e8c65e52...  d:\\vb_c++\\Explosive\\ExplosiveTr\\With Encry...             NaN
12  fc75410aa8f76154f5ae8fe035b9a13c76f6e132077346...  C:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
13  4bfe2216ee63657312af1b2507c8f2bf362fdf1d63c88f...  d:\\!work\\etc\\hideinstaller_kis2013\\Bin\\De...             NaN
14  Torpig miniloader_4A3543E6771BC78D32AE46820AED...                                prieivatie.pdb\x00'             NaN
15                                        ___2A6E.tmp                              ParentDelete.pdb\x00'             NaN
16  Torpig miniloader_2DACC4556FAD30027A384875C8D9...                                 catlashis.pdb\x00'             NaN
17  Potao_DebugVersion_7263A328F0D47C76B4E103546B6...     E:\\svn\\sapotao\\BIN\\node69-dropper.pdb\x00'             NaN
18                               Win32.GravityRAT.exe  C:\\Users\\The Invincible\\Desktop\\gx\\gx-cur...  The Invincible
19      jpeg1x32.dll_C2BA81C0DE01038A54703DE26B18E9EE                                  jpeg1x32.pdb\x00'             NaN
20                               Win32.WannaPeace.exe  E:\\Users\\SCORPION\\Downloads\\privatelocker_...        SCORPION
21                                InstallBC201401.exe  D:\\Dev\\Tin9\\InstallDir\\vc80-win32u\\Loader...             NaN
22  zerolocker_d4c62215df74753371db33a19a69fccdc4b...  C:\\Users\\George\\Desktop\\Projects\\ZeroLock...          George
23                                         NAudio.dll  C:\\Users\\Mark\\Code\\CodePlex\\naudio\\NAudi...            Mark
24  Potao_FakeTrueCryptextracted exe_C1F715FF0AFC7...  C:\\dev\\msvc\\TrueCrypt\\Mount\\Debug\\Mount....             NaN
25  d43c10a2c983049d4a32487ab1e8fe7727646052228554...  C:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
26  26b4699a7b9eeb16e76305d843d4ab05e94d43f3201436...               GoogleCrashHandler_unsigned.pdb\x00'             NaN
27                                     Mono.Cecil.dll  C:\\Users\\njq8\\Desktop\\jbevain-cecil-0.9.5-...            njq8
28  0d8c2bcb575378f6a88d17b5f6ce70e794a264cdc8556c...  b:\\myrtus\\src\\objfre_w2k_x86\\i386\\guava.p...             NaN
29  Torpig miniloader_809910F29AA63913EFA76D00FA8C...                                naiotoivhe.pdb\x00'             NaN
30              GROK_24A6EC8EBF9C0867ED1C097F4A653B8D  c:\\users\\rmgree5\\co\\standalonegrok_2.1.1.1...         rmgree5
31  48b1024f599c3184a49c0d66c5600385265b9868d09361...  C:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
32  37f4e9d0153221d9a236f299151c9f6911a6f78fff54c9...  d:\\vb_c++\\Explosive\\ExplosiveTr\\ExplosiveT...             NaN
33                                 CretClient.exe.vir  e:\\Code\\ok_code\\CretClient\\release\\CretCl...             NaN
34  Torpig miniloader_011C1CA6030EE091CE7C20CD3AAE...                                piachakage.pdb\x00'             NaN
35                                       lwxtbjqm.cpp                                lawAsystem.pdb\x00'             NaN
36                                            131.exe  \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x...             NaN
37  0008065861f5b09195e51add72dacd3c4bbce644471132...  d:\\vb_c++\\c++\\Profiler-P\\SmartSender\\wnhe...             NaN
38                  Install_LiveManagerPlayer.exe.vir  d:\\Projects\\WinRAR\\SFX\\build\\sfxrar32\\Re...             NaN
39  Potao_DebugVersion_BDC9255DF5385F534FEA83B497C...     E:\\svn\\sapotao\\BIN\\node69-dropper.pdb\x00'             NaN
40                                  Win32.KeyPass.bin  G:\\Doc\\My work (C++)\\_New 2018\\Encryption\...             NaN
41  2094d105ec70aa98866a83b38a22614cff906b2cf0a089...  c:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc
42                                 Fake Intel (1).exe                         c:\\To\\CALs\\The.pdb\x00'             NaN
43  c999bf5da5ea3960408d3cba154f965d3436b497ac9d49...  C:\\Users\\tmc\\Documents\\Visual Studio 2015\...             tmc


--------------------PDB PATH REPEATS--------------------
                                           pdbname                                               file username
 C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  1ee894c0b91f3b2f836288c22ebeab44798f222f17c255...      tmc
                                                    fc75410aa8f76154f5ae8fe035b9a13c76f6e132077346...      tmc
                                                    d43c10a2c983049d4a32487ab1e8fe7727646052228554...      tmc
                                                    c999bf5da5ea3960408d3cba154f965d3436b497ac9d49...      tmc
    E:\\svn\\sapotao\\BIN\\node69-dropper.pdb\x00'  Potao_DebugVersion_5199FCD031987834ED3121FB316...      NaN
                                                    Potao_DebugVersion_7263A328F0D47C76B4E103546B6...      NaN
                                                    Potao_DebugVersion_BDC9255DF5385F534FEA83B497C...      NaN
 c:\\Users\\tmc\\Documents\\Visual Studio 2015\...  f152ed03e4383592ce7dd548c34f73da53fc457ce8f26d...      tmc
                                                    2094d105ec70aa98866a83b38a22614cff906b2cf0a089...      tmc
 d:\\Projects\\WinRAR\\SFX\\build\\sfxrar32\\Re...                   F1E546FE9D51DC96EB766EC61269EDFB      NaN
                                                                    Install_LiveManagerPlayer.exe.vir      NaN
 d:\\vb_c++\\c++\\Profiler-P\\SmartSender\\wnhe...  ea335556fecaf983f6f26b9788b286fbf5bd85ff403bb4...      NaN
                                                    0008065861f5b09195e51add72dacd3c4bbce644471132...      NaN


--------------------USERNAME REPEATS--------------------
username                                            pdbname                                               file
     tmc  c:\\Users\\tmc\\Documents\\Visual Studio 2015\...  f152ed03e4383592ce7dd548c34f73da53fc457ce8f26d...
          C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  1ee894c0b91f3b2f836288c22ebeab44798f222f17c255...
          C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  fc75410aa8f76154f5ae8fe035b9a13c76f6e132077346...
          C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  d43c10a2c983049d4a32487ab1e8fe7727646052228554...
          C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  48b1024f599c3184a49c0d66c5600385265b9868d09361...
          c:\\Users\\tmc\\Documents\\Visual Studio 2015\...  2094d105ec70aa98866a83b38a22614cff906b2cf0a089...
          C:\\Users\\tmc\\Documents\\Visual Studio 2015\...  c999bf5da5ea3960408d3cba154f965d3436b497ac9d49...

--------------------USERNAMES FOUND--------------------
 - algha_000
 - tmc
 - The Invincible
 - SCORPION
 - George
 - Mark
 - njq8
 - rmgree5


test@ubuntu:~/home/PDBlaster$ 

```
### Running Found Names through sherlock:

With sherlock installed in the same directory as pdblaster.py, and the ```--sherlock``` flag used in the commandline, usernames can be filtered and run through sherlock. (Shown in the output example below.)

Input:

```test@ubuntu:~/home/PDBlaster$ python3 pdblaster.py -s /home/samples/theZoo/ -o ./outputs/ --users --sherlock```

Output:
```

   )' .                                                                                      
  /    \      (\-./                                                                         
 /     |    _/ o. \                ___   ___   ___         ___   ___   ___   ___   ___       
|      | .-'      y)-             |   |   | |   | | |     |   | |       |   |     |   |     
|      |/       _/ \ __,_____     |-+-    + |   +-  |     |-+-|  -+-    +   |-+-  |-+-      
\     /j   _'.\(@)  / __.==--'    |       | |   | | |     |   |     |   |   |     |  \      
 \   ( |    `.''  )/#(-'          |      ---   ---   ---         ---         ---             
  \  _`-     |   / `-'                                                                      
    '  `-._  <_ (                                                                           
          `-.      


Pulling PDB path from 3143 samples!
Output saved to: home/outputs/output20191121130612.csv
Processing File: 3143 of 3143
--------------------USERNAMES FOUND--------------------
 - algha_000
 - tmc
 - The Invincible
 - SCORPION
 - George
 - Mark
 - njq8
 - rmgree5

Enter the usernames you would like to remove from search: ('done' to end)
George
George removed

Current Name List: 
 - algha_000
 - tmc
 - The Invincible
 - SCORPION
 - Mark
 - njq8
 - rmgree5
Enter the usernames you would like to remove from search: ('done' to end)
Mark
[-] Mark removed

Current Name List: 
 - algha_000
 - tmc
 - The Invincible
 - SCORPION
 - njq8
 - rmgree5
Enter the usernames you would like to remove from search: ('done' to end)
SCORPION
[-] SCORPION removed

Current Name List: 
 - algha_000
 - tmc
 - The Invincible
 - njq8
 - rmgree5
Enter the usernames you would like to remove from search: ('done' to end)
tmc
[-] tmc removed

Current Name List: 
 - algha_000
 - The Invincible
 - njq8
 - rmgree5
Enter the usernames you would like to remove from search: ('done' to end)
done

[*] Checking username algha_000 on:
[-] Facebook: Illegal Username Format For This Site!
[-] GitHub: Illegal Username Format For This Site!
[...sherlock continues to search through each username, in the order listed above...]
```

# Setup
* Install Requirements ``` pip3 install -r requirements.txt ```
* OPTIONAL: for use of ```--sherlock``` to automatically feed found usernames into a sherlock scan, you must first clone sherlock into the repository using: ``` git clone https://github.com/sherlock-project/sherlock ``` and follow steps on the [sherlock github](https://github.com/sherlock-project/sherlock) for proper setup instructions
* NOTE: Usernames are simply the value after ```...\Users\[username]\...``` in a PDB path
