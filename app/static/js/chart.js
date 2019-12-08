
var ctx = document.getElementById('chartBlogger').getContext('2d');
elementosRotulo = $('.rotulo')
elementosQuantidade = $('.quantidade')

rotulos = []
quantidade = []

for(i=0;i<elementosRotulo.length;i++){
    rotulos.push(elementosRotulo[i].value)
}

for(i=0;i<elementosQuantidade.length;i++){
    quantidade.push(elementosQuantidade[i].value)
}


var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: rotulos,
        datasets: [{
            label: 'Quantidades',
            data: quantidade,
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

$('.quantidade').remove()
$('.rotulo').remove()


elementospost = $('.postface')
elementosreacoes = $('.reacoes')

posts = []
reacoes = []

for(i=0;i<elementospost.length;i++){
    posts.push(elementospost[i].value)
}

for(i=0;i<elementosreacoes.length;i++){
    reacoes.push(elementosreacoes[i].value)
}

var ctxFacebook = document.getElementById('chartFacebook').getContext('2d');
var myChart = new Chart(ctxFacebook, {
    type: 'line',
    data: {
        labels: posts,
        datasets: [{
            label: 'Reacoes',
            data: reacoes,
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
