# RTFM

- Type of challenge: **Learning**
- Duration: **60 min**
- Team Challenge: **solo**

## Learning objectives

At the end of this challenge you should be able to:

- Read the manual of commands.
- Find out what a command does.
- Understand the `--help` flag.

## The mission

The terminal can be intimidating with all these commands and text flying around. It’s an all new world, one of _textual interface_ with rules very different from a more familiar _graphical interface_. Hopefully, to guide you in this new environment there are tools like `man` (![Windows icon](./assets/win_icon.png) `help`).

- Open a **terminal**
- Type `man man` (![Windows icon](./assets/win_icon.png) `help help`)
- Hit the `h` key (Linux only)
- Leave the manual

You might have guessed it, `man` opens the manual for the wanted page and although it can be technical it remains one of the best place to learn.

**[Linux or WSL only]** Still, if you simply want a description let’s try to use `whatis`.

- Type `whatis man`
- Type `whatis whatis`

Another great, but more concise, way to understand how to use a command is the `--help`
[flag](http://www.tldp.org/LDP/abs/html/standard-options.html).

- Type `whatis --help`

You won’t always find a manual page, but you will usually be able to get information via the help flag.

Practice by learning about `ls` (![Windows icon](./assets/win_icon.png) `dir`), `cp` (![Windows icon](./assets/win_icon.png) `copy`) and `pwd` (![Windows icon](./assets/win_icon.png) `cd`).

### Optional [Linux or WSL only]

An alternative to the `man` command is `info`. Do some research to learn more about their differences.

Lastly, a great tool that you can install using your package manager is `tldr`, which stands for **Too Long, Didn’t Read**. It is a community driven list which gives the most common usages for a given command.

- Try it out with `tldr ls`

## Congrats

Understanding software is the most important step in using it. Because remember, in the manual lies the **wisdom** and **madness** of the creator.

![GIF](https://media.giphy.com/media/8dYmJ6Buo3lYY/giphy.gif)
