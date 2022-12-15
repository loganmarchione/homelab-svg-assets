# homelab-svg-assets

![](https://img.shields.io/github/directory-file-count/loganmarchione/homelab-svg-assets/assets?extension=svg&label=Icons&type=file)
![](https://img.shields.io/github/repo-size/loganmarchione/homelab-svg-assets)

I frequently need full-color SVGs logos/icons of open-source software or brands, in a normalized size. Other projects exist (like [Simple Icons](https://simpleicons.org/) or [Bootstrap Icons](https://icons.getbootstrap.com/)), but I've found they don't fit my needs.

This repo will serve as a source of icons used in my personal projects.

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Usage](#usage)
  - [General usage](#general-usage)
  - [PHP usage](#php-usage)
- [The Icons](#the-icons)
- [ToDo](#todo)
- [Contribute](#contribute)

## Usage

### General usage

Icons as SVGs are available in the [assets](https://github.com/loganmarchione/homelab-svg-assets/tree/main/assets) directory.

### PHP usage

Icons are available in PHP as a package on [Packagist](https://packagist.org/packages/loganmarchione/homelab-svg-assets).  


Run `composer require loganmarchione/homelab-svg-assets:0.0.1`, or add the package to your `composer.json` file (below)

```
{
    "require": {
        "loganmarchione/homelab-svg-assets": "0.0.1"
    }
}
```

### Hugo usage

There is a [go.mod](https://github.com/loganmarchione/homelab-svg-assets/blob/main/go.mod) file that can be used as a [Hugo module](https://gohugo.io/hugo-modules/). You need to be using at least Hugo [0.56.0](https://gohugo.io/news/0.56.0-relnotes/).

In your Hugo site directory, initialize your site as a module:

```
hugo mod init github.com/<your_user>/<your_project>
```

In your `config.yaml` (adjust for `.json` or `.toml` configurations), add the section below:

```
module:
  imports:
    - path: github.com/loganmarchione/homelab-svg-assets
      mounts:
        - source: assets
          target: assets/svg/svg-assets
```

Download the module:

```
hugo mod get -u
```

## The Icons

See [ICONS.md](ICONS.md) for a preview of all icons.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md)


## TODO

- AdGuard Home
- Adminer
- C#
- Fedora
- Microsoft SQl Server
- Pritunl
- Radarr
- Radicale
- Seafile
- Trakt
- VMWare
- XCP-ng
- Zigbee2MQTT

- Icons that I can't find
  - Baikal - Can't find a SVG of this
  - Bazarr - Can't find a SVG of this
  - Caddy - Can't find a SVG of this (has some PNG data inside it)
  - CloudBeaver - Can't find a SVG of this
  - Emby - Can't find a SVG of this
  - FreeBSD - Can't find a good SVG of this  (has some PNG data inside it)
  - Ghost - Can't find a SVG of this
  - Handbrake - The [SVG](https://github.com/HandBrake/HandBrake/blob/master/gtk/src/hb-icon.svg) is an encoded PNG
  - Jackett - Can't find a SVG of this
  - Postfix - Can't find a SVG of this
  - Tdarr - Can't find a SVG of this
  - Telegraf - Issue open [here](https://github.com/influxdata/telegraf/issues/12327)
  - TinyTinyRSS - Can't find a SVG of this
  - ZeroTier - Can't find a SVG of this
  - Zigbee - Can't find a SVG of this

- Icons that don't touch the edges (possibly need to be replaced?)
  - Audacity
  - CyberChef
  - CentOS
  - LXC
  - WikiJS
  - WhatsApp

