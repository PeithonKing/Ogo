
# Ogo

This is a personal virtual assistant...

I will write what it does in the next commit I do to this repo!



# Important

**After installing all the other requirements by ```pip install -r requirements.txt```** command, you need to manually install the PyAudio library.

Suppose you are using python version 3.x\
(ofcourse it doesn't support python 2!)

(in case you don't know which version you are in, go to any terminal and run:

```powershell
python --version
```
or

```powershell
python3 --version
```


)

then....


**if x<6:**\
&emsp;&emsp;run

```powershell
pip install PyAudio
```

**else:** go to [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
and download the PyAudio according to your system configuration. Keep the downloaded file in the same folder as the *requirements.txt* file.

For example, I had **Python 3.9.1**. So I downloaded the file named **"PyAudio-0.2.11-cp39-cp39-win_amd64.whl"** 

then navigate to the directory where the file is, and install the library using ```pip install <filename>``` command.\
(filename = "PyAudio-0.2.11-cp39-cp39-win_amd64.whl" in my case).