<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Butterfly Data Visualization - Enchanted Wings</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #fce4ec;
            margin: 0;
            padding: 30px;
            color: #333;
            text-align: center;
        }

        h1 {
            color: #d81b60;
            margin-bottom: 10px;
        }

        .chart-container {
            margin: 40px auto;
            max-width: 700px;
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        canvas {
            max-width: 100%;
        }
    </style>
</head>
<body>
    <h1>🦋 Enchanted Wings: Data Visualization</h1>
    <p>Insights into butterfly species, colors, and rarity</p>

    <div class="chart-container">
        <h2>Species Distribution</h2>
        <canvas id="speciesChart"></canvas>
    </div>

    <div class="chart-container">
        <h2>Wing Color Patterns</h2>
        <canvas id="colorChart"></canvas>
    </div>

    <div class="chart-container">
        <h2>Rarity Status</h2>
        <canvas id="rarityChart"></canvas>
    </div>

    <script>
        const speciesCtx = document.getElementById('speciesChart').getContext('2d');
        new Chart(speciesCtx, {
            type: 'bar',
            data: {
                labels: ['Monarch', 'Swallowtail', 'Morpho', 'Painted Lady', 'Red Admiral'],
                datasets: [{
                    label: 'Number of Sightings',
                    data: [120, 90, 60, 80, 70],
                    backgroundColor: ['#ff6384','#36a2eb','#cc65fe','#ffce56','#00c853']
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });

        const colorCtx = document.getElementById('colorChart').getContext('2d');
        new Chart(colorCtx, {
            type: 'pie',
            data: {
                labels: ['Orange', 'Blue', 'Black', 'Yellow', 'White'],
                datasets: [{
                    data: [30, 20, 25, 15, 10],
                    backgroundColor: ['#ffa726', '#42a5f5', '#212121', '#ffee58', '#e0e0e0']
                }]
            },
            options: {
                responsive: true
            }
        });

        const rarityCtx = document.getElementById('rarityChart').getContext('2d');
        new Chart(rarityCtx, {
            type: 'doughnut',
            data: {
                labels: ['Common', 'Uncommon', 'Rare', 'Endangered'],
                datasets: [{
                    data: [50, 30, 15, 5],
                    backgroundColor: ['#81c784', '#64b5f6', '#ffb74d', '#e57373']
                }]
            },
            options: {
                responsive: true
            }
        });
    </script>
</body>
</html>
