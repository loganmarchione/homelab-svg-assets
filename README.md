# homelab-svg-assets

<a href="https://github.com/loganmarchione/homelab-svg-assets/tree/main/assets"><img src="https://img.shields.io/github/directory-file-count/loganmarchione/homelab-svg-assets/assets?extension=svg&label=Total%20Icons&type=file" alt="Total Icons"/></a>
<a href="https://github.com/loganmarchione/homelab-svg-assets"><img src="https://img.shields.io/github/repo-size/loganmarchione/homelab-svg-assets??label=Repo%20Size" alt="Repo Size"/></a>


[![Lint](https://github.com/loganmarchione/homelab-svg-assets/actions/workflows/main.yml/badge.svg)](https://github.com/loganmarchione/homelab-svg-assets/actions/workflows/main.yml)
[![Lint](https://img.shields.io/github/stars/loganmarchione/homelab-svg-assets?style=social)](https://github.com/loganmarchione/homelab-svg-assets/stargazers)


<a href="https://github.com/loganmarchione/homelab-svg-assets/tags"><img src="https://img.shields.io/github/v/tag/loganmarchione/homelab-svg-assets?color=green&logo=github&label=Latest%20GitHub%20Tag&sort=semver" alt="Latest GitHub Tag"/></a>
<a href="https://packagist.org/packages/loganmarchione/homelab-svg-assets"><img src="https://img.shields.io/packagist/v/loganmarchione/homelab-svg-assets?color=green&logo=packagist&logoColor=white&label=Latest%20Packagist%20Version" alt="Latest Packagist Version"/></a>
<a href="https://www.npmjs.com/package/@loganmarchione/homelab-svg-assets"><img src="https://img.shields.io/npm/v/@loganmarchione/homelab-svg-assets?color=green&logo=npm&label=Latest%20NPM%20Version" alt="Latest NPM Version"/></a>

Over 575 full-color SVG icons of homelab-related software, products, and brands in a normalized size.

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Usage](#usage)
  - [General usage](#general-usage)
  - [Diagrams.net usage](#diagramsnet-usage)
  - [CDN usage](#cdn-usage)
  - [PHP usage](#php-usage)
  - [NPM usage](#npm-usage)
  - [Hugo usage](#hugo-usage)
- [Legal](#legal)
- [Other icon sets](#other-icon-sets)
- [TODO](#todo)

# Usage

⚠️ All users should read the [disclaimer](DISCLAIMER.md) before using this project. ⚠️

## General usage

Icons as SVGs are available in the [assets](https://github.com/loganmarchione/homelab-svg-assets/tree/main/assets) directory. See [ICONS.md](ICONS.md) for a preview of all icons.

## Diagrams.net usage

In a [Diagrams.net](https://app.diagrams.net/) project, go to `File-->Open Library from-->URL` and paste in the URL below (it will take a second to load)

```
https://raw.githubusercontent.com/loganmarchione/homelab-svg-assets/main/homelab-svg-assets.xml
```

You can also start brand new project with the library built-in to the URL by using [this link](https://app.diagrams.net/?clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Floganmarchione%2Fhomelab-svg-assets%2Fmain%2Fhomelab-svg-assets.xml) (also below)

```
https://app.diagrams.net/?clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Floganmarchione%2Fhomelab-svg-assets%2Fmain%2Fhomelab-svg-assets.xml
```

If you self-host Diagrams.net (it is available as a [Docker container](https://hub.docker.com/r/jgraph/drawio)), you can replace the domain with your custom domain

```
https://drawio.yourdomain.com/?clibs=Uhttps%3A%2F%2Fraw.githubusercontent.com%2Floganmarchione%2Fhomelab-svg-assets%2Fmain%2Fhomelab-svg-assets.xml
```

## CDN usage

Icons are available via [jsDelivr](https://www.jsdelivr.com/package/npm/@loganmarchione/homelab-svg-assets).

Replace the icon name as needed. You can also replace `latest` with a specific version.

```
<img height="48" width="48" src="https://cdn.jsdelivr.net/npm/@loganmarchione/homelab-svg-assets@latest/assets/linux.svg"/>
```

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

## NPM usage
Icons are available as a package on [NPM](https://www.npmjs.com/package/@loganmarchione/homelab-svg-assets).

Run `npm install @loganmarchione/homelab-svg-assets`, or add the package to your `package.json` file (below)

```
{
  "dependencies": {
    "@loganmarchione/homelab-svg-assets": "*"
  }
}
```

Icons will be available at `./node_modules/@loganmarchione/homelab-svg-assets/assets/linux.svg`

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
{{< homelab src="linux" >}}
```

# Legal

See [DISCLAIMER.md](DISCLAIMER.md)

# Other icon sets

It would be remiss of me if I did not mention other great icons sets

- [Simple Icons](https://simpleicons.org/) - Monochromatic SVG icons for popular brands
- [Bootstrap Icons](https://icons.getbootstrap.com/) - Mostly generic icons, but some brand icons
- [Font Awesome](https://fontawesome.com/icons) - Mix of generic and brand icons
- [Devicon](https://devicon.dev/) - Icons representing programming languages, designing & development tools
- [Dashboard Icons](https://github.com/walkxcode/dashboard-icons/tree/main) - Mix of SVG and PNG dashboard icons
- [Aegis Icons](https://github.com/aegis-icons/aegis-icons) - Unofficial 2FA entry icons for open source Android authenticator Aegis
