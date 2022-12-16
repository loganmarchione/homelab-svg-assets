# homelab-svg-assets

<a href="https://github.com/loganmarchione/homelab-svg-assets/tree/main/assets"><img src="https://img.shields.io/github/directory-file-count/loganmarchione/homelab-svg-assets/assets?extension=svg&label=Total%20Icons&type=file" alt="Total Icons"/></a>
<img src="https://img.shields.io/github/repo-size/loganmarchione/homelab-svg-assets??label=Repo%20Size" alt="Repo Size"/>


<a href="https://github.com/loganmarchione/homelab-svg-assets/tags"><img src="https://img.shields.io/github/v/tag/loganmarchione/homelab-svg-assets?label=Latest%20GitHub%20Version&sort=semver" alt="Latest GitHub Version"/></a>
<a href="https://packagist.org/packages/loganmarchione/homelab-svg-assets"><img src="https://img.shields.io/packagist/v/loganmarchione/homelab-svg-assets?label=Latest%20Packagist%20Version" alt="Latest Packagist Version"/></a>

I frequently need full-color SVG icons of homelab-related software, products, and brands  in a normalized size. Other projects exist (like [Simple Icons](https://simpleicons.org/) or [Bootstrap Icons](https://icons.getbootstrap.com/)), but I've found they don't fit my needs.

This repo will serve as a source of icons used in my personal projects.

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Usage](#usage)
  - [General usage](#general-usage)
  - [PHP usage](#php-usage)
  - [Hugo usage](#hugo-usage)
- [Icons](#icons)
- [Contribute](#contribute)
- [TODO](#todo)

# Usage

❗ All users should read read the [disclaimer](DISCLAIMER.md) before using this project. 

## General usage

Icons as SVGs are available in the [assets](https://github.com/loganmarchione/homelab-svg-assets/tree/main/assets) directory.

## PHP usage

Icons are available in PHP as a package on [Packagist](https://packagist.org/packages/loganmarchione/homelab-svg-assets).  

Run `composer require loganmarchione/homelab-svg-assets`, or add the package to your `composer.json` file (below)

```
{
    "require": {
        "loganmarchione/homelab-svg-assets"
    }
}
```

Icons will be available at `./vendor/loganmarchione/homelab-svg-assets/assets/linux.svg`

## Hugo usage

There is a [go.mod](https://github.com/loganmarchione/homelab-svg-assets/blob/main/go.mod) file, so this icon pack can be used as a [Hugo module](https://gohugo.io/hugo-modules/). You need to be using at least Hugo [0.56.0](https://gohugo.io/news/0.56.0-relnotes/).

In your Hugo site directory, initialize your site as a module:

```
hugo mod init foo
```

In your `config.yaml` (adjust for `.json` or `.toml` configuration files), add the section below:

```
module:
  imports:
    - path: github.com/loganmarchione/homelab-svg-assets
      mounts:
        - source: assets
          target: assets/svg/homelab-svg-assets
```

Download the module:

```
hugo mod get -u
```

Create a shortcode in the location below:

```
layouts/shortcodes/homelab.html
```

Copy/paste the following code into the shortcode (you can apply custom CSS using the class `blah` in the example):

```
{{/*Get the parameters */}}
{{ $path := (.Get "src") }}

{{/* Concat to create the correct path */}}
{{- $icon := resources.Get (print "svg/homelab-svg-assets/" $path ".svg" ) -}}

<span class="blah">{{- $icon.Content | safeHTML -}}</span>
```

Finally, in your markdown files, you can reference the icon:

```
{{< homelab src="twitter" >}}
```

# Icons

See [ICONS.md](ICONS.md) for a preview of all icons.

# Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md)

# Legal

See [DISCLAIMER.md](DISCLAIMER.md)

# TODO

- [x] Add Hugo working example
- [x] Add LICENSE.md
- [x] Add DISCLAIMER.md
- [ ] Verify auto-update [Packagist hook](https://packagist.org/about#how-to-update-packages) is working
- [ ] Add `data.json` to collect brand guidelines and legal requirements
- [ ] Write Python script to dynamically generate `ICONS.md` from `data.json` file
- [ ] Go through list of icons to find any that require the registered trademark (®) or trademark symbol (™) to be added
- [ ] Add Diagrams.net library (need)
