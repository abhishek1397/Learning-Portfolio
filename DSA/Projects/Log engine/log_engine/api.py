from fastapi import FastAPI
from processor import LogProcessor
from config import TOP_K
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Global processor instance
processor = LogProcessor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/metrics/error_rate")
def error_rate():
    return {"error_rate": processor.get_error_rate()}


@app.get("/metrics/top_ips")
def top_ips():
    return {"top_ips": processor.get_top_k_ips(TOP_K)}


@app.get("/metrics/service_load")
def service_load():
    return {"services": processor.get_service_counts()}


@app.get("/alerts")
def alerts():
    return {"alerts": processor.check_alerts()}


@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Log Monitoring Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: white;
            margin: 0;
            padding: 20px;
        }

        h1 {
            text-align: center;
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .card {
            background: #1e293b;
            padding: 15px;
            border-radius: 10px;
        }

        .alert {
            background: #7f1d1d;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 15px;
            display: none;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 8px;
            text-align: left;
        }

        th {
            background: #334155;
        }

        .metric {
            font-size: 20px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<h1>Real-Time Log Monitoring</h1>

<div id="alertBox" class="alert"></div>

<div class="grid">

    <div class="card">
        <div class="metric">Error Rate (Last 60s)</div>
        <canvas id="errorChart"></canvas>
    </div>

    <div class="card">
        <div class="metric">Service Load</div>
        <canvas id="serviceChart"></canvas>
    </div>

    <div class="card">
        <div class="metric">Top IPs</div>
        <table id="ipTable">
            <thead>
                <tr>
                    <th>IP Address</th>
                    <th>Requests</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

</div>

<script>
    const errorCtx = document.getElementById('errorChart').getContext('2d');
    const serviceCtx = document.getElementById('serviceChart').getContext('2d');

    let labels = [];
    let errorData = [];

    const errorChart = new Chart(errorCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Error Rate',
                data: errorData,
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239,68,68,0.2)'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { min: 0, max: 1 }
            }
        }
    });

    const serviceChart = new Chart(serviceCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Requests',
                data: [],
                backgroundColor: '#3b82f6'
            }]
        }
    });

    async function updateDashboard() {
        const errorRes = await fetch('/metrics/error_rate');
        const errorJson = await errorRes.json();

        const serviceRes = await fetch('/metrics/service_load');
        const serviceJson = await serviceRes.json();

        const ipRes = await fetch('/metrics/top_ips');
        const ipJson = await ipRes.json();

        const alertRes = await fetch('/alerts');
        const alertJson = await alertRes.json();

        const time = new Date().toLocaleTimeString();

        // Update error chart
        labels.push(time);
        errorData.push(errorJson.error_rate);

        if (labels.length > 20) {
            labels.shift();
            errorData.shift();
        }

        errorChart.update();

        // Update service chart
        serviceChart.data.labels = Object.keys(serviceJson.services);
        serviceChart.data.datasets[0].data = Object.values(serviceJson.services);
        serviceChart.update();

        // Update Top IP table
        const tableBody = document.querySelector("#ipTable tbody");
        tableBody.innerHTML = "";
        ipJson.top_ips.forEach(([count, ip]) => {
            const row = `<tr>
                <td>${ip}</td>
                <td>${count}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });

        // Update Alerts
        const alertBox = document.getElementById("alertBox");
        if (alertJson.alerts.length > 0) {
            alertBox.style.display = "block";
            alertBox.innerHTML = alertJson.alerts.join("<br>");
        } else {
            alertBox.style.display = "none";
        }
    }

    setInterval(updateDashboard, 2000);
</script>

</body>
</html>
"""