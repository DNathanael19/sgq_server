(function () {
  'use strict'
//----------------
const ctx = document.getElementById('myChart').getContext('2d');

// Dados para o gráfico


// Crie o gráfico
new Chart(ctx, {
  type: 'scatter', // Use o tipo de gráfico que desejar (scatter, line, etc.)
  data: data,
  options: {
    // Personalize as opções conforme necessário
  },
});






})()








/*
const ctx = document.getElementById('myChart');
new Chart(ctx, {
  type: 'line',  //line
  data: data,
  options: {
    scales: {
      x: {
        type: 'linear',
        position: 'bottom'
      }
      
      
    }
  }






















//------------------------
});*/






















/* other type
(function () {
  'use strict'

  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'pratico',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 3
      },


      {
        label: 'teorico',
        data: [89, 30, 3, 105, 1, 10],
        borderWidth: 3
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
})()*/




