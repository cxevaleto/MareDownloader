# MareDownloader
A GTK4 application that downloads images of mares based on https://derpibooru.org
![screenshot](screenshot.png)

# Instalation

## Configure

```bash
meson setup build
```
or to install for local user
```bash
meson setup --prefix=~/.local build
```

## then compile and install

```bash
cd build
ninja
meson install
```
