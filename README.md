# starlette-rootpath-middleware

FastAPI 0.146.0 deprecated `FastAPI()`'s `root_path` parameter in favor of a `--root-path` command-line flag to
`fastapi run`. If you specifically need to set the root path at runtime, you can use this middleware.

Though built for FastAPI, there is nothing FastAPI-specific about this middleware and it should work
with all Starlette applications.

## Installation

```shell
pip install starlette-rootpath-middleware
```

## Usage

```python
from fastapi import FastAPI
from starlette_rootpath_middleware import RootPathMiddleware

app = FastAPI()
app.add_middleware(RootPathMiddleware, root_path="/some/path/")
```