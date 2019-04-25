google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawTrendlines);

const LOG = ''

// prepare data ie parse .csv

function parseCSV(file){
    output = [];

    
}

parseCSV()


function drawTrendlines() {
      var data = new google.visualization.DataTable();
      data.addColumn('number', 'X');
      data.addColumn('number', 'Dogs');
      data.addColumn('number', 'Cats');

      data.addRows([
        [0, 0, 0],
            [1, 10, 5],
               [2, 23, 15]
      ]);

      var options = {
        hAxis: {
          title: 'Time'
        },
        vAxis: {
          title: 'Popularity'
        },
        colors: ['#AB0D06', '#007329'],
        trendlines: {
          0: {type: 'exponential', color: '#333', opacity: 1},
          1: {type: 'linear', color: '#111', opacity: .3}
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }