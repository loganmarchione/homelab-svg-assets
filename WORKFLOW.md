# Workflow

Most of this is taken from the [CONTRIBUTING.md](https://github.com/simple-icons/simple-icons/blob/develop/CONTRIBUTING.md) file from the [Simple Icons](https://simpleicons.org/) project

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Get software](#1-get-software)
- [Setup Inkscape](#2-setup-inkscape)
- [Identify icon](#3-identify-icon)
- [Adding an icon](#4-adding-an-icon)
- [Name the icon](#5-name-the-icon)
- [Optimizing an icon](#6-optimizing-an-icon)
- [Annotating an icon](#7-annotating-an-icon)
- [Updating the README](#8-updating-the-readme)
- [Workflow for publishing a new version](#9-workflow-for-publishing-a-new-version)

# 1. Get software

1. Download [Inkscape](https://inkscape.org/). It's free for Windows, Mac, and Linux.
1. Install [svgo](https://github.com/svg/svgo) (this is used to optimize SVGs)
1. Install `scour` on Linux (not sure if this is needed on Windows or Mac)
    - Arch = `sudo pacman -S scour`
    - Ubuntu = `sudo apt-get install python3-scour`

# 2. Setup Inkscape

You only need to do this once:

1. `Edit-->Preferences-->Behavior-->Transforms-->Scale stroke width` = Enabled

# 3. Identify icon

Only homelab-related icons will be added (e.g., Burger King will not be added). In addition, the following icons will not be added:

- Government organizations 
- Flags and banners
- Universities or educational institutions

When possible, icons should be sought from official sources first, only then falling back on unofficial sources. The order below should be the preferred order.

1. About pages, Press pages, Media Kits, and Brand Guidelines (example [here](https://github.com/logos) and [here](https://www.hashicorp.com/brand))
1. Website images (example [here](https://gohugo.io/))
1. GitHub repositories (example [here](https://github.com/kubernetes/kubernetes/blob/master/logo/logo.svg))
    - If the main project repo doesn't contain any images, be sure to check for a repo that contains a project website (example [here](https://github.com/lxc/linuxcontainers.org/blob/master/static/img/containers.svg)) or a repo that specifically contains branding and icons (example [here](https://github.com/miniflux/logo/blob/master/icon.svg))
1. Wikipedia (example [here](https://en.wikipedia.org/wiki/OpenZFS))

# 4. Adding an icon

1. Open each file with Inkscape
1. Resize the document and viewbox to 48x48
1. Select all elements of the icon and create a group (this helps during resizing/alignment)
1. Resize the icon to 48x48 (ensuring to retain ratio)
1. Center the icon on page both horizontally and vertically (the icon should be touching at least two sides of the document now)
1. Clean up document (`File--->Clean Up Document`)
1. Save the SVG file to the `assets` directory
    1. Be sure to use `Optimized SVG` filetype
    1. On the `SVG Output` tab:
       - Check `Remove metadata`
       - Check `Remove comments`
       - Uncheck `Embed raster images`
       - Check `Enable viewboxing`

# 5. Name the icon

Each icon will have two names:
- A filename (e.g., `filename.svg`)
- A display name

Adhere to the following rules when choosing filenames:

1. Use the lowercase [ISO basic Latin alphabet](https://en.wikipedia.org/wiki/ISO_basic_Latin_alphabet) with no whitespaces.
   | Correct                 | Incorrect               |
   |-------------------------|-------------------------|
   | `github.svg`            | `GitHub.svg`            |
   | `microsoftedge.svg`     | `microsoft edge.svg`    |
1. Replace symbols in the brand name with their spelled-out words.
   | Correct                 | Incorrect               |
   |-------------------------|-------------------------|
   | `cplusplus.svg`         | `c++.svg`               |
   | `diagramsdotnet.svg`    | `diagrams.net.svg`      |
1. Use a dash (`-`) to indicate a separate version of the icon.
   ```
   bash-dark.svg
   bash-light.svg
   ```
1. When a brand is part of the product name, use it in the filename.
   | Correct                 | Incorrect               |
   |-------------------------|-------------------------|
   | `apachesolr.svg`        | `solr.svg`              |

# 6. Optimizing an icon

1. Run `svgo` to optimize the image (the default settings are fine) 
   ```
   svgo assets/filename.svg
   ```

# 7. Annotating an icon

Manually check each icon to ensure it **HAS** these settings:

- The SVG namespace
    ```
    xmlns="http://www.w3.org/2000/svg"
    ```
- A 48x48 viewbox
    ```
    viewBox="0 0 48 48"
    ```

Below is a partial example of a file.
```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">...</svg>
```

Manually check each icon to ensure it **DOES NOT** have these settings:

- `xlink` - This is usually caused by cloned shapes. You can remove this by selecting the clones and choosing `Edit-->Clone-->Unlink Clone`.
    - This might be harder to remove depending on the design. Try your best.
- `height` or `width` - Instead, use `viewBox` as show above.
- Make sure there is no `png` data encoded into each file.

# 8. Updating the JSON file

Add the icon to the `icons.json` file. There are four lines for each icon:

1. Path: The path in the `assets` directory to the icon
1. Name: The display name that will be shown in the final markdown file
1. A link to the source where you found the SVG file
1. A link to the brand's guidelines
    - If none exist, leave blank
    - The guidelines may be the same as the source

When adding to the `icons.json` file, use the following guidelines:

1. Use alphabetical order by the display name (not the filename)
1. The display name can have symbols (e.g., `C++` or `Diagrams.net`)
1. Separate version of the icon should have descriptive display names (e.g., `Bash (dark)` and `Bash (light)`)
1. The display name should be stylized as per the brand's requirements (e.g., `ownCloud` instead of `OwnCloud`)
1. The display name can have more information about the icon (e.g., the Linux penguin's name is Tux!)

A full example is below:

```
        {
            "path": "./assets/gimp.svg",
            "name": "GIMP (Wilber)",
            "source": "https://gitlab.gnome.org/Infrastructure/gimp-web/blob/master/themes/newgimp/static/images/gimp.svg",
            "guidelines": "https://www.gimp.org/about/linking.html"
        },
```

# 9. Workflow for publishing a new version

1. Install Python requirements
    ```
    pip3 install --user -r requirements.txt
    ```
1. Run the Python script 
    ```
    python3 scripts/convert_json.py
    ```
1. Get current git tags
   ```
   git tag
   ```
1. Increment the version number in `package.json` to match a new git tag
1. Do git work
    ```
    git add .
    git commit -m "Text goes here"
    git push
    git tag -a X.Y.Z -m "X.Y.Z - Text goes here"
    git push origin X.Y.Z
    ```
1. Publish to NPM
   ```
   npm publish --access public
   ```