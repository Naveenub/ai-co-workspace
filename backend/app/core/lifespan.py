from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    print("Starting up AI Co-Workspace backend...")
    # Add startup code here
    yield
    print("Shutting down backend...")
