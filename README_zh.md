# milk jpn vocalsharp

[English](README.md) | **中文**

[Github](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/blob/main/README_zh.md) | 
[Gitlab](https://gitlab.com/oxygen-dioxide/milk-jpn-vocalsharp/-/blob/main/README_zh.md) | 
[Bitbucket](https://bitbucket.org/oxygendioxide/milk-jpn-vocalsharp/src/main/README_zh.md) |

Milk是Xepheris制作的UTAU虚拟歌手。本仓库是Milk日文VCV音源的镜像站。音频和oto均没有修改。

根据Milk的[用户协议](https://github.com/oxygen-dioxide/milk-jpn/blob/main/license.md)，转载，修改oto.ini和音频文件，以及移植到其他合成引擎是允许的，但须正确地注明音源名称“Milk”和原作者“Xepheris”，并明确地声明你所作的改动。

## 下载
[从Github下载](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/releases)

## 技术规格
- 六音阶（A3、F3、D4、G4、PowerC5、假声(Falsetto)）
- 日文VCV

## 贡献者注意
目前请不要创建Pull Request，尤其是对于vsdxmf文件。因为vsdxmf文件在我每次构建音源时使用python脚本由oto.ini重新生成。如果你想修复bug或实现新功能，请[提出issue](https://github.com/oxygen-dioxide/milk-jpn-vocalsharp/issues/new)

## 对源文件的修改
- 每个音频文件开头和结尾加0.2s空白音频，因为vocalsharp不允许标记线离头尾太近。
- 将oto.ini使用python脚本转为main.vsdxmf

## 相关链接
- CV：Xepheris
- Oto：DiPi, Kimchi_tan, Kale
- Quality Checking by DiPi and Kimchi_tan
- [Milk官网](https://xepheris.wixsite.com/milk)
- [Xepheris的b站空间](https://space.bilibili.com/618761702/dynamic)