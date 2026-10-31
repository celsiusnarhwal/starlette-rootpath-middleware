from starlette.types import ASGIApp, Receive, Scope, Send


__all__ = ["RootPathMiddleware"]


class RootPathMiddleware:
    def __init__(self, app: ASGIApp, root_path: str):
        self.app = app
        self.root_path = root_path.rstrip("/")

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] in ["http", "websocket"] and self.root_path:
            scope = {**scope, "root_path": self.root_path}

        await self.app(scope, receive, send)
