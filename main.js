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

// Synchronously read a text file from the web server with Ajax
//
// The filePath is relative to the web page folder.
// Example:   myStuff = loadFile("Chuuk_data.txt");
//
// You can also pass a full URL, like http://sealevel.info/Chuuk1_data.json, but there
// might be Access-Control-Allow-Origin issues. I found it works okay in Firefox, Edge,
// or Opera, and works in IE 11 if the server is configured properly, but in Chrome it only
// works if the domains exactly match (and note that "xyz.com" & "www.xyz.com" don't match).
// Otherwise Chrome reports an error:
//
//   No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://sealevel.info' is therefore not allowed access.
//
// That happens even when "Access-Control-Allow-Origin *" is configured in .htaccess,
// and even though I verified the headers returned (you can use a header-checker site like
// http://www.webconfs.com/http-header-check.php to check it). I think it's a Chrome bug.
function loadFile(filePath) {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if (xmlhttp.status==200 || '') {
      result = xmlhttp.responseText;
    }
    return result;
  }