# Installing and configuring Git

## Installation

Follow the instructions [here](https://git-scm.com/downloads) for downloading and installing Git on your computer.

## Configuration

### Your profile on GitHub

Create and complete your [GitHub profile](https://github.com/settings/profile).
Your name, surname and a recent picture of yourself are required.

### Use GitHub in the terminal

To login into GitHub from the terminal you need a **SSH-key**. This key will connect your computer to your Github account. It will prevent you to enter your username and password each time you will interact with Github (and believe us, you will do it a lot)

In the next steps we will see how to generate a SSH-key and link it to your GitHub account.

1. Open your terminal.
2. Copy the following command into your terminal by changing "your_email@example.com" with the email address linked to your GitHub account and press `Enter`.

   ```shell
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

   This will create an SSH key that is linked to your email

3. Generate a private/public RSA key pair. When you are asked to "Enter a file in which to save the key", press `Enter`. This will accept the standard location. Keep this location somewhere because you will need it later.
4. Enter passphrase (empty for no passphrase): [Leave blank and press `Enter`]. We suggest that you don't add a password here to avoid multiple password typings per day.
5. Enter same passphrase again: [Leave blank and press `Enter`].
6. Follow [this tutorial](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to link your ssh key to your github account depending on your operating system.