# milk jpn vocalsharp

**English** | [中文](README_zh.md)

[Github](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp) | 
[Gitlab](https://gitlab.com/oxygen-dioxide/milk-jpn-vocalsharp) | 
[Bitbucket](https://bitbucket.org/oxygendioxide/milk-jpn-vocalsharp) | 
[Coding](https://oxygen-dioxide.coding.net/public/1/milk-jpn-vocalsharp/git/files)

Milk is a UTAU virtual singer developed by Xepheris. This repo ports Milk's Japanese VCV UTAU voicebank to Vocalsharp.

According to Milk's [Voicebank Terms of Use](license.md), redistribution of voicebanks, editing of oto.ini and audio samples, and porting to other synthesis softwares are allowed without permission, so long as the voicebank name and author are credited, and any changes you have made are clearly stated.

If you like this voicebank, please give him a star.

If you find a bug, please [create an issue](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/issues/new) to report it.

## Download
[Download from Github](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/releases)

## Tech Specs
- 6 pitches（A3、F3、D4、G4、PowerC5、Falsetto）
- Japanese VCV
- Breath endings: R (in development)
- Glottal Stops: ! (in development)
- Vocal Fry: ' (in development)

## Contributor notice
Currently please don't create pull requests, especially those about .vsdxmf files. Because vsdxmf files are generated from oto.ini with my python script each time I build this voicebank. If you want to fix a bug or implement a function, Please [create an issue](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/issues/new) to let me know.

## Changes to the source files
- 0.2s of blank audio are added to the begin and end of each audio file to meet vocalsharp's requirement.
- oto.ini files are converted to main.vsdxmf with my python script

## Links
- CV：Xepheris
- Oto：DiPi, Kimchi_tan, Kale
- Quality Checking by DiPi and Kimchi_tan
- [VocalSharp official site](https://vocalsharp.com)
- [Milk Official Website](https://xepheris.wixsite.com/milk)
- [Xepheris' bilibili channel](https://space.bilibili.com/618761702/dynamic)