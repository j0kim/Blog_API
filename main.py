from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Data": "Fast API"}

# Get posts
@app.get("/posts")
async def get_posts():
    return {"Data": "User Posts"}

# Get individual post
@app.get("/posts/{id}")
async def get_posts(id: int):
    return {"Data": "Particular user Post"}

# Create Post
@app.post("/posts")
async def create_post(post):
    return {"Data": "Post successfully created"}

# Update Post
@app.put("/posts/{id}")
async def update_post(id:int, post):
    return {"Data": "Post has been successfully updated"}

# Delete Post
@app.delete("/posts/{id}")
async def delete_post(id:int):
    return {"Data": "Post was successfully deleted"}