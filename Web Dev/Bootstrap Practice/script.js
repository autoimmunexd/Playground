var ctx = document.getElementById('chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['10s', '10s','10s'], // This will be your time axis (e.g., ['1s', '2s', '3s', ...])
        datasets: [
            {
                label: 'CPU Utilization',
                data: [25, 40, 90, 1, 50, 40,25, 40, 90, 1, 50, 40,25, 40, 90, 1, 50, 40,25, 40, 90, 1, 50, 40,25, 40, 90, 1, 50, 40,25, 40, 90, 1, 50, 40], // This will be your CPU utilization data (e.g., [30, 45, 25, ...])
                borderColor: 'rgba(75, 192, 192, 1)',
                tension: 0.1
            },
            {
                label: 'Memory Utilization',
                data: [45, 55, 50, 50, 50, 50, 52, 90, 95, 100, 20], // This will be your memory utilization data (e.g., [20, 35, 50, ...])
                borderColor: 'rgba(192, 75, 75, 1)',
                tension: 0.1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});