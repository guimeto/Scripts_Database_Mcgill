
var today = new Date();
var year=  today.getFullYear();
today.setMinutes(0);
var yesterday = today.setDate(today.getDate() - 1) -  today.getTimezoneOffset() * 60000;
var today2 = today -  today.getTimezoneOffset() * 60000;

///Panneau sur les températures
var options1 = {

  chart: {
    renderTo: 'graphdiv',
    zoomType: 'xy',
  },
  title: {
    text: ' '
  },
  subtitle: {
    text: ' '
  },
   xAxis: [{
            type:'datetime',
            tickInterval:3600 * 1000 * 2,
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat('%b %e', this.value);

                },

            }

        }],

  yAxis: [{ // Primary yAxis
    labels: {
      format: '{value} °C',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
    title: {
      text: 'Température',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
  }, { // Secondary yAxis
    gridLineWidth: 0,
    title: {
      text: 'Précipitatation totale',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
    labels: {
      format: '{value} mm',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
       opposite: true
  }
         ]
    ,
               plotOptions: {
                 series: {
           pointStart: Date.UTC(2014, 1, 1) ,
            pointInterval:  24 * 3600 * 1000 // one day
        },
                spline: {
                    marker: {
                        enabled: false
                    }
                }
            }
   ,
         tooltip: {

    xDateFormat: '%Y-%m-%d',
    shared: true
  },

            rangeSelector:{
                enabled:true
            },
  series: [{
    name: 'Précipitation totale',
    type: 'column',
    yAxis: 1,
    data: [],
    tooltip: {
      valueSuffix: ' mm'
    }

  },
    {
    name: 'Température point de rosée',
    type: 'spline',
    data: [],
    tooltip: {
      valueSuffix: ' °C'
    },
    color: '#70db70'

  },
    {
    name: 'Température',
    type: 'spline',
    data: [],
    tooltip: {
      valueSuffix: ' °C'
    },
    color: '#ff3333'

  }


          ],
    credits: {
      enabled: false
  },
  //disable the nav export button
};
get('/data/UQAM_DATA_STATION_2018.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length; i++) {
        var cat = lines[i].split(",")[0]
        var firCol = lines[i].split(",")[4];
        var secCol = lines[i].split(",")[1];
        var thirdCol = lines[i].split(",")[2];
        options1.series[0].data.push(parseFloat(firCol))
        options1.series[1].data.push(parseFloat(secCol))
        options1.series[2].data.push(parseFloat(thirdCol))

    }

    // Create the chart
     chart = new Highcharts.Chart(options1);
});


  var checkboxes = ['Précipitation totale', 'Température point de rosée', 'Température']
  checkboxes.forEach((elem, i) => {
		var checkbox = document.getElementById(elem)
    checkbox.onchange = function() {
    		chart.series[i].update({
        		showInLegend: chart.series[i].legendItem ? false : true
        })
        chart.series[i].setVisible()
    }
})

var options2 = {

  chart: {
    type: 'heatmap',
      renderTo: 'graphdiv2',
       zoomType: 'xy',
    margin: [60, 10, 80, 50]
  },

  boost: {
    useGPUTranslations: true
  },

  title: {
    text:  'Variation de la température horaire pour: ' + year ,
    align: 'center',

  },

  subtitle: {
    text: ' '   ,
    align: 'left',
    x: 40
  },

  xAxis: {
    type: 'datetime',
    min: Date.UTC(year, 0, 1),
    max: Date.UTC(year, 12, 31, 23, 59, 59),
    labels: {
      align: 'left',
      x: 5,
      y: 14,
      format: '{value:%B}' // long month
    },
    showLastLabel: false,
    tickLength: 16
  },

  yAxis: {
    title: {
      text: 'Heures'
    },
    labels: {
      format: '{value}:00'
    },
    minPadding: 0,
    maxPadding: 0,
    startOnTick: false,
    endOnTick: false,
    tickPositions: [0, 6, 12, 18, 24],
    tickWidth: 1,
    min: 0,
    max: 23,
    reversed: true
  },

  colorAxis: {
    stops: [
      [0, '#3060cf'],
      [0.5, '#fffbbc'],
      [0.9, '#c4463a'],
      [1, '#c4463a']
    ],
    min: -20,
    max: 40,
    startOnTick: false,
    endOnTick: false,
    labels: {
      format: '{value}℃'
    }
  },
  credits: {
      enabled: false
  },

  series: [{
      data:[],
    boostThreshold: 100,
    borderWidth: 0,
    nullColor: '#EFEFEF',
    colsize: 24 * 36e5, // one day
    tooltip: {
      headerFormat: 'Température moyenne horaire<br/>',
      pointFormat: '{point.x:%e %b, %Y} {point.y}:00: <b>{point.value} ℃</b>'
    },
    turboThreshold: Number.MAX_VALUE // #3404, remove after 4.0.5 release
  }]
};
 $.get('/data/Heat_temp.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length-1; i++) {
        var firCol = lines[i].split(",")[0];
        var secCol = lines[i].split(",")[1];
        var thirdCol = lines[i].split(",")[2];
options2.series[0].data.push([Date.parse(firCol),parseFloat(secCol),parseFloat(thirdCol)])
    }

    // Create the chart
     chart = new Highcharts.Chart(options2);
});





