$(function () {
      
var today = new Date();
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
                    return Highcharts.dateFormat('%H h', this.value);

                },

            }

        }], 

  yAxis: [{ // Primary yAxis
    labels: {
      format: '{value}',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
    title: {
      text: 'Température [°C]',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
  }, { // Secondary yAxis
    gridLineWidth: 0,
    title: {
      text: 'Humidex',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
    labels: {
      format: '{value}',
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
            pointStart: yesterday,
            pointInterval:  3600 * 1000  // one hour
        },   
                spline: {
                    marker: {
                        enabled: false
                    }
                }
            }
   ,
         tooltip: {
             
     xDateFormat: '%e %b - %H h',
    shared: true   
  },
  legend: {
    layout: 'horizontal',
    align: 'center',
    floating: false,
    backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
    shadow: true
  },
  series: [{
    name: 'Humidex',
    type: 'spline',
    yAxis: 1,
    data: [],
    tooltip: {
      valueSuffix: ' '
    } ,
    color: Highcharts.getOptions().colors[0]
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
  navigation: {
    buttonOptions: {
      enabled: false
    }}
};
$.get('/static/shared/data/UQAM_DATA_STATION.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length; i++) {
        var cat = lines[i].split(",")[0]
        var firCol = lines[i].split(",")[3];
        var secCol = lines[i].split(",")[4];
        var thirdCol = lines[i].split(",")[5];
        options1.series[0].data.push(parseFloat(firCol))
        options1.series[1].data.push(parseFloat(secCol))
        options1.series[2].data.push(parseFloat(thirdCol))
        
    }

    // Create the chart
     chart = new Highcharts.Chart(options1);
});

///Panneau sur la precipitation et l'humidité relative
    
var options2 = {
    
  chart: {
    plotAreaWidth: 10,
    plotAreaHeight: 100,  
    renderTo: 'graphdiv2',
    zoomType: 'xy'
  },
  title: {
    text: ' '
  },
  subtitle: {
    text: ' '
  },
    credits: {
      enabled: false
  }
   ,
   xAxis: [{
            type:'datetime',
            tickInterval:3600 * 1000 * 2,
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat('%H h', this.value);

                },

            }

        }],
  yAxis: [{ // Primary yAxis
    labels: {
      format: '{value}',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
      max: 100,
      min: 25,
      tickInterval: 5,
      title: {
      text: 'Humidité relative [%]',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
    opposite: true

  }, { // Secondary yAxis
    gridLineWidth: 0,
    title: {
      text: 'Précipitation [mm]',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
    labels: {
      format: '{value}',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    }

  }
         ],
  tooltip: {
    shared: true,
    xDateFormat: '%e %b - %H h'
  },
  plotOptions: {
       series: {
            pointStart: yesterday,
            pointInterval: 3600000 // one hour
        },   
        spline: {
             marker: {
              enabled: false
          }
      }
      }
    ,
   legend: {
    layout: 'horizontal',
    align: 'center',
    floating: false,
    backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
    shadow: true
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
    name: 'Humidité relative',
    type: 'spline',
    data: [],
    tooltip: {
      valueSuffix: ' %' 
    }
  }],
  //disable the nav export button
  navigation: {
    buttonOptions: {
      enabled: false
    }}
};
$.get('/static/shared/data/UQAM_DATA_STATION.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length; i++) {
        var cat = lines[i].split(",")[0]
        var firCol = lines[i].split(",")[1];
        var secCol = lines[i].split(",")[6];
        options2.series[0].data.push(parseFloat(firCol))
        options2.series[1].data.push(parseFloat(secCol))
    }

    // Create the chart
    chart = new Highcharts.Chart(options2);
});


///Panneau sur pression de surface

var options3 = {
    
  chart: {
    renderTo: 'graphdiv3',
    zoomType: 'xy'
  },
  title: {
    text: ' '
  },
  subtitle: {
    text: ' '
  },
    credits: {
      enabled: false
  }
    ,
   xAxis: [{
            type:'datetime',
            tickInterval:3600 * 1000 * 2,
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat('%H h', this.value);

                },

            }

        }],
  yAxis: [{ // Primary yAxis
     min: 980,
    labels: {
      format: '{value}',
      style: {
        color: Highcharts.getOptions().colors[3]
      }
    },
    title: {
      text: 'Pression [hPa]',
      style: {
        color: Highcharts.getOptions().colors[3]
      }
    }

  }
         ],
  tooltip: {
    shared: true,
    xDateFormat: '%e %b - %H h'
  },
  plotOptions: {
       series: {
           pointStart: yesterday,
            pointInterval: 3600000 // one hour
        },   
        area: {
             marker: {
              enabled: false
          }
      }
      }
    ,
    legend: {
    layout: 'horizontal',
    align: 'center',
    floating: false,
    backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
    shadow: true
  },

  series: [{
    name: 'Pression',
    type: 'area',
    data: [],
    tooltip: {
      valueSuffix: ' hPa'
    },
        color: Highcharts.getOptions().colors[3],
        fillColor: {
            linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
            stops: [
                [0, Highcharts.getOptions().colors[3]],
                [
                    1,
                    Highcharts.color(Highcharts.getOptions().colors[3])
                        .setOpacity(0.25).get()
                ]
            ]
        }

  } 
],
  //disable the nav export button
  navigation: {
    buttonOptions: {
      enabled: false
    }}
};
$.get('/static/shared/data/UQAM_DATA_STATION.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length; i++) {
        var cat = lines[i].split(",")[0]
        var Col = lines[i].split(",")[2];
        options3.series[0].data.push(parseFloat(Col))
    }

    // Create the chart
    chart = new Highcharts.Chart(options3);
});


///Panneau sur la direction du vent et le module
var options4 = {
    
  chart: {
    renderTo: 'graphdiv4',
    zoomType: 'xy'
  },
  title: {
    text: ' '
  },
  subtitle: {
    text: ' '
  },
    credits: {
      enabled: false
  }
    ,
   xAxis: [{
            type:'datetime',
           tickInterval:3600 * 1000 * 2,
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat('%H h', this.value);

                },

            }

        }],
   yAxis: [{ // Primary yAxis
    labels: {
      format: '{value}',
    },
    title: {
      text: 'Vitesse du vent [km.h-1]'
    }

  }
         ], 
    
   plotOptions: {
        series: {
            pointStart: yesterday,
            pointInterval: 3600000 // one hour
        },
       
        area: {
                    marker: {
                        enabled: false
                    }
                }
    }, 
    
    series: [{
        type: 'windbarb',
        data: [],
        name: 'Direction du vent',
        color: Highcharts.getOptions().colors[1],
        tooltip: {
            valueSuffix: ' km/h'
        }
    }, {
        type: 'area',
        keys: ['y', 'rotation'], // rotation is not used here
        data: [],
        color: Highcharts.getOptions().colors[0],
        fillColor: {
            linearGradient: { x1: 0, x2: 0, y1: 0, y2: 1 },
            stops: [
                [0, Highcharts.getOptions().colors[0]],
                [
                    1,
                    Highcharts.color(Highcharts.getOptions().colors[0])
                        .setOpacity(0.25).get()
                ]
            ]
        },
        name: 'Vitesse du vent',
        tooltip: {
            valueSuffix: ' km/h',
            xDateFormat: '%e %b - %H h'
        }
    }]  ,
  //disable the nav export button
  navigation: {
    buttonOptions: {
      enabled: false
    }

  }
};
$.get('/static/shared/data/UQAM_DATA_STATION.csv', function(data) {
    // Split the lines
    var lines = data.split('\n');

    // Push column data into data list
    for (var i =1; i < lines.length; i++) {
        var cat = lines[i].split(",")[0]
        var firCol = lines[i].split(",")[8];
        var secCol = lines[i].split(",")[7];
        options4.series[0].data.push([parseFloat(firCol),parseFloat(secCol)])
        options4.series[1].data.push([parseFloat(firCol),parseFloat(secCol)])
        
    }

    // Create the chart
    chart = new Highcharts.Chart(options4);
});

});

















