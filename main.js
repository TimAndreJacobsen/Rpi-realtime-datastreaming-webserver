google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawTrendlines);

const logPath = ''

const day1 = new Date(2019, 04, 24, 17, 00, 28);
const day2 = new Date(2019, 05, 24, 17, 00, 28);
const day3 = new Date(2019, 04, 24, 23, 00, 28);



// prepare data ie parse .csv

function parseCSV(file){
    output = [];

    
}

parseCSV()


function drawTrendlines() {
      var data = new google.visualization.DataTable();
      data.addColumn('datetime', 'X');
      data.addColumn('number', 'Dogs');
      data.addColumn('number', 'Cats');

      data.addRows([
        [day1, 0, 0],
            [day2, 10, 5],
               [day3, 23, 15]
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
          1: {type: 'linear', color: '#111', opacity: .3}
        }
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }