
var ctx = document.getElementById('chartFacebook').getContext('2d');
ctx.canvas.width = 100;
ctx.canvas.height = 100;
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Fev', 'Mar'],
        datasets: [{
            label: 'Reações',
            data: [54, 64, 35],
            backgroundColor: 'rgba(24, 47, 71, 0.3)',
            borderColor: 'rgba(24, 47, 71, 1)'  ,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var ctx = document.getElementById('chartInstagram').getContext('2d');
ctx.canvas.width = 100;
ctx.canvas.height = 100;
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Fev', 'Mar'],
        datasets: [{
            label: 'Curtidas',
            data: [54, 64, 35],
            backgroundColor: 'rgba(24, 47, 71, 0.3)',
            borderColor: 'rgba(24, 47, 71, 1)'  ,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var ctx = document.getElementById('chartBlog').getContext('2d');
ctx.canvas.width = 100;
ctx.canvas.height = 100;
var myChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ['Jan', 'Fev', 'Mar'],
        datasets: [{
            label: 'Acessos',
            data: [54, 64, 35],
            backgroundColor: 'rgba(24, 47, 71, 0.3)',
            borderColor: 'rgba(24, 47, 71, 1)'  ,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});