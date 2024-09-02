# Package manager

- Type of challenge: **Learning**
- Duration: **30 min**
- Team challenge: **solo**

## Learning objectives

At the end of this challenge you should be able to:

- Install packages
- Remove packages
- Search for packages
- **[Linux or WSL only]** update your Linux kernel (if you don't know what the kernel is, Google it!)

## Requirements

This drill assumes you know how to:

- Consult the manual within the terminal

## The mission

You need to install `neofetch` on your machine, and you’ve been told that most Unix operating systems have a tool for that, the **package manager**.

You’ve heard that the package manager for the **Ubuntu based distribution** is `apt-get`. Open your **terminal** and **read its manual** to understand it, then follow the instructions below.

On Windows, package managers are relatively unused and are of wildly different flavors. [`scoop`](https://scoop.sh/) was until now one of the few package managers adapted to Windows, but it is for PowerShell, and not `cmd`. Remember, in Windows, there are 2 default terminals, and unfortunately this tutorial centers on `cmd`. You are welcome to try it out on PowerShell, but you are on your own.

However, recently Microsoft introduced an official package manager [winget](https://www.howtogeek.com/674470/how-to-use-windows-10s-package-manager-winget/). You are welcome to try this one out too.

Don't spend too much time on this chapter on Windows, if it doesn't work, just move on to the next. As we mentioned, command line installers are not widespread yet in Windows.

> **Note**
>
> If you use another distribution, find out which package manager it uses and research it.

- Update all the packages on your system.
- Search if your distribution has `neofetch`.
- Install `neofetch`.
- Launch `neofetch`.
- Remove `neofetch`.

There are plenty of package managers across a lot of operating systems, Mac uses `brew`, Arch Linux uses `pacman`, even languages such as NodeJS (`npm`), Python (`pip`) and PHP (`composer`) use them to manage dependencies.

- [Apt-get tutorial](https://itsfoss.com/apt-get-linux-guide/)

## Congrats

In the world of Unix/Linux you rarely download a program from its website. Rather each distribution has a **repository** of software to install, which you can consult with your **package manager**.

![GIF](https://media.giphy.com/media/n1koqKtJ8xffa/giphy.gif)
