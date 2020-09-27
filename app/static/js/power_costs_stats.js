const renderPowerCostsSummaryUsage = (months, usage) => {
    var ctx = document.getElementById('power-monthly-costs');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: months,
            datasets: [{
                label: " ",
                data: usage,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1,
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Electricity Costs per month',
                fontSize: 20,
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel:{
                        display: true,
                        labelString: 'Costs zł/month',
                        fontSize: 18,
                    },
                }],
                xAxes: [{
                    scaleLabel:{
                        display: true,
                        labelString: 'Months',
                        fontSize: 18,
                    },
                }],
            },
        }
    });
};

const getPowerCostsData = () => {
    fetch('/power-summary-costs')
    .then((res) => res.json())
    .then((results,) => {
        console.log("results", results);
        const summary = results.summary;
        const [month, usage,] = [
            Object.keys(summary),
            Object.values(summary),
        ];
        return renderPowerCostsSummaryUsage(month, usage);
    });
}

document.onload = getPowerCostsData();