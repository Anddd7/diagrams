# MAIN branch for Anddd7

Since the upstream repo is inactive, this fork will use main as the active branch.

- master: keep the same as upstream
- main: my active branch

## How to use

build the package

```sh
poetry install
poetry build
```

install as a local dependencies

```sh
pdm add <your-path>/diagrams-ext/dist/diagrams-0.23.5a0-py3-none-any.whl 
```

## How to maintain

- checkout from main branch, add feat/fix/..., create PR and merge to main
- if it's usable, create PR to upstream/master

## Features

- [x] cluster icon: <https://github.com/Anddd7/diagrams-ext/pull/1>
  - ~~<https://github.com/mingrammer/diagrams/pull/853>~~
  - ~~<https://github.com/mingrammer/diagrams/pull/439>~~
  - ~~<https://github.com/mingrammer/diagrams/pull/438>~~
- [ ] overlapping cluster: <https://github.com/mingrammer/diagrams/issues/852>
- [ ] edge attr: <https://github.com/mingrammer/diagrams/issues/560>

- [ ] read tfstate and generate graph
  - <https://github.com/cycloidio/inframap>
  - <https://github.com/28mm/blast-radius>

- [ ] read aws cli and generate graph
  - <https://github.com/Cloud-Architects/cloudiscovery>

- [ ] other terraform interesting tools
  - <https://github.com/cycloidio/terracost>
  - <https://pypi.org/project/python-hcl2/>