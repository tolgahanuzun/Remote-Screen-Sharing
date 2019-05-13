# Remote Screen Sharing

It is a project that streams the screen image of the computer onto the web. At first I was planning to serve the local network. But then I decided to share it on the outer network. 

## Motivation
I have a desktop computer at home. I was giving it some tasks. I just need their status in these tasks. I started this project for this.

## How to install

Very simple.

```
python install -r requirements.txt
```

## I'm Use

I got help from the `pyscreenshot` library to capture the screen. With Flask (!ILOVEFLASK) I made it a web application. I opened the external network with Ngrok.

## Example Screen

- Server:

<img src="https://farm5.staticflickr.com/4875/33148801038_20f703b541_b.jpg"  alt="drawing" style="width:600px;"/>

- Client


<img src="https://farm8.staticflickr.com/7850/47023968531_01762ac848_b.jpg"  alt="drawing" style="width:600px;"/>

## TODO:

- Clean code!
- I need to build in .exe format for Windows.
- I need bash command for Unix.
- I need to find a better solution than ngrok.