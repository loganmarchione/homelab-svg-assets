# svg_assets

I typically need full-color SVGs logos of open-source software or brands, but they're hard to find, or I don't like to link to them directly.

Other projects exist (like [Simple Icons](https://simpleicons.org/) or [Bootstrap Icons](https://icons.getbootstrap.com/)), but I've found they don't fit my needs.

This repo will serve as a source of icons, used in my personal projects.

| Icon                                                | Name                                       | Source                                                                                                                         |
| --------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| ![](./assets/argo-icon-color.svg)                   | Argo                                       | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/etcd-icon-color.svg)                   | etcd                                       | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/flux-icon-color.svg)                   | Flux                                       | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/helm-icon-color.svg)                   | Helm                                       | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/k3s-icon-color.svg)                    | K3s                                        | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/kubernetes-icon-color.svg)             | Kubernetes                                 | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/longhorn-icon-color.svg)               | Longhorn                                   | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/prometheus-icon-color.svg)             | Prometheus                                 | [CNCF Branding](https://cncf-branding.netlify.app/)                                                                            |
| ![](./assets/rancher-cow.svg)                       | Rancher (cow)                              | [GitHub](https://github.com/rancher/ui/blob/master/public/assets/images/logos/welcome-cow.svg)
| ![](./assets/traefik-gopher.svg)                    | Traefik (gopher)                           | [GitHub](https://github.com/traefik/traefik/blob/master/webui/src/assets/traefik.avatar.svg)                                   | 


# Instructions

1. Download `.svg` file into `/assets` directory
1. Open each file with Inkscape
1. Resize page to 48x48
1. Group all elements of the icon
1. Resize to 48x48px (ensuring to retain ratio)
1. Center the icon on page both horizontally and vertically
  1. The icon should be touching at least two sides of the page now
1. Ungroup all elements of the icon
1. Clean up document (`File--->Clean Up Document`)
1. Save the `.svg` file
1. Run `svgo *.svg` to optimize images
1. Add to the table in the `README.md` file