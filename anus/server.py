import os
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import json

from anus.core.orchestrator import AgentOrchestrator

# Initialiseer FastAPI app
app = FastAPI(title="ANUS API", description="Autonomous Networked Utility System")

# Voeg CORS middleware toe
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creëer een Orchestrator instantie
orchestrator = AgentOrchestrator()

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ANUS - Autonomous Networked Utility System</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
                line-height: 1.6;
                color: #333;
            }
            h1 {
                color: #635bff;
                margin-bottom: 1rem;
            }
            .container {
                background-color: #f6f9fc;
                border: 1px solid #e3e8ee;
                border-radius: 8px;
                padding: 2rem;
                margin-top: 2rem;
            }
            .chat-form {
                margin-top: 1.5rem;
            }
            textarea {
                width: 100%;
                padding: 12px;
                border: 1px solid #e3e8ee;
                border-radius: 4px;
                height: 100px;
                margin-bottom: 1rem;
                font-family: inherit;
            }
            select {
                padding: 8px;
                border: 1px solid #e3e8ee;
                border-radius: 4px;
                margin-bottom: 1rem;
            }
            button {
                background-color: #635bff;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 12px 24px;
                font-weight: 600;
                cursor: pointer;
            }
            button:hover {
                background-color: #5851db;
            }
            .response {
                margin-top: 1.5rem;
                white-space: pre-wrap;
            }
            .footer {
                margin-top: 2rem;
                font-size: 0.9rem;
                color: #666;
                text-align: center;
                border-top: 1px solid #e3e8ee;
                padding-top: 1rem;
            }
        </style>
        <script>
            async function submitForm() {
                const userInput = document.getElementById('userInput').value;
                const mode = document.getElementById('mode').value;
                const resultDiv = document.getElementById('result');
                
                resultDiv.innerHTML = "ANUS denkt na...";
                
                try {
                    const response = await fetch('/execute', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            task: userInput,
                            mode: mode
                        }),
                    });
                    
                    const data = await response.json();
                    resultDiv.innerHTML = `<strong>ANUS:</strong> ${data.result}`;
                } catch (error) {
                    resultDiv.innerHTML = `Er is een fout opgetreden: ${error.message}`;
                }
            }
        </script>
    </head>
    <body>
        <h1>ANUS AI</h1>
        <h3>Autonomous Networked Utility System</h3>
        
        <div class="container">
            <h3>Chat met ANUS</h3>
            <div class="chat-form">
                <textarea id="userInput" placeholder="Typ je vraag of opdracht..."></textarea>
                <div>
                    <label for="mode">Mode: </label>
                    <select id="mode">
                        <option value="single">Single</option>
                        <option value="multi">Multi</option>
                    </select>
                </div>
                <button onclick="submitForm()">Verstuur</button>
            </div>
            <div id="result" class="response"></div>
        </div>
        
        <div class="footer">
            ANUS is een AI framework dat gebruik maakt van geavanceerde technieken om je te helpen met diverse taken.
        </div>
    </body>
    </html>
    """
    return html_content

# API endpoint voor het uitvoeren van taken
@app.post("/execute")
async def execute(request: Request):
    data = await request.json()
    task = data["task"]
    mode = data.get("mode", "single")
    
    try:
        result = orchestrator.execute_task(task, mode=mode)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

# Start de server als dit script direct wordt uitgevoerd
if __name__ == "__main__":
    # Krijg de poort uit de omgevingsvariabele of gebruik standaard 10000
    port = int(os.environ.get("PORT", 10000))
    
    # Start de uvicorn server met de juiste configuratie
    uvicorn.run(
        "anus.server:app",
        host="0.0.0.0",  # Bind aan alle interfaces
        port=port,
        reload=False
    ) 