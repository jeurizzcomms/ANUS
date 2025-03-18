import os
import uvicorn
from fastapi import FastAPI

# Create a basic FastAPI application
app = FastAPI(title="ANUS - Autonomous Networked Utility System")

@app.get("/")
async def root():
    return {"message": "ANUS is up and running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    # The crucial part: Get the port from environment variables (Render sets this)
    port = int(os.environ.get("PORT", 10000))
    
    # Log for debugging
    print(f"==> Starting ANUS server on port {port}")
    print(f"==> Binding to host 0.0.0.0 and port {port}")
    
    # Run with explicit host and port binding
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info") 