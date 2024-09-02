# List of commands

This file contains a list of useful commands on Linux and their Windows (![Windows icon](./assets/win_icon.png)) or Mac OS equivalent (![Mac OS Icon](./assets/apple_icon.png)) if they exist and if they are different. The descriptions down below are far from complete, they are only here to give an idea of the use case.
Plus, there are many more commands and terminal tools out there for all sorts of needs, feel free to research.

_NOTE: Not all commands are necessarily installed on your system._

## Help

- `man` (![Windows icon](./assets/win_icon.png) `help`): display system documentation
- `whatis`: prints manual page description
- `info`: read _Info_ documents

## Navigation

- `cd`: change current directory
- `ls` (![Windows icon](./assets/win_icon.png) `dir`): list directory content
- `pwd` (![Windows icon](./assets/win_icon.png) `cd` with no arguments): print the current directory
- `pushd`: go to a folder while keeping old location on _"cache"_
- `popd`: go back to an old location on _"cache"_

## File operation

- `cat` (![Windows icon](./assets/win_icon.png) `type`): concatenate and print files
- `touch` (![Windows icon](./assets/win_icon.png) `type nul >`): create a file or update timestamps
- `cp` (![Windows icon](./assets/win_icon.png) `copy`): copy a file
- `mkdir` (![Windows icon](./assets/win_icon.png) `mkdir`): create a directory
- `mv` (![Windows icon](./assets/win_icon.png) `move`): move or rename a file
- `rm` (![Windows icon](./assets/win_icon.png) `del`): remove a file or directory
- `rmdir` (![Windows icon](./assets/win_icon.png) `rmdir`): remove an empty directory
- `ln` (![Windows icon](./assets/win_icon.png) `mklink`): link files
- `head`: output the first part of files
- `tail`: output the last part of files

## System

- `date` (![Windows icon](./assets/win_icon.png) `date /t`): print the date and time
- `cal`: display a calendar
- `lsblk` (![Apple icon](./assets/apple_icon.png) `diskutil list`): list connected drives

## Users

- `passwd` (![Windows icon](./assets/win_icon.png) `net user`): change user password
- `usermod` (![Windows icon](./assets/win_icon.png) `net user`): modify a user account
- `groupadd`(![Windows icon](./assets/win_icon.png) `net localgroup <GROUP_NAME> /add`): create a new group
- `whoami` (![Windows icon](./assets/win_icon.png) `whoami`): print current logged user

(![Apple icon](./assets/apple_icon.png) : on Mac OS all commands related to the users start with `sudo dscl`)

## Permissions

- `sudo` (![Windows icon](./assets/win_icon.png) `runas /user:<LOCAL_MACHINE_NAME>\administrator`): execute a command as the super-user
- `su`: change the current user
- `chmod`(![Windows icon](./assets/win_icon.png) `cacls`): change file permissions
- `chown` (![Windows icon](./assets/win_icon.png) `takeown`): change the owner of a file
- `chgrp`: change the group of a file

## Compression

- `tar`: archive files
- `gzip`: compress and expand files

## Remote

- `ssh`: remote login
- `rsync`: remote file copying tool

## Process management

- `ps` (![Windows icon](./assets/win_icon.png) `tasklist`): report process status
- `ps aux` (![Windows icon](./assets/win_icon.png) `tasklist`): list every running process in the system
- `kill` (![Windows icon](./assets/win_icon.png) `taskkill`): stop a process
- `top`: display a repetitively updating list of running processes
- `htop`: improved version of `top`
- `bg`: put a process in the background
- `fg`: bring a process in the foreground

## Package manager

- `apt-get` (![Apple icon](./assets/apple_icon.png) `brew`)
- `snap`
- `pip`: python packages

## Text editor

- ![Windows icon](./assets/win_icon.png) `notepad`
- `vim`
- `nvim`
- `nano`
- `gedit`
