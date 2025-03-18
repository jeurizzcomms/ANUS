import os
import socket
import uvicorn
from fastapi import FastAPI

# Logging voor debugging
print("Minimale server startup gestart...")
print(f"Current working directory: {os.getcwd()}")
print(f"Environment PORT: {os.environ.get('PORT', '10000')}")

# Maak een ultra-eenvoudige app
app = FastAPI(title="ANUS Minimal API")

# Health check endpoint
@app.get("/health")
async def health_check():
    print("Health check aangeroepen")
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
async def root():
    print("Root endpoint aangeroepen")
    return {"message": "ANUS Minimal Server is running"}

def is_port_available(host, port):
    """Test of poort beschikbaar is voor binding."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((host, port))
        sock.close()
        return True
    except:
        sock.close()
        return False

# Dit script wordt direct uitgevoerd
if __name__ == "__main__":
    # Krijg de poort uit de environment variable
    port = int(os.environ.get("PORT", 10000))
    host = "0.0.0.0"
    
    print(f"Probeer te binden aan {host}:{port}...")
    
    # Test of poort beschikbaar is
    if not is_port_available(host, port):
        print(f"WAARSCHUWING: Poort {port} lijkt al in gebruik te zijn!")
    else:
        print(f"Poort {port} is beschikbaar voor binding")
    
    # Start de server
    print(f"Server start nu op {host}:{port}...")
    uvicorn.run(
        "anus.minimal_server:app",
        host=host,
        port=port,
        log_level="debug"
    ) 