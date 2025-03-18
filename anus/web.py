import os
from fastapi import FastAPI
from anus.core.orchestrator import AgentOrchestrator

app = FastAPI(title="ANUS API", description="Autonomous Networked Utility System API")
orchestrator = AgentOrchestrator()

@app.get("/")
async def root():
    return {"message": "Welcome to ANUS API - Autonomous Networked Utility System"}

@app.post("/execute")
async def execute_task(task: str, mode: str = "single"):
    result = orchestrator.execute_task(task, mode=mode)
    return result

def start_server(host="0.0.0.0", port=None):
    """Start the FastAPI server"""
    import uvicorn
    
    # Get port from environment variable or use default
    port = int(port or os.environ.get("PORT", 8000))
    
    # Start server
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_server() 